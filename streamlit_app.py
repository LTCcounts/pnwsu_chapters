import altair as alt
import pandas as pd
import streamlit as st

# Common widgets that persist across all pages
user_name = st.sidebar.text_input("Password", key="password")
user_role = st.sidebar.selectbox("Chapter", ["BSSU", "PROTEC17"], key="chapter")

# Navigation
page = st.navigation([
    st.Page("page1.py", title="Dashboard"),
    #st.Page("page2.py", title="Settings"),
])
page.run()


