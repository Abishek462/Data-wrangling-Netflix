import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

# Fill missing values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('0')


# Fix date column (IMPORTANT FIX)
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')

# Feature engineering
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

# Clean duration
df['duration'] = df['duration'].str.replace(' min', '', regex=False)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_netflix_data.csv", index=False)

print("Cleaning Done Successfully")