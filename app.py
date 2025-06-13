import streamlit as st
import openai

client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("21Hash OpenAI Connection Test")

if st.button("Run test API call"):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello"}
            ]
        )
        st.success("API call successful!")
        st.write(response.choices[0].message.content)
    except Exception as e:
        st.error(f"⚠️ API call failed: {e}")
