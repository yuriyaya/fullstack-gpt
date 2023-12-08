import streamlit as st

st.selectbox("Choose your model", ("GPT-3", "GPT-4"))

name = st.text_input("What is your name?")

st.write(name)