import streamlit as st
import requests

st.set_page_config(page_title="AI Space Chatbot", page_icon="🛰️")
st.title("🚀 Space Exploration AI Chatbot")

# Hugging Face token
HF_TOKEN = "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"


# Function to call Hugging Face API
def query_huggingface(prompt):
    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result[0]['generated_text']
    else:
        return "🤖 Sorry, the AI is on a coffee break right now."


# Chat interface
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("👨‍🚀 You:", placeholder="Plan a mission to Mars", key="input")

if user_input:
    prompt = f"You are an expert space mission planner AI. Help with: {user_input}"
    with st.spinner("Thinking... 🚀"):
        ai_reply = query_huggingface(prompt)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("AI", ai_reply))

# Display chat
for speaker, msg in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**🧑‍🚀 You:** {msg}")
    else:
        st.markdown(f"**🤖 AI:** {msg}")
