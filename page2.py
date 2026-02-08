import altair as alt
import pandas as pd
import streamlit as st
# Show the page title and description.
st.set_page_config(page_title="PNWSU Resources")
st.title("PNWSU Resources")
st.write("Find other PNWSU content below")
colz1, colz2, colz3 = st.columns(3)

with colz1:
  st.link_button("PNWSU website","https://pnwsu.org")

with colz2:
  st.link_button("At-Large C&B and CBAs","https://pnwsu.org/resources/")
    
with colz3:
  st.link_button("Online store","https://pnwsu.myshopify.com/")
        