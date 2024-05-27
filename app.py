import streamlit as st
from PIL import Image
st.header('Welcome')
st.subheader(' to the stem club website')
st.set_page_config(page_title='The_Chicken_Empire', page_icon=":chicken:", layout= 'wide')
teams,  = st.columns([1])
with teams:
    st.image(Image.open("Stem.png"), width= 600)
    st.markdown("https://teams.microsoft.com/v2/")