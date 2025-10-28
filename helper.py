# def medal_tally(df):
#     medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
#     medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by=['Gold'], ascending=False).reset_index()
#     medal_tally["Total"] = medal_tally["Gold"] + medal_tally["Bronze"] + medal_tally["Silver"]
#     medal_tally["Gold"] = medal_tally["Gold"].astype(int)
#     medal_tally["Silver"]=medal_tally["Silver"].astype(int)
#     medal_tally["Bronze"] =medal_tally["Bronze"].astype(int)
#     medal_tally["Total"] = medal_tally["Total"].astype(int)
#
#     return medal_tally
#

def country_year_list(df):
    years = df["Year"].unique().tolist()
    years.sort()
    years.insert(0,"Overall")

    country = df["region"].dropna().unique().tolist()
    country.sort()
    country.insert(0,"Overall")

    return years, country



def fetch_medal_tally(df,year,country):
    medal_df = df.drop_duplicates(
        subset=['Team', 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal'])
    flag =0
    if year == "Overall" and country =="Overall":
        temp_df = medal_df
    elif year =="Overall" and country != "Overall":
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    elif year !="Overall" and country =="Overall":
        temp_df = medal_df[medal_df['Year'] == year]
    else: #year != "Overall" and country != "Overall"
        temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]

    if flag ==1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by=['Gold'],ascending=False).reset_index()
    if flag ==0:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values(by=['Gold'],ascending=False).reset_index()

    x["Total"] = x["Gold"] + x["Bronze"] + x["Silver"]
    x["Gold"] = x["Gold"].astype(int)
    x["Silver"] = x["Silver"].astype(int)
    x["Bronze"] = x["Bronze"].astype(int)
    x["Total"] = x["Total"].astype(int)

    return x
