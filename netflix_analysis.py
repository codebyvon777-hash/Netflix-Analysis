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


# Count movies and TV shows by release year
content_by_year = (
    df.groupby(["release_year", "type"])
    .size()
    .reset_index(name="count")
)

print(content_by_year.head())

# Export for Tableau
content_by_year.to_csv("data/content_by_year.csv", index=False)


# Count titles by rating
ratings = (
    df["rating"]
    .fillna("Unknown")
    .value_counts()
    .reset_index()
)

ratings.columns = ["rating", "count"]

print(ratings.head())

# Export for Tableau
ratings.to_csv("data/ratings.csv", index=False)
