import altair as alt
import pandas as pd
import streamlit as st
import math
from pathlib import Path
import webbrowser

def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.    
        video_file = open("data/pnwsu_mov.mp4", "rb")
        video_bytes = video_file.read()
        st.video(video_bytes, loop=True, autoplay=True)
        st.text_input("Welcome. Please input password to proceed:", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Password incorrect, show input + error.
        st.text_input("Password", type="password", on_change=password_entered, key="password")
        st.error("Incorrect password. Please try again.")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.caption("Password accepted.")
    colz1, colz2, colz3 = st.columns(3)

    with colz1:
        st.link_button("PNWSU website","https://pnwsu.org")

    with colz2:
        st.link_button("At-Large C&B and CBAs","https://pnwsu.org/resources/")
        
    with colz3:
        st.link_button("Online store","https://pnwsu.myshopify.com/")
            

