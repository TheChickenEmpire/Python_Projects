import streamlit as st
from PIL import Image
st.set_page_config(page_title='The_Chicken_Empire', page_icon=":chicken:", layout= 'wide')
with st.container():
    st.subheader("This is a test run")
Im = Image.open('sub.png')
st.image(Im)
#python -m streamlit run app.py