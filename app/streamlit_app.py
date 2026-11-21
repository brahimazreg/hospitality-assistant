import streamlit as st
import requests
import os 

# Get the directory containing this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Image path
HOTEL_ICON = os.path.join(BASE_DIR, "oasis.jpeg")

# Application header
col1, col2 = st.columns([1, 5], vertical_alignment="center")

with col1:
    st.image(HOTEL_ICON, width=500)

with col2:
    st.title("Sahab Oasis Hotel")
# Page configuration
st.set_page_config(
    page_title="Sahab Oasis Hotel Assistant",
    page_icon=HOTEL_ICON,
    layout="centered"
)


st.subheader("Your Multilingual Hotel Assistant")

# Language selection
if "language" not in st.session_state:
    st.session_state.language = "English"

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🇬🇧 English", use_container_width=True):
        st.session_state.language = "English"

with col2:
    if st.button("🇫🇷 Français", use_container_width=True):
        st.session_state.language = "French"

with col3:
    if st.button("🇸🇦 العربية", use_container_width=True):
        st.session_state.language = "Arabic"

# Welcome messages
welcome_messages = {
    "English": "Ask me anything about our hotel.",
    "French": "Posez-moi vos questions sur notre hôtel.",
    "Arabic": "يمكنك طرح أي سؤال حول فندقنا."
}

st.write(welcome_messages[st.session_state.language])

# FastAPI backend URL

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/ask"
)

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear conversation button
if st.button("🗑️ Clear conversation"):
    st.session_state.messages = []
    st.rerun()

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
input_placeholders = {
    "English": "Ask your question...",
    "French": "Posez votre question...",
    "Arabic": "اكتب سؤالك هنا..."
}

question = st.chat_input(input_placeholders[st.session_state.language])

if question:

    # Display user question
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Call FastAPI
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=120
                )

                response.raise_for_status()

                answer = response.json()["answer"]

                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except requests.exceptions.RequestException as error:
                st.error(f"Could not contact the AI assistant: {error}")