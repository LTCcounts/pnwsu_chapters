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

st.write(
    """
  Last updated: 05 February 2026
    """
)

st.link_button("View static report", "pnwsu.org", icon="🌲", icon_position="left", disabled=False, width="content")

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

chapters = st.selectbox("Select your chapter",
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
            'UFCW 21 '],
             placeholder="None selected")


# Show a slider widget with the years using `st.slider`.
years = st.slider("Year", 2023, 2026, (2024, 2026))
months = st.slider("Month", 1, 12, (1, 12))
st.write(
    """
  Account balances for: 
    """
) 
print(chapters)

# Filter the dataframe based on the widget input and reshape it.
df_filtered = df[(df["Chapter"]==chapters]) & (df["Year"].between(years[0], years[1])) & (df["Month"].between(months[0], months[1]))]

#DF Reshape 0
df_reshaped0 = df_filtered.pivot_table(
    #index="Year", 
    columns=["Chapter","Year","Month","General Fund","Savings/Strike"],  
    fill_value=0
)
#df_reshaped0 = df_reshaped0.sort_values(by="Year", ascending=False)

st.dataframe(
    df_reshaped0,
    use_container_width=True,
    column_config={"Year": st.column_config.TextColumn("Year"),"Month": st.column_config.TextColumn("Month"), "General Fund": st.column_config.NumberColumn("General Fund ($)"), "Savings/Strike": st.column_config.NumberColumn("Savings/Strike ($)")},
)
