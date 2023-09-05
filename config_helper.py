
import streamlit as st
import openai

def setup_config():
    # Set Streamlit page configuration
    st.set_page_config(page_title="Ask Noble | Virtual Agent", page_icon="🤖", layout="centered")
    
    # Set OpenAI API key
    try:
        openai.api_key = st.secrets.get("openai_key", "default_key")
    except AttributeError:
        st.error("OpenAI key not found in secrets.")
