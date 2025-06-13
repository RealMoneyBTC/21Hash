import streamlit as st

st.set_page_config(page_title="21Hash - Bitcoin Mining Assistant", layout="wide")

st.title("🧠 21Hash: Open-Source Bitcoin Mining Assistant")
st.markdown("Ask anything about Bitcoin mining hardware, firmware, setup, or optimization.")

with st.sidebar:
    st.markdown("## Settings")
    st.markdown("This version is currently in placeholder mode while we finalize backend integration.")
    st.markdown("---")
    st.markdown("### 🔐 Privacy")
    st.markdown(
        "No IP addresses or personal identifiers are collected. This app will connect to an open AI backend soon."
    )
    st.markdown("---")
    st.markdown("Created by the community for the community. [GitHub Repo](https://github.com/RealMoneyBTC/21Hash)")

user_input = st.chat_input("Ask your Bitcoin mining question here...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        st.warning("Backend integration is not active. Please check back soon.")
