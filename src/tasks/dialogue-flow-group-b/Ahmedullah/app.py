import streamlit as st
import requests

# Function to Get Chatbot Response


def get_chatbot_response(user_input, rasa_url):
    payload = {"message": user_input}
    headers = {"Content-Type": "application/json"}
    response = requests.post(rasa_url, json=payload, headers=headers)
    bot_response = response.json()
    return bot_response[0]["text"]


# Streamlit App Title
st.title("Chatbot")

# Rasa Server URL
rasa_url = "http://localhost:5005/webhooks/rest/webhook?model=default"

# User Input
user_input = st.text_input("You:", "")

# Send User Input and Get Chatbot Response
if st.button("Send"):
    if user_input.strip() != "":
        bot_response = get_chatbot_response(user_input, rasa_url)
        st.text_area("Chatbot:", bot_response)
