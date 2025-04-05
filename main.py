import streamlit as st
import google.generativeai as genai
import requests

# Configure Gemini API
genai.configure(api_key="AIzaSyBSiY9Mi1db3LMDj8Py2YYBAsG_IHmIRwY")

model = genai.GenerativeModel("gemini-1.5-pro")

# Streamlit UI
st.set_page_config(page_title="🚀 SpaceBot", layout="centered")
st.title("🌌 Space Exploration Chatbot")

user_input = st.text_input("Ask me something about space:")

# Free API Functions
def get_iss_location():
    res = requests.get("http://api.open-notify.org/iss-now.json").json()
    pos = res['iss_position']
    return f"The ISS is at:\nLatitude: {pos['latitude']}, Longitude: {pos['longitude']}"

def get_astronauts():
    res = requests.get("http://api.open-notify.org/astros.json").json()
    people = [p['name'] for p in res['people']]
    return f"There are {len(people)} astronauts in space:\n" + ', '.join(people)

def get_apod():
    nasa_key = "w14IH6vVFpo5jcCIFgm7jCIWYMZzMOTqk6FRgQdG"  # Replace with your own if you have one
    url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_key}"
    res = requests.get(url).json()
    return f"📷 {res['title']}\n\n{res['explanation']}\n\nImage: {res['url']}"

def ask_gemini(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Process input
if user_input:
    if "iss" in user_input.lower():
        st.success(get_iss_location())
    elif "astronaut" in user_input.lower():
        st.success(get_astronauts())
    elif "picture" in user_input.lower() or "apod" in user_input.lower():
        st.success(get_apod())
    else:
        answer = ask_gemini(user_input)
        st.info(answer)
