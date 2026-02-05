import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Chapters", page_icon="📈")
st.title("📈 Chapters")
st.write(
    """
  Dynamic information on chapter account balances over time, intended to give chapters a sense of dues remittance dynamics and chapter resource growth and availability.  
    """
)

#Columns: Year,Month,Date,Chapter,General Fund,Savings/Strike
# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/chapter_bal.csv")
    return df


df = load_data()
#Columns: Year,Month,Date,Chapter,General Fund,Savings/Strike
# Show a multiselect widget with the genres using `st.multiselect`.
chapters = st.multiselect(
    "Chapter",
    df.Chapter.unique(),
    ['WORKING WA',
'BSSU',
'LA LABOR FED',
'PROTEC17',
'SEIU 925 ',
'SEIU 2015 ',
'SEIU 221 ',
'UFCW 3000',
'MEAWU',
'NVLF',
'UDWU',
'UFCW367',
'KIWA',
'SEIU 121RN ',
'UFCW 21 '
],
)

# Show a slider widget with the years using `st.slider`.
years = st.slider("Year", 2023, 2025, (2024, 2025))
months = st.slider("Month", 1, 12, (1, 12))

# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df["Chapter"].isin(chapters)) & (df["Year"].between(years[0], years[1])) & (df["Month"].between(months[0], months[1]))]
df_reshaped = df_filtered.pivot_table(
    index="Year", columns="Chapter", values=["General Fund","Savings/Strike"], aggfunc="sum", fill_value=0
)
df_reshaped = df_reshaped.sort_values(by="Year", ascending=False)

#Columns: Year,Month,Date,Chapter,General Fund,Savings/Strike
# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"Year": st.column_config.TextColumn("Year")},
)
#Columns: Year,Month,Date,Chapter,General Fund,Savings/Strike
# Display the data as an Altair chart using `st.altair_chart`.
df_chart = pd.melt(
    df_reshaped.reset_index(), id_vars="Year", var_name="Chapter", value_name="gross"
)
st.bar_chart(
    df,
    x="Year",
    y=["General Fund", "Savings/Strike"],
    color=["#00ff00", "#339933"]
)