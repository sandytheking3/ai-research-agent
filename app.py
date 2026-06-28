import streamlit as st

st.title("Ai Reasearch agent: ")

question = st.text_input("Enter your reasearch question:")

if question:
    st.write("YOu asked: ", question)