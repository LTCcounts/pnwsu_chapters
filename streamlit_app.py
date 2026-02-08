import altair as alt
import pandas as pd
import streamlit as st

st.image("data/skyline5.png")

pages = {
    "Your account": [
        st.Page("page1.py", title="Please input password")
    ],
    "Resources": [
        st.Page("page2.py", title="PNWSU Resources")]
}

pg = st.navigation(pages)
pg.run()


