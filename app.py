import streamlit as st
from PIL import Image
st.set_page_config(page_title='Chicken', page_icon=":chicken:", layout= 'wide')
hi = st.columns(3)
with hi:
    st.header('**Welcome to**')
with hi:
    st.image(Image.open('Chicks.png'))
st.subheader(':red[**The Chicken Empire**]')
st.subheader('_website_')
st.text('')
st.text('')
st.subheader('Recent News:')
st.text('Making Chicken Empire website')