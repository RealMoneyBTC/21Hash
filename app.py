import streamlit as st
import requests

# Your Hugging Face Space API endpoint
api_url = "https://RealMoneyBTC-21hash-assistant.hf.space/predict"

st.set_page_config(page_title="21Hash - Bitcoin Mining Assistant", layout="wide")

st.title("🧠 21Hash: Open-Source Bitcoin Mining Assistant")
st.markdown("Ask anything about Bitcoin mining hardware, firmware, setup, or optimization.")

with st.sidebar:
    st.markdown("## Settings")
    st.markdown("This version connects to your Hugging Face Space for responses.")
    st.markdown("---")
    st.markdown("### 🔐 Privacy")
    st.markdown(
        "No IP addresses or personal identifiers are collected. Prompts are sent to your Hugging Face Space API."
    )
    st.markdown("---")
    st.markdown("Created by the community for the community. [GitHub Repo](https://github.com/RealMoneyBTC/21Hash)")

def query_huggingface(prompt):
    try:
        response = requests.post(api_url, json={"prompt": prompt})
        if response.status_code == 200:
            return response.json()["response"]
        else:
            st.error(f"API error: {response.status_code} {response.text}")
            return None
    except Exception as e:
        st.error(f"Exception: {str(e)}")
        return None

# Chat input and output
user_input = st.chat_input("Ask your Bitcoin mining question here...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            prompt = f"You are a Bitcoin mining expert. {user_input}"
            reply = query_huggingface(prompt)
            if reply:
                st.markdown(reply)
            else:
                st.error("No valid response received from the model.")
