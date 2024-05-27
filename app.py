import streamlit as st
from PIL import Image
st.set_page_config(page_title='The_Chicken_Empire', page_icon=":chicken:", layout= 'wide')
st.image(Image.open("Stem.png"))
st.page_link("https://teams.microsoft.com/v2/", 'For Teams Click Here')