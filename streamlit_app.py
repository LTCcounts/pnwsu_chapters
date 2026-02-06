import altair as alt
import pandas as pd
import streamlit as st

st.image("data/Picture1.png")
df = pd.read_csv("data/chapter_bal.csv")
df = df[["Chapter","Year","Date","General Fund","Savings/Strike"]]

df_filtered = df[(df["Chapter"]=="PROTEC17")]
#chart_df["Year"] = chart_df.index
st.line_chart(df_filtered, x="Date", y=["General Fund"])





