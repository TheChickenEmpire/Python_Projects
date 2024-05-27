import streamlit as st
from PIL import Image
import keyboard
st.set_page_config(page_title='The_Chicken_Empire', page_icon=":chicken:", layout= 'wide')
st.header('Learn about stem club')
st.text("Stem club is a place in lunch that you can code, learn, 3dmodel and more!!!\nIt is also free and gives you opportunities to learn to code for\nexample if you don't have time at home you can learn to make games\nand learn how to 3d model and we also have fun projects sometimes\nso if your interested come meet at N5 Matamoe Hub at Lunch time and bring your computer")
st.image(Image.open('images.png'))
if st.button('Back to main'):
    keyboard.press_and_release('ctrl+w')
    