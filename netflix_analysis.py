import pandas as pd

df = pd.read_csv("netflix_titles.csv")

# Clean missing countries
df["country"] = df["country"].fillna("Unknown")


# Top countries
top_countries = (
    df["country"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_countries.columns = ["country", "title_count"]

top_countries.to_csv("Top_10_countries.csv", index=False)


# Top genres
top_genres = (
    df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
    .reset_index()
)

top_genres.columns = ["genre", "count"]

top_genres.to_csv("Top_10_genres.csv", index=False)