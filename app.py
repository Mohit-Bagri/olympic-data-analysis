from multiprocessing.resource_tracker import register

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import  seaborn as sns
import plotly.figure_factory as ff
from pandas import pivot_table
from plotly.figure_factory import create_distplot

import preproccesor,helper
from helper import data_over_time, year_wise_medal_tally


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


if user_select == 'Overall Analysis':
    editions = df["Year"].unique().shape[0] -1
    cities = df["City"].unique().shape[0]
    sports = df["Sport"].unique().shape[0]
    events = df["Event"].unique().shape[0]
    athletes = df["Name"].unique().shape[0]
    region =df["region"].unique().shape[0]

    st.title("Top Stats")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Cities")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Event")
        st.title(events)
    with col2:
        st.header("Athletes")
        st.title(athletes)
    with col3:
        st.header("Region")
        st.title(region)

    participating_nations_over_time = helper.data_over_time(df, "region")
    st.title("Participating Nations Over Time")
    fig = px.line(participating_nations_over_time, x="Year", y="count", labels={"Year": "Olympic Year", "count": "Number of Countries"})
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, "Event")
    st.title("Events Over Time")
    fig = px.line(events_over_time, x="Year", y="count",
                  labels={"Year": "Olympic Year", "count": "Number of Events"})
    st.plotly_chart(fig)

    athletes_over_time = helper.data_over_time(df, "Name")
    st.title("Athletes Over Time")
    fig = px.line(athletes_over_time, x="Year", y="count",
                  labels={"Year": "Olympic Year", "count": "Number of Athletes"})
    st.plotly_chart(fig)


    st.title("No. of Events in Every Sport over Time")
    x = helper.heatmap(df)
    fig, ax = plt.subplots(figsize = (10,10))
    ax= sns.heatmap(x.pivot_table(index = "Sport" , columns="Year", values="Event", aggfunc = "count").fillna(0).astype("int"), annot=True)
    st.pyplot(fig)

    st.title("Most Successful Athletes")
    sport_list = df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, "Overall")
    user_select_sport = st.selectbox("Select Sport",sport_list)
    x = helper.most_successful(df, user_select_sport)
    st.table(x)


if user_select == 'Country-wise Analysis':
    st.sidebar.title("Country wise Analysis")

    country_list = df["region"].dropna().unique().tolist()
    country_list.sort()
    user_select_country = st.sidebar.selectbox("Select Country",country_list)

    country_df = helper.year_wise_medal_tally(df, user_select_country)
    st.title(user_select_country + " Medal Tally over the Years")
    fig = px.line(country_df, x="Year", y="Medal")
    st.plotly_chart(fig)

    st.title("Sport-wise Medal Tally of " + user_select_country)
    heat_df = helper.heatmap_country_sports(df, user_select_country)
    fig, ax = plt.subplots(figsize=(10, 10))
    ax = sns.heatmap(heat_df.pivot_table(index="Sport", columns="Year", values="Event", aggfunc="count").fillna(0),annot=True)
    st.pyplot(fig)

    st.title("Top 10 Athletes of " + user_select_country)
    top10_df = helper.most_successful_country_wise(df, user_select_country)
    st.table(top10_df)


if user_select == 'Athelete-wise Analysis':
    athlete_df = df.dropna(subset=["Name","region"])

    x1 = athlete_df["Age"].dropna()
    x2 = athlete_df[athlete_df["Medal"] == "Gold"]["Age"].dropna()
    x3 = athlete_df[athlete_df["Medal"] == "Silver"]["Age"].dropna()
    x4 = athlete_df[athlete_df["Medal"] == "Bronze"]["Age"].dropna()
    fig = create_distplot([x1,x2,x3,x4], ["Overall Age", 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'], show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df, selected_sport)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(data=temp_df, x='Weight', y='Height', hue='Medal', style='Sex', s=60)
    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)
