import streamlit as st
from PIL import Image
import difflib
def chat(asks: str, ans: str):
    """Use this function for chatbots
    By typing for example chat('Hi, Hello',
                                                                                                Hi, Greetings)
    It will return the Answer of the closest question Line 1 is Questions 
    line 2 is answers"""
    asks = asks.lower()
    ans = ans.lower()
    asks = asks.split(', ')
    ans = ans.split(', ') 
    ask = str(st.chat_input('Message')).lower()
    if ask == 'none':
        return('')
    else:
        e = difflib.get_close_matches(ask, asks, 1)
        try:
            e = e[0]
            e = str(e)
            e = e.replace('[', '')
            e = e.replace(']', '')
            e = e.replace("'", '')
            index = asks.index(e)
            return('User:'+ask.capitalize()+'\n\nChipbot:\n'+ans[index].capitalize())
        except: 
            return("Im sorry I don't understand what you mean")
st.set_page_config(page_title='Chicken Empire', page_icon=":chicken:", layout= 'wide')
st.logo(Image.open('Chicken.png'))
with st.sidebar:
    st.header(':rainbow[_____-----Chipbot Assistant-----_____]')
    with st.chat_message('🍟'):
        st.info(chat('hi, hello, where can i find the comics, who is your favoirite youtuber, how do i get into the subscribers section on this website, how did you lose your channel, what is your favoirite food, Okay, what are you, are you happy, are you alive, English or spanish, what are you doing, whos the stupidest person in the world, Are you smart, Youre stupid, Okay You idiot',
                     'hello, hi, up down here VVVVVVV, The Chicken Empire you can check out his channel here>>>https://www.youtube.com/@TheChickenEmpire, you just need to sunscribe to the chicken empire, i accidently deleted because of google, mcdonalds, yeah, Im a assistant created by the website designer who also created The Chicken Empire, yes under circumstances, No well accordingly, Ancient greek, nothing, Ethan, Maybe, Do I care.... No!, Why are you so mean....... Just kidding you no home no life no brain no parents orphan'))
    st.divider()
    st.subheader(':rainbow[My channel]')
    st.link_button("Channel", 'https://www.youtube.com/@TheChickenEmpire')
    st.divider()
    st.subheader(':rainbow[Chicken Empire Comics]')
    st.link_button("Comics", 'https://thechickenempirecomic.streamlit.app/')
    st.markdown('Made by Oscar :red[**WARNING THERE IS \nA BIT OF BLOOD**]')
st.header('Welcome to')
st.header(':rainbow[**The Chicken Empire**]')
st.subheader('_website_') 
st.divider()
st.subheader('Recent News:')
st.text(st.secrets["RecentNews"])
st.divider()
st.subheader('About Me')
st.text('Hi im a youtuber who likes coding\nwe all have dreams\nand If you Subscribe\nyou would be helping\nme fulfil mine\nplease\n\/\/\/') 
st.link_button('Click Here Plz', 'https://www.youtube.com/@TheChickenEmpire')
st.divider()
st.subheader('My Subscribers')
st.text("")
st.divider()
st.subheader('History:')
st.text('June 23:\nChicken Empire Created\n\nJuly:\nChicken Empire faces war\n\n2024:\nYoutube channel starts\n\nMarch 2024 - April 2024:\nChannel thrives\n\nApril 24 - June 24:\nChannel views and subs drop of me going back to school\n\nJune 24:\nI create this website\n\n')
st.divider()
st.subheader('Wonderful portraits:')
st.image(Image.open('1.png'), width=400)
st.text('Credits: By Oscar')
st.image(Image.open('Victory.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('CE Poster (Portrait).png'), width=400)
st.text('Credits: By Zxjoshua33(My Friend)')
st.image(Image.open('James.png'), width=400)
st.text('Credits: By OppositeAce8412(My Friend)')
st.image(Image.open('Standard.png'), width=400) 
st.text('Credits: By Zxjoshua33(My Friend)')
st.image(Image.open('James1.png'), width=400) 
st.text('Credits: By OppositeAce8412(My Friend)')
st.image(Image.open('Rizzkens.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Chick (1).png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Sigma.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Chicks.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('The Chicken Empire.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Burn.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Mew.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Rock.png'), width=400)
st.text('Credits: By Me')
st.image(Image.open('Roost.png'), width=400)
st.text('Credits: By Me')
st.divider()
st.subheader('Credits')
st.text('Oscar\nDonnie(My other friend)\nZxJoshua33(You should go see his channel)\nOppositeAce8412(You should go see his channel)\nChickens\nEthan(My other friend)')
if st.checkbox(''):
    if st.text_input('Password:').lower() == str(st.secrets['Password']).lower():
        pass