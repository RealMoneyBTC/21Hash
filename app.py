import streamlit as st
import openai
import os
from datetime import datetime
import json

# Load OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set page config
st.set_page_config(page_title="21Hash - Bitcoin Mining Assistant", layout="wide")

# Title
st.title("🧠 21Hash: Open Mining Assistant")
st.markdown("Ask anything about Bitcoin mining hardware, firmware, setup, or optimization.")

# Sidebar
with st.sidebar:
    st.markdown("## Settings")
    temperature = st.slider("Response creativity", 0.0, 1.0, 0.4)
    st.markdown("---")
    st.markdown("### 🔐 Privacy")
    st.markdown(
        "We do **not** collect IP addresses, usernames, or any personal identifiers. "
        "All logged questions and answers are anonymous and used solely to improve the assistant "
        "for the Bitcoin mining community. This is an open-source, community-first project."
    )
    st.markdown("---")
    st.markdown("Created by the community for the community. [GitHub Repo](https://github.com/RealMoneyBTC/21Hash)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Static system prompt
prompt_context = """You are 21Hash, an AI assistant built for the Bitcoin mining community.
You specialize in mining hardware (like Antminer S19/S21 and WhatsMiner models),
firmware (BraiinsOS, LuxOS), immersion cooling setups, energy optimization, and diagnostics.

Provide helpful, technically accurate, and beginner-friendly answers. When needed, ask for more context.

Be concise, honest, and assume the user is operating real mining equipment.
"""

# Logging function
def log_interaction(question, answer):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "answer": answer,
        "feedback": "unmarked"
    }
    try:
        with open("chat_log.json", "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        st.error("⚠️ Could not save interaction log.")

# Chat input logic
user_input = st.chat_input("Ask your Bitcoin mining question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                temperature=temperature,
                messages=[
                    {"role": "system", "content": prompt_context},
                    *st.session_state.messages
                ]
            )
            answer = response.choices[0].message.content
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
            log_interaction(user_input, answer)
        except Exception as e:
            st.error("⚠️ There was an error generating a response.")
