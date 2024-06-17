import first_langchain as lg
import streamlit as st

st.title("Essay")
st.header("Say us the name and we'll do the research for you")

name = st.text_area("whom you want to know about?", max_chars = 50)
button = st.button("Get Essay")
if button:
    response = lg.research(name)
    st.write(response)
