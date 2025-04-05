import streamlit as st
import google.generativeai as genai
import requests

# ==== 🌌 PAGE CONFIG ====
st.set_page_config(
    page_title="🚀 SpaceBot",
    layout="centered",
    page_icon="🌠"
)

# ==== 🎨 SOFT DARK-LIGHT UI ====
st.markdown("""
    <style>
        .stApp {
            background-color: #1a1a1a;
            color: #f0f0f0;
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            text-align: center;
            color: #ffffff;
        }
        .stTextInput input {
            background-color: #333333;
            color: #ffffff;
            border: 1px solid #555555;
        }
        .stButton>button {
            background-color: #444;
            color: white;
            border-radius: 6px;
            padding: 0.5em 1em;
            border: none;
        }
        .stMarkdown {
            font-size: 16px;
            line-height: 1.6;
        }
    </style>
""", unsafe_allow_html=True)

# ==== 🔑 CONFIGURE GEMINI ====
genai.configure(api_key="AIzaSyBSiY9Mi1db3LMDj8Py2YYBAsG_IHmIRwY")
model = genai.GenerativeModel("gemini-1.5-pro")

# ==== 🚀 TITLE ====
st.markdown("<h1>🚀 SpaceBot: Your Cosmic Companion</h1>", unsafe_allow_html=True)

# ==== 👽 USER INPUT ====
user_input = st.text_input("💬 Ask me something about space:", placeholder="e.g. What is a black hole?")

# ==== 🌍 ISS LOCATION ====
def get_iss_location():
    res = requests.get("http://api.open-notify.org/iss-now.json").json()
    pos = res['iss_position']
    return f"🛰️ The ISS is currently at:\n🌐 Latitude: {pos['latitude']}, Longitude: {pos['longitude']}"

# ==== 👨‍🚀 ASTRONAUTS ====
def get_astronauts():
    res = requests.get("http://api.open-notify.org/astros.json").json()
    people = [p['name'] for p in res['people']]
    return f"👨‍🚀 There are {len(people)} astronauts in space:\n🔹 " + '\n🔹 '.join(people)

# ==== 🌌 NASA APOD ====
def get_apod():
    nasa_key = "w14IH6vVFpo5jcCIFgm7jCIWYMZzMOTqk6FRgQdG"
    url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_key}"
    res = requests.get(url).json()
    return f"📸 **{res['title']}**\n\n{res['explanation']}\n\n🖼️ [View Image]({res['url']})"

# ==== 🤖 GEMINI RESPONSE ====
def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"

# ==== 🎯 HANDLE INPUT ====
if user_input:
    input_lower = user_input.lower()
    if "iss" in input_lower:
        st.success(get_iss_location())
    elif "astronaut" in input_lower:
        st.success(get_astronauts())
    elif "picture" in input_lower or "apod" in input_lower:
        st.success(get_apod())
    else:
        st.info(ask_gemini(user_input))
