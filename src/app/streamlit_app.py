import streamlit as st

st.title("Enterprise RAG Chatbot")

query = st.text_input("Ask anything:")

if st.button("Ask"):
    st.write("Response will appear here!")
