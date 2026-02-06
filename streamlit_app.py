import altair as alt
import pandas as pd
import streamlit as st

st.image("data/Picture1.png")
df = pd.read_csv("data/chapter_bal.csv")
df = df[["Chapter","Year","General Fund","Savings/Strike"]]
chart_df = df.groupby(["Year"])
#chart_df["Year"] = chart_df.index
st.line_chart(chart_df, x="Year", y=["General Fund"])
st.line_chart(chart_df, x="Year", y=["Savings/Strike"])




