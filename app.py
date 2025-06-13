import streamlit as st
import requests

# Using public Space API endpoint
api_url = "https://huggingface.co/spaces/project-baize/chat-with-baize/api/predict/"

st.set_page_config(page_title="21Hash - Bitcoin Mining Assistant", layout="wide")
st.title("🧠 21Hash: Open-Source Bitcoin Mining Assistant")
st.markdown("Ask anything about Bitcoin mining hardware, firmware, setup, or optimization.")

with st.sidebar:
    st.markdown("### ⚙️ Demo Powered by Public HF Space")
    st.markdown("---")
    st.markdown("▶️ No API key required — working out-of-the-box")

def query_public_space(prompt):
    try:
        payload = {"data": [prompt]}
        resp = requests.post(api_url, json=payload)
        if resp.status_code == 200:
            return resp.json()["data"][0]
        else:
            st.error(f"API error: {resp.status_code} {resp.text}")
            return None
    except Exception as e:
        st.error(f"Exception: {e}")
        return None

user_input = st.chat_input("Ask your Bitcoin mining question here...")
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = query_public_space(user_input)
            if reply:
                st.markdown(reply)
            else:
                st.error("No valid response received.")
