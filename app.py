import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import time
import random


HF_API_KEY = st.secrets["HUGGING_FACE_API_KEY"] # Insert your Hugging Face API Key/Token here
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

# Hugging Face API endpoint
MODEL_NAME = "stabilityai/stable-diffusion-xl-base-1.0" # Insert your model name here
MODEL_API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

st.set_page_config(page_title="AI Visionary", layout="wide")

st.markdown(
    """
    <style>
        .nav-bar  {
            display: flex;
            align-items: center;
            color: white;
            position: relative;
        }
        .logo {
            height: 100px;
            margin-left: 10px;
        }
        .title {
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            font-size: 40px;
            font-weight: bold;
            white-space: nowrap;
        }
    </style>
    <div class="nav-bar">
        <img src="https://iili.io/3dopqMu.th.png" class="logo">
        <span class="title">AI Visionary</span>
    </div>
    """,
    unsafe_allow_html=True
)

prompt = st.text_input("prompt", placeholder="Enter a prompt", label_visibility="hidden")

# **Function to Generate Image**
def generate_image(prompt):
    request_id = time.time() + random.random()
    data = {"inputs": prompt, "request_id": request_id}
    response = requests.post(MODEL_API_URL, headers=headers, json=data)
    response.raise_for_status()
    return response

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        try:
            response = generate_image(prompt)
            st.session_state.generated_image = response.content 
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")

if "generated_image" in st.session_state:
    img = Image.open(BytesIO(st.session_state.generated_image))

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, width=650)
        st.download_button(
            label="Download Image",
            data=st.session_state.generated_image,
            file_name="generated_image.png",
            mime="image/png"
        )
