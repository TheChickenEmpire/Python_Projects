import streamlit as st
from PIL import Image
from datetime import datetime
st.set_page_config(page_title='Chicken Empire', page_icon=":chicken:", layout= 'wide')
st.logo(Image.open('Chicken.png'))
st.subheader('Welcome to')
st.header(':rainbow[**The Chicken Empire**]')
st.subheader('_website_') 
st.divider()
st.subheader('Recent News:')
st.text(st.secrets["RecentNews"])
st.divider()
st.subheader('About Me')
st.text('Hi im a youtuber who likes coding\nwe all have dreams\nand If you Subscribe\nyou would be helping\nme fulfil mine\nplease\n\/\/\/') 
st.link_button('Click Here Plz', 'https://www.youtube.com/@Join_The_Chicken_Empire/featured')
st.divider()
st.subheader('My Subscribers')
st.text("Ramona Time\nSmakshi Sarvaria\nTooklesoft\nSoshjackhe hello 120\nZxJoshua33\nAnun\nAmy Cartwright\nVineet Shrivastava\nBayu Trikurnia\nNoFace247\nSabina Ferk\nArcturus Ciel\nEduardo Díaz\nDavid Gilbert\nzian asher\nyvette metzger\nEster Nakale\nИбраһим 💪\nRidewithYamphel\nKAM22312\nsheuli bhowmik\nHanan Alwaqet\nTấn Hà Thị\nKing Nathan\nAIRWIND'S CHANNEL\nEster Lava\nTeremoana Eli\nEric Hernán Herazo Barrios\nvanina2229\nJudeVR\nLisa Pollack\nBrett Marchand")
st.divider()
st.subheader('History:')
st.text('June 23:\nChicken Empire Created\n\nJuly:\nChicken Empire faces war\n\n2024:\nYoutube channel starts\n\nMarch 2024 - April 2024:\nChannel thrives\n\nApril 24 - June 24:\nChannel views and subs drop of me going back to school\n\nJune 24:\nI create this website\n\n')
st.divider()
st.subheader('Wonderful portraits:')
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
st.text('Donnie(My other friend)\nZxJoshua33(You should go see his channel)\nOppositeAce8412(You should go see his channel)\nChickens\nEthan(My other friend)')
from vega_datasets import data

from utils import chart, db

COMMENT_TEMPLATE_MD = """{} - {}
> {}"""


def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


st.set_page_config(layout="centered", page_icon="💬", page_title="Commenting app")
st.title("💬 Commenting app")
source = data.stocks()
all_symbols = source.symbol.unique()
symbols = st.multiselect("Choose stocks to visualize", all_symbols, all_symbols[:3])
space(1)
source = source[source.symbol.isin(symbols)]
chart = chart.get_chart(source)
st.altair_chart(chart, use_container_width=True)
space(2)
conn = db.connect()
comments = db.collect(conn)
with st.expander("💬 Open comments"):
    st.write("**Comments:**")
    for index, entry in enumerate(comments.itertuples()):
        st.markdown(COMMENT_TEMPLATE_MD.format(entry.name, entry.date, entry.comment))

        is_last = index == len(comments) - 1
        is_new = "just_posted" in st.session_state and is_last
        if is_new:
            st.success("☝️ Your comment was successfully posted.")
    space(2)
    st.write("**Add your own comment:**")
    form = st.form("comment")
    name = form.text_input("Name")
    comment = form.text_area("Comment")
    submit = form.form_submit_button("Add comment")

    if submit:
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.insert(conn, [[name, comment, date]])
        if "just_posted" not in st.session_state:
            st.session_state["just_posted"] = True
        st.experimental_rerun()