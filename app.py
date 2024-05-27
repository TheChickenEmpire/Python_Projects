import streamlit as st
from PIL import Image
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('images.jpeg')
st.set_page_config(page_title='The_Chicken_Empire', page_icon=":chicken:", layout= 'wide')
st.header('Welcome')
st.subheader(' to the stem club website')
st.text("At STEM Club, we delve into the captivating world of coding and technological discoveries. \nOur mission is to cultivate a community of passionate individuals who are eager to unravel \nthe mysteries of science, technology, engineering, and mathematics. Whether you're a seasoned \nprogrammer or just starting your journey into the realm of technology, \nSTEM Club provides a vibrant and supportive environment where members can \ncollaborate, learn, and push the boundaries of their knowledge. \nFrom coding workshops to discussions on the latest breakthroughs in science and technology, \nthere's always something exciting happening at STEM Club.\nJoin us as we embark on a journey to unlock the endless possibilities of the digital age. \nTogether, let's inspire creativity, foster innovation, and shape the future through the power of STEM!")
teams,  = st.columns([1])
with teams:
    st.image(Image.open("Stem.png"), width= 600)
    st.markdown("https://teams.microsoft.com/v2/")
