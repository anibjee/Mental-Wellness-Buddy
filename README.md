# 🧠 Mental Wellness Buddy Chatbot

Welcome to the **Mental Wellness Buddy**, a Retrieval-Augmented Generation (RAG) based chatbot that provides **empathetic and evidence-based** responses to mental wellness concerns such as stress, anxiety, and depression. This project was built as part of the **IBM Adroit Program**.

🟢 **Try it live** → [https://mental-wellness-buddy.streamlit.app/](https://mental-wellness-buddy.streamlit.app/)

---

## 📌 Table of Contents

- [🌟 Features](#-features)
- [🚀 Hosted Web App](#-hosted-web-app)
- [📂 Project Structure](#-project-structure)
- [💻 Run the App Locally](#-run-the-app-locally)
- [🧪 Run in Jupyter Notebook](#-run-in-jupyter-notebook)
- [🔄 Data Preparation Workflow](#-data-preparation-workflow)
- [🛠️ Tech Stack & Libraries](#-tech-stack--libraries)
- [📄 License](#-license)
- [🤝 Contributing](#-contributing)

---

## 🌟 Features

- 💬 Human-like conversational experience
- 🧘 Empathy + practical advice for mental wellness
- 🔍 Semantic search powered by vector embeddings
- 🧠 LLM (LLaMA-3 via Groq) generates context-aware responses
- 🌐 Streamlit UI for easy interaction

---

## 🚀 Hosted Web App

Click below to experience the chatbot directly:

👉 [**mental-wellness-buddy.streamlit.app**](https://mental-wellness-buddy.streamlit.app/)

---

## 📂 Project Structure

```
.
├── chatbot_interface.py              # Streamlit frontend
├── chatbot_logic.py                  # LLM and RAG backend
├── Mental_Wellness_Chatbot_Main.ipynb # Jupyter-based version
├── retreiving_html.py                # Scrape HTML articles from URLs
├── Extract_Text.py                   # Clean and extract text from HTML
├── mental_wellness_articles.csv      # Source URLs by category
├── requirements.txt                  # Required Python packages
├── Text Extracted Files/             # Cleaned text files
├── HTML Files/                       # Raw HTML files
└── chroma_db/                        # Vector DB for semantic search
```

## 💻 Run the App Locally
To run the full chatbot as a web application on your machine:

### 1. Clone the Repository
```
git clone https://github.com/anibjee/IBM-Adroit-Project-Mental-Wellness-Chatbot
```
### 2. Open the folder where the repo was cloned
### 3. Install Required Packages
```
pip install -r requirements.txt
```
### 4. Set Up the Groq API Key
#### Create a folder called .streamlit:
```
mkdir .streamlit
```
#### Inside it, create a file called secrets.toml:
```
touch secrets.toml
```
#### Paste the content below inside secrets.toml
```
GROQ_API_KEY = "your_groq_api_key_here"
```
#### 🔑 You can get your API key from: https://console.groq.com/keys

### 5. Run the Chatbot Web App
```
streamlit run chatbot_interface.py
```

## 🧪 Run in Jupyter Notebook
If you want to experiment with the chatbot directly in a notebook:

### 1. Clone the Repository
```
git clone https://github.com/anibjee/IBM-Adroit-Project-Mental-Wellness-Chatbot
```
### 2. Open the folder where the repo was cloned
### 3. Set Up the Groq API Key
Create a folder called .streamlit:
```
mkdir .streamlit
```
#### Inside it, create a file called secrets.toml:
```
touch secrets.toml
```
#### Paste the content below inside secrets.toml
```
GROQ_API_KEY = "your_groq_api_key_here"
```
### 🔑 You can get your API key from: https://console.groq.com/keys

### 4. Open Mental_Wellness_Chatbot_Main.ipynb in Jupyter
### 5. Run all cells to interact with the chatbot in notebook mode

#### 💡 This mode is ideal for debugging, experimentation, and modifying internal logic.

## 🔄 Data Preparation Workflow
This section describes how to recreate the full pipeline from external data scraping to vector embedding.

### 1. Start with the Article CSV
#### Edit or use the existing mental_wellness_articles.csv file.
#### You can also add new url to the existing topics
#### Each row should look like this:
```
Topic,URL 1,URL 2,URL 3,...
Anxiety,https://example.com/article1,https://example.com/article2
Depression,...
```

### 2. Retrieve Web Articles
Run the following command:
```
python retreiving_html.py
```
#### This script:
#### Reads the CSV file
#### Downloads HTML from all URLs
#### Saves files in topic-wise folders inside /HTML Files

### 3. Extract Text from HTML
Then run:
```
python Extract_Text.py
```
#### This script:
#### Parses all HTML files using BeautifulSoup
#### Extracts meaningful content
#### Saves clean .txt files in /Text Extracted Files
#### These cleaned text files are later used to create a vector database for semantic search.

## 🛠️ Tech Stack & Libraries
### Frontend: Streamlit

### LLM API: Groq — LLaMA-3

### Embeddings: SentenceTransformers – all-MiniLM-L6-v2

### Vector Store: ChromaDB

### Framework: LangChain

### Scraping: requests, fake-useragent, BeautifulSoup

### Notebook Dev: Jupyter, Google Colab

### Language: Python 3.x


## 🤝 Contributing
### We welcome contributions of all kinds!

### 📥 Submit pull requests

### 🐛 Report issues

### 🌱 Suggest features

# Made with ❤️ by Aniruddha Bhattacharjee
