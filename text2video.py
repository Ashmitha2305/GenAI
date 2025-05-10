import streamlit as st
import requests

API_KEY = "your_did_api_key"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

st.title("Text to Video (Avatar)")

text_input = st.text_input("Enter text for the avatar to speak:")

if st.button("Generate Video"):
    payload = {
        "script": {"type": "text", "input": text_input},
        "source_url": "https://create.avatar.url"  # Use a default avatar
    }

    response = requests.post("https://api.d-id.com/talks", json=payload, headers=HEADERS)
    if response.status_code == 200:
        video_url = response.json().get("result_url")
        st.video(video_url)
    else:
        st.error("Video generation failed.")
