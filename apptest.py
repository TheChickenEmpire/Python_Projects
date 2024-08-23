import streamlit as st
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
st.set_page_config('TEST', "🧪")
st.header(':rainbow[_____-----Chipbot Assistant-----_____]')
with st.chat_message('🍟'):
    st.info(chat('hi, hello, where can i find the comics, who is your favoirite youtuber, how do i get into the subscribers section on this website, how did you lose your channel, what is your favoirite food, Okay, what are you, are you happy, are you alive, English or spanish, what are you doing, whos the stupidest person in the world',
                'hello, hi, up here ^^^^^^^^^^, The Chicken Empire you can check out his channel here>>>https://www.youtube.com/@TheChickenEmpire, you just need to sunscribe to the chicken empire, i accidently deleted because of google, mcdonalds, yeah, Im a assistant created by the website designer who also created The Chicken Empire, yes under circumstances, No well accordingly, Ancient greek, nothing, Ethan'))