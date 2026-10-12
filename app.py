import streamlit as st
import joblib
import random

model = joblib.load("Chatbot.pkl")
vector = joblib.load("vector.pkl")
res = joblib.load("res.pkl")

st.title("Shivani's ChatBot")
st.write("Ask something to the chatbot")

# Chat history ko current session me save karein
if "chat" not in st.session_state:
    st.session_state.chat = []

# Purani chat dikhayein
for role, message in st.session_state.chat:
    with st.chat_message(role):
        st.write(message)

# User ka naya message lein
user = st.chat_input("You: ")

if user:
    # User ka message history me add karein
    st.session_state.chat.append(("user", user))

    user_vector = vector.transform([user]).toarray()
    predict = model.predict(user_vector)[0]

    if predict in res:
        reply = random.choice(res[predict])
    else:
        reply = "Maaf kijiye, mujhe iska jawab nahi pata."

    # Bot ka jawab history me add karein
    st.session_state.chat.append(("assistant", reply))

    # Nayi chat dikhane ke liye app rerun karein
    st.rerun()