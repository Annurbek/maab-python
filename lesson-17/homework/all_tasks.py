import pandas as pd
import sqlite3

# -------------------------------
# Merging and Joining
# -------------------------------

conn = sqlite3.connect("chinook.db")
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
conn.close()

inner_merged = pd.merge(customers, invoices, on="CustomerId", how="inner")
invoice_counts = inner_merged.groupby('CustomerId').size().reset_index(name='TotalInvoices')

movie_df = pd.read_csv("movie.csv")
df1 = movie_df[['director_name', 'color']].drop_duplicates()
df2 = movie_df[['director_name', 'num_critic_for_reviews']].drop_duplicates()

left_join = pd.merge(df1, df2, on='director_name', how='left')
outer_join = pd.merge(df1, df2, on='director_name', how='outer')

left_join_count = len(left_join)
outer_join_count = len(outer_join)

# -------------------------------
# Grouping and Aggregating
# -------------------------------

titanic = pd.read_excel("titanic.xlsx")
grouped_titanic = titanic.groupby('Pclass').agg({
    'Age': 'mean',
    'Fare': 'sum',
    'PassengerId': 'count'
}).rename(columns={'PassengerId': 'PassengerCount'}).reset_index()

grouped_movies = movie_df.groupby(['color', 'director_name']).agg({
    'num_critic_for_reviews': 'sum',
    'duration': 'mean'
}).reset_index()

flights = pd.read_parquet("flights.parquet")
nested_group = flights.groupby(['Year', 'Month']).agg({
    'FlightNum': 'count',
    'ArrDelay': 'mean',
    'DepDelay': 'max'
}).reset_index().rename(columns={'FlightNum': 'TotalFlights'})

# -------------------------------
# Applying Functions
# -------------------------------

def classify_age(age):
    return 'Child' if age < 18 else 'Adult'

titanic['Age_Group'] = titanic['Age'].apply(classify_age)

employee = pd.read_csv("employee.csv")
employee['NormalizedSalary'] = employee.groupby('Department')['Salary'].transform(
    lambda x: (x - x.mean()) / x.std())

def movie_length_class(duration):
    if duration < 60:
        return 'Short'
    elif duration <= 120:
        return 'Medium'
    else:
        return 'Long'

movie_df['Length_Class'] = movie_df['duration'].apply(movie_length_class)

# -------------------------------
# Using pipe
# -------------------------------

def filter_survived(df):
    return df[df['Survived'] == 1]

def fill_age(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df

def add_fare_per_age(df):
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

titanic_pipe = (titanic
    .pipe(filter_survived)
    .pipe(fill_age)
    .pipe(add_fare_per_age))

def filter_delayed(df):
    return df[df['DepDelay'] > 30]

def add_delay_per_hour(df):
    df['Delay_Per_Hour'] = df['DepDelay'] / df['AirTime']
    return df

flights_pipe = (flights
    .pipe(filter_delayed)
    .pipe(add_delay_per_hour))
