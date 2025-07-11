import pandas as pd
import sqlite3

# -------------------------------
# Part 1: Reading Files
# -------------------------------

conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
print("Part 1.1 - First 10 rows from customers table:")
print(customers_df.head(10))
conn.close()

iris_df = pd.read_json("iris.json")
print("\nPart 1.2 - Shape and Columns of iris.json:")
print("Shape:", iris_df.shape)
print("Columns:", iris_df.columns.tolist())

titanic_df = pd.read_excel("titanic.xlsx")
print("\nPart 1.3 - First 5 rows of titanic.xlsx:")
print(titanic_df.head())

flights_df = pd.read_parquet("flights.parquet")
print("\nPart 1.4 - Info of flights parquet:")
print(flights_df.info())

movie_df = pd.read_csv("movie.csv")
print("\nPart 1.5 - Random sample from movie.csv:")
print(movie_df.sample(10))

# -------------------------------
# Part 2: Exploring DataFrames
# -------------------------------

iris_df.columns = [col.lower() for col in iris_df.columns]
iris_selected = iris_df[['sepal_length', 'sepal_width']]
print("\nPart 2.1 - Selected columns from iris.json:")
print(iris_selected.head())

titanic_filtered = titanic_df[titanic_df['Age'] > 30]
print("\nPart 2.2 - Passengers with age > 30:")
print(titanic_filtered.head())

print("\nPart 2.2 - Gender count:")
print(titanic_df['Sex'].value_counts())

flights_selected = flights_df[['origin', 'dest', 'carrier']]
print("\nPart 2.3 - Selected columns from flights:")
print(flights_selected.head())

print("\nPart 2.3 - Unique destinations:", flights_df['dest'].nunique())

long_movies = movie_df[movie_df['duration'] > 120]
sorted_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print("\nPart 2.4 - Long movies sorted by director likes:")
print(sorted_movies[['director_name', 'duration', 'director_facebook_likes']].head())

# -------------------------------
# Part 3: Challenges and Explorations
# -------------------------------

print("\nPart 3.1 - iris statistics:")
print("Mean:\n", iris_df.mean(numeric_only=True))
print("Median:\n", iris_df.median(numeric_only=True))
print("Std:\n", iris_df.std(numeric_only=True))

print("\nPart 3.2 - Titanic Age Stats:")
print("Min age:", titanic_df['Age'].min())
print("Max age:", titanic_df['Age'].max())
print("Sum of ages:", titanic_df['Age'].sum())

director_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum()
top_director = director_likes.idxmax()
top_likes = director_likes.max()
print("\nPart 3.3 - Top director by total Facebook likes:")
print(f"{top_director} with {top_likes} likes")

longest_movies = movie_df.nlargest(5, 'duration')[['movie_title', 'director_name', 'duration']]
print("\nPart 3.3 - Top 5 longest movies:")
print(longest_movies)

print("\nPart 3.4 - Missing values in flights dataset:")
print(flights_df.isnull().sum())

numeric_cols = flights_df.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    flights_df[col].fillna(flights_df[col].mean(), inplace=True)
print("\nMissing values filled with mean in numeric columns.")
