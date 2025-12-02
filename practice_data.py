

import pandas as pd

# Load your CSV file
df = pd.read_csv("Tricon7_dataset.csv")

# Print the data to check if it loads correctly
print(df)


# Profilling the data: want: pt, ps, differentiation, Ang1




# statistics
print("\n=== SUMMARY STATISTICS ===")
print(df[["pt", "ps", "differentiation", "Ang1"]].describe(include="all"))


# Basic info chcek
print("\n=== INFO ===")
df[["pt", "ps", "differentiation", "Ang1", "Ang2"]].info()


# count missing values:
print("\n=== MISSING VALUES ===")
print(df[["pt", "ps", "differentiation", "Ang1"]].isnull().sum())