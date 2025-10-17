## aidé par chatgpt

import pandas as pd
import csv

# Load CSV
df = pd.read_csv(r'C:\Users\Mysmae\Desktop\College\S5-Autumn25\_ExplorationNouvellesTechnos\Projet2\steam_games.csv')

# GAME_TITLE delete rows that are empty or nan
df = df[df.iloc[:, 2].notna() & (df.iloc[:, 2].str.strip() != '')]

# PRICE Get rid of non numbers, format as float
df['price'] = df['price'].astype(str).str.strip()
df['price'] = df['price'].str.extract(r'\$ ?(\d+\.\d+)', expand=False)
df = df[df['price'].notna()]
df['price'] = df['price'].astype(float)

# TOTAL_REVIEWS Get rid of non numbers, format as integer
df['total_reviews'] = df['total_reviews'].astype(str).str.replace(r'\D+', '', regex=True)
df = df[df['total_reviews'] != '']
df['total_reviews'] = df['total_reviews'].astype(int)

# CLEAN: Remove line breaks, tabs, and excessive spaces from all text columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype(str)\
    .str.replace(r'[\n\r\t]+', ' ', regex=True)\
    .str.replace(r'\s+', ' ', regex=True)\
    .str.strip()

# Extended rows for each developper
df['developper'] = df['developper'].str.split(',')
df = df.explode('developper')
df['developper'] = df['developper'].str.strip()

# DROP unwanted columns
df = df.drop(columns=['web-scraper-order', 'web-scraper-start-url', 'link'], errors='ignore')

# SAVE the final cleaned DataFrame as CSV with semicolon delimiter and all fields quoted
df.to_csv(
    r'C:\Users\Mysmae\Desktop\College\S5-Autumn25\_ExplorationNouvellesTechnos\Projet2\steam_games_expanded.csv',
    sep=';',                    # Use semicolon as field separator
    index=False,
    quoting=csv.QUOTE_ALL,      # Quote all fields
    quotechar='"',
    escapechar='\\'
)

print("Conversion completed.")
