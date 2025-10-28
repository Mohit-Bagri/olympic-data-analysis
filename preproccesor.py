import pandas as pd



def preprocess():
    df = pd.read_csv("athlete_events.csv")
    regions_df = pd.read_csv("noc_regions.csv")

    df = df[df["Season"]=="Summer"]
    df = df.merge(regions_df, on="NOC", how="left")
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)

    return df