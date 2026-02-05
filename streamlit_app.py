import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Chapters", page_icon="📈")
st.title("📈 Chapters")
st.image("data/Basic_Logo.png")
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
#months = st.slider("Month", 1, 12, (1, 12))
months = st.multiselect(
    "Month",
    df.Month.unique(),
    ['Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'June',
    'July',
    'Aug',
    'Sept',
    'Oct',
    'Nov',
    'Dec'
    ],
    )

# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df["Chapter"].isin(chapters)) & (df["Year"].between(years[0], years[1])) & (df["Month"].isin(months)) ]
#DF Reshape 1
df_reshaped = df_filtered.pivot_table(
    index="Year", columns=["Chapter","Month"], values=["General Fund"], aggfunc="sum", fill_value=0
)
df_reshaped = df_reshaped.sort_values(by="Year", ascending=False)
#DF reshape 2
df_reshaped2 = df_filtered.pivot_table(
    index="Year", columns=["Chapter","Month"], values=["Savings/Strike"], aggfunc="sum", fill_value=0
)
df_reshaped2 = df_reshaped2.sort_values(by="Year", ascending=False)

# Display the data as a table using `st.dataframe`.
colz1, colz2 = st.columns(2)

with colz1:
    st.dataframe(
        df_reshaped,
        use_container_width=True,
        column_config={"Year": st.column_config.TextColumn("Year"), "General Fund": st.column_config.NumberColumn("General Fund ($)")},
)
with colz2:
    st.dataframe(
        df_reshaped2,
        use_container_width=True,
        column_config={"Year": st.column_config.TextColumn("Year"), "Savings/Strike": st.column_config.NumberColumn("Savings/Strike ($)")},
    )

#Columns: Year,Month,Date,Chapter,General Fund,Savings/Strike
# Display the data as an Altair chart using `st.altair_chart`.
