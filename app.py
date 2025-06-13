import streamlit as st
import requests

# Hugging Face Space URL — using a public Mistral-7B Instruct Space (no API key needed for many public Spaces)
api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

st.set_page_config(page_title="21Hash - Bitcoin Mining Assistant", layout="wide")

st.title("🧠 21Hash: Open Mining Assistant (Hugging Face)")
st.markdown("Ask anything about Bitcoin mining hardware, firmware, setup, or optimization.")

with st.sidebar:
    st.markdown("## Settings")
    temperature = st.slider("Response creativity (placeholder, not functional in HF API)", 0.0, 1.0, 0.4)
    st.markdown("---")
    st.markdown("### 🔐 Privacy")
    st.markdown(
        "No IP addresses, usernames, or personal identifiers are collected. "
        "Prompts and replies are sent to Hugging Face's API. "
        "All use is anonymous and intended to improve mining knowledge."
    )
    st.markdown("---")
    st.markdown("Created by the community for the community. [GitHub Repo](https://github.com/RealMoneyBTC/21Hash)")

def query_huggingface(payload):
    response = requests.post(api_url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API error: {response.status_code} {response.text}")
        return None

user_input = st.chat_input("Ask your Bitcoin mining question here...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            payload = {
                "inputs": f"You are a Bitcoin mining expert. {user_input}"
            }
            result = query_huggingface(payload)
            if result and isinstance(result, list):
                st.markdown(result[0]["generated_text"])
