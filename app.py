import streamlit as st
from PIL import Image
st.set_page_config(page_title='Chicken', page_icon=":chicken:", layout= 'wide')
hi1, hi2 = st.columns([1,1])
with hi1:
    st.header('**Welcome to**')
with hi2:
    st.image(Image.open('Chicks.png'), width=100)
st.subheader(':red[**The Chicken Empire**]')
st.subheader('_website_')
st.text('')
st.text('')
st.subheader('Recent News:')
st.text('Making Chicken Empire website')