import streamlit as st
from PIL import Image
st.set_page_config(page_title='Chicken', page_icon=":chicken:", layout= 'wide')
st.header('**Welcome to**')
st.subheader(':red[**The Chicken Empire**]')
st.subheader('_website_')
st.divider()
st.subheader('Recent News:')
st.text('Making Chicken Empire website...')
st.divider()
st.subheader('Wonderful portraits:')
st.image(Image.open('Chicks.png'), width=200)
st.divider()