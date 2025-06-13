import streamlit as st
import requests

# Hugging Face Inference API URL
api_url = "https://api-inference.huggingface.co/models/openchat/openchat-3.5-1210"

# Streamlit app config
st.set_page_config(page_title="21Hash - Bitcoin Mining Assistant", layout="wide")

# Title + sidebar
st.title("🧠 21Hash: Open-Source Bitcoin Mining Assistant")
st.markdown("Ask anything about Bitcoin mining hardware, firmware, setup, or optimization.")

with st.sidebar:
    st.markdown("## Settings")
    temperature = st.slider("Response creativity (not functional for HF API)", 0.0, 1.0, 0.4)
    st.markdown("---")
    st.markdown("### 🔐 Privacy")
    st.markdown(
        "No IP addresses or personal identifiers are collected. Prompts and replies are sent to the Hugging Face API."
    )
    st.markdown("---")
    st.markdown("Created by the community for the community. [GitHub Repo](https://github.com/RealMoneyBTC/21Hash)")

# Function to query Hugging Face
def query_huggingface(payload):
    headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API error: {response.status_code} {response.text}")
        return None

# Chat logic
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
            if result and isinstance(result, list) and "generated_text" in result[0]:
                st.markdown(result[0]["generated_text"])
            else:
                st.error("No valid response received from the model.")
