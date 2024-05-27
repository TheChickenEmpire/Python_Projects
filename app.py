import streamlit as st
from PIL import Image
st.set_page_config(page_title='Stem Club', page_icon=":chicken:", layout= 'wide')
st.header('Welcome')
st.subheader(' to the stem club website')
st.text("At STEM Club, we delve into the captivating world of coding and technological discoveries. \nOur mission is to cultivate a community of passionate individuals who are eager to unravel \nthe mysteries of science, technology, engineering, and mathematics. Whether you're a seasoned \nprogrammer or just starting your journey into the realm of technology, \nSTEM Club provides a vibrant and supportive environment where members can \ncollaborate, learn, and push the boundaries of their knowledge. \nFrom coding workshops to discussions on the latest breakthroughs in science and technology, \nthere's always something exciting happening at STEM Club.\nJoin us as we embark on a journey to unlock the endless possibilities of the digital age. \nTogether, let's inspire creativity, foster innovation, and shape the future through the power of STEM!")
teams, im = st.columns([1,1])
with teams:
    st.image(Image.open("Stem.png"), width= 600)
    st.markdown("https://teams.microsoft.com/v2/")
    st.link_button('Learn More', 'https://stemclublearn.streamlit.app/')
with im:
    st.image(Image.open("r.png"), width= 300)