import streamlit as st
from PIL import Image
st.set_page_config(page_title='Chicken', page_icon=":chicken:", layout= 'wide')
st.header('**Welcome to**', 100)
st.subheader(':red[**The Chicken Empire**]')
st.subheader('_website_')
st.text('')
st.text('')
st.subheader('Recent News:')
st.text('Making Chicken Empire website...')
st.subheader('Wonderful portrait:')
st.image(Image.open('Chicks.png'), width=200)