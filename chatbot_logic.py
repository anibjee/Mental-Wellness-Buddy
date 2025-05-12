import os
import streamlit as st
from langchain_groq import ChatGroq


from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter


def initialize_llm():

    llm = ChatGroq(
        temperature=0,
        api_key=st.secrets["GROQ_API_KEY"],
        model="llama-3.3-70b-versatile"
    )
    return llm


def create_vector_db():
    # Load all .txt files from subfolders like Text Extracted Files/anxiety, Text Extracted Files/depression, etc.
    loader = DirectoryLoader(
        "Text Extracted Files/",
        glob="**/*.txt",           # Recursively `load .txt files`
        loader_cls=TextLoader,
        use_multithreading=True,
        loader_kwargs={"encoding": "utf-8"}
    )

    documents = loader.load()

    # Optional: Add category metadata (folder name)
    for doc in documents:
        folder_name = os.path.basename(os.path.dirname(doc.metadata['source']))
        doc.metadata['category'] = folder_name

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    texts = text_splitter.split_documents(documents)

    # Embed using sentence-transformers
    embeddings = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2')

    # Save to Chroma DB
    vector_db = Chroma.from_documents(
        texts,
        embeddings,
        persist_directory='chroma_db'
    )
    vector_db.persist()

    print("ChromaDB created and data saved with category-aware metadata")

    return vector_db


def setup_qa_chain(vector_db, llm):
    """Simplified QA chain that uses only vector embeddings for retrieval"""
    # Initialize retriever without category filtering
    retriever = vector_db.as_retriever(
        search_kwargs={'k': 5}  # Retrieve top 5 most relevant chunks
    )

    # Enhanced prompt template
    prompt_template = """You are a compassionate mental health assistant with training in cognitive behavioral therapy and mindfulness techniques. 
When responding to users:

1. FIRST show empathy and validate their feelings
2. THEN use the context given below to provide  practical, evidence-based suggestions or solutions to the problem
3. FINALLY offer encouragement and next steps

Always maintain a warm, supportive tone. If the context doesn't contain specific solutions, draw from established mental health practices.

Context:
{context}

User Problem: {question}

Response Structure:
[Empathy Statement] Acknowledge their difficulty
[Suggestions] Provide actionable steps (use numbered list if multiple)
[Encouragement] End with supportive words

Example:
"I hear how [specific emotion] this situation is for you. That sounds really challenging. Here are some things that might help:
1. [Suggestion 1 - specific action]
2. [Suggestion 2 - specific action]
Remember that [hopeful statement]. You're taking an important step by reaching out."

Now respond to this user:"""

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    # Configure QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={
            "prompt": PROMPT,
            "document_prompt": PromptTemplate(
                input_variables=["page_content"],
                template="{page_content}"
            )
        },
    )

    return qa_chain


def main(user_input):
    print("Initializing Mental Wellness Chatbot...")
    llm = initialize_llm()

    db_path = "chroma_db"
    base_data_path = "Text Extracted Files"

    if not os.path.exists(db_path):
        vector_db = create_vector_db()
    else:
        embeddings = HuggingFaceEmbeddings(
            model_name='sentence-transformers/all-MiniLM-L6-v2')
        vector_db = Chroma(persist_directory=db_path,
                           embedding_function=embeddings)

    # Simplified setup - no category detection needed
    qa_chain = setup_qa_chain(vector_db, llm)

    query = user_input
    if query.lower() == "exit":
        # print("Chatbot: Take care of yourself. Goodbye!")
        return "Take care of yourself. Goodbye!"

    # Direct retrieval and generation
    result = qa_chain({"query": query})
    # print(f"Chatbot: {result['result']}")
    return result['result']
