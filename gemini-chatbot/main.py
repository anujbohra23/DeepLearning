import streamlit as st
import os
from dotenv import load_dotenv
import numpy as np
import google.generativeai as genai


load_dotenv()

#streamlit layout
st.set_page_config(
    page_title = "Gemini Chatbot",
    page_icon = ":brain:",
    layout = "wide"
)

#api
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#model
genai.configure(api_key = GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

#function to translate role between streamlit and gemeini
def translate_streamlit(user_role):
    if user_role == 'model':
        return "assistant"
    else:
        return user_role

#initialising chat session if not already present  
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    
st.title("Gemini Chatbot")

#to display history of messages
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_streamlit(message.role)):
        st.markdown(message.parts[0].text)
        
user_prompt = st.chat_input("Ask Questions:")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
    
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
    