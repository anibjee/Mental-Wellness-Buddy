import streamlit as st
import random
import time
from chatbot_logic import main


st.set_page_config(page_title="Mental Wellness Buddy", page_icon="🧠")

# App title with a more friendly UI
st.markdown("""
    <h1 style='text-align: center; color: #0d6efd; margin-bottom: 30px;'>
        Mental Wellness Buddy 🧠
    </h1>
""", unsafe_allow_html=True)

# Streamed response emulator


def response_generator(user_input):
    response = main(user_input)
    output_array = []
    for sen in response.split("\n"):
        for word in sen.split():
            output_array.append(word)
        output_array.append("\n")

    for word in output_array:
        if word == "\n":
            yield word
        else:
            yield word + " "
        time.sleep(0.05)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add a welcome message when the app first loads
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hi there! I'm your Mental Wellness Buddy. How are you feeling today?"
    })

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Share your thoughts..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
