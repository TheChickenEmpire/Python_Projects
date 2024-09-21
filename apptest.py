import plotly.express as px
import pandas as pd
import streamlit as st
import shelve

from streamlit_plotly_events import plotly_events

DB_FILE = "db.shelve"

if "comments" not in st.session_state:
    with shelve.open(DB_FILE) as db:
        if "comments" in db:
            st.session_state.comments = db["comments"]
        else:
            st.session_state.comments = {}

if "selected_point" not in st.session_state:
    st.session_state.selected_point = None


def point_to_key(point: dict[str, int]) -> str:
    return f"{point['x']}_{point['y']}"


def key_to_xy(key: str) -> tuple[int, int]:
    return tuple([int(a) for a in key.split("_")])


points = pd.DataFrame({"x": [1, 2, 3, 4, 5, 6], "y": [1, 4, 9, 16, 25, 36]})
points["has_comment"] = False

for key, comment in st.session_state.comments.items():
    x, y = key_to_xy(key)
    points.loc[(points["x"] == x) & (points["y"] == y), "has_comment"] = True


fig = px.scatter(
    points,
    x="x",
    y="y",
    color="has_comment",
    color_discrete_map={True: "red", False: "blue"},
)
selected_points = plotly_events(fig)

if selected_points:
    st.session_state.selected_point = point_to_key(selected_points[0])

if not st.session_state.selected_point:
    st.stop()


def submit_comments(key: str):
    if key not in st.session_state.comments:
        st.session_state.comments[key] = []
    st.session_state.comments[key].append(st.session_state["new_comment"])
    with shelve.open(DB_FILE) as db:
        db["comments"] = st.session_state.comments


key = st.session_state.selected_point
if key in st.session_state.comments:
    x, y = key_to_xy(key)
    st.write(f"Comments: on point ({x}, {y}):")
    for comment in st.session_state.comments[key]:
        st.write(f"* {comment}")

with st.form("comments"):
    x, y = key_to_xy(key)
    st.text_input(
        f"What would you like to say about this point ({x}, {y})", key="new_comment"
    )
    st.form_submit_button("Submit", on_click=submit_comments, args=(key,))