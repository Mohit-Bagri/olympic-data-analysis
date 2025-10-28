import streamlit as st
import pandas as pd

import preproccesor,helper


df = preproccesor.preprocess()
st.sidebar.title("Olympics Analysis")
user_select  = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis', 'Country-wise Analysis', 'Athelete-wise Analysis')
)


if user_select == 'Medal Tally':
    st.sidebar.header("Medal Tally")

    years,country= helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country",country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)

    if(selected_country == "Overall" and selected_year == "Overall"):
        st.title("Overall Tally")
    elif (selected_country != "Overall" and selected_year == "Overall"):
        st.title("Overall Performance of " + selected_country)
    elif (selected_country == "Overall" and selected_year != "Overall"):
        st.title("Overall Medal Tally in " + str(selected_year) + " Olympics")
    else: #(selected_country != "Overall" and selected_year != "Overall"):
        st.title(selected_country + " Performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

