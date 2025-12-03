

import pandas as pd

# Step 1: Load your CSV file
df = pd.read_csv("Tricon7_dataset.csv")

# Step 2: Clean pt coloumn
# Converts all values in pt to strings.
# Removes commas (so "1,234" → "1234") and trims whitespace.
# Print the data to check if it loads correctly

df["pt"] = df["pt"].astype(str).str.replace(",", "", regex=False).str.strip()
df["pt"] = pd.to_numeric(df["pt"], errors="coerce")
df["pt"] = df["pt"].astype("Int64")


bad_rows = df[df["pt"].isna()]
if not bad_rows.empty:
    print("Rows that could not be converted to numbers:")
    print(bad_rows[["pt"]])

# Lists all rows where "pt" could not be converted to a number.
# Shows <NA> for missing/invalid values.

# Step 3: Verification:
print("\n=== pt column after conversion ===")
print(df["pt"].head())
print("dtype:", df["pt"].dtype)
print("All pt values are whole numbers:", (df["pt"] % 1 == 0).all())




# Step 4: analysis: 
# Shows the first few rows of all columns in your CSV after cleaning "pt".
# Useful to confirm that cleaning didn’t break other columns.

print("\nFirst few rows of the dataset:")
print(df.head())



# Prints all column names:
print("\nColumn names in dataset:")
print(df.columns.tolist())


# statistics
print("\n=== SUMMARY STATISTICS OF SELECTED COLOUMNS ===")
print(df[["pt", "ps", "differentiation", "Ang1"]].describe(include="all"))


# Basic info chcek
print("\n=== INFO ===")
df[["pt", "ps", "differentiation", "Ang1", "Ang2"]].info()
# total 5 columns, shows number fo rows
# Non-null counts for each column → helps find missing data


# count missing values:
# Tells you how many rows have <NA> or NaN.
# Useful for deciding whether you need to fill missing values or drop needing attention.
print("\n=== MISSING VALUES ===")
print(df[["pt", "ps", "differentiation", "Ang1"]].isnull().sum())


#  TASK 1: DATA TYPES & STRUCTURES: Create new DataFrame with only the required columns
df_selected = pd.DataFrame({
    "pt": df["pt"],
    "bmi": df["bmi"],
    "age_at_randomisation": df["age_at_randomisation"],
    "ps": df["ps"],
    "differentiation": df["differentiation"],
    "bevacizumab": df["bevacizumab"]
})

# Optional: preview the new DataFrame
print("\n=== Selected Columns DataFrame ===")
print(df_selected.head())


# Creating two seperate datasets by splitting:into clinical and biomarker data
df_clinical = df[["pt", "bmi", "age_at_randomisation", "ps", "differentiation", "bevacizumab"]].copy()
df_biomarkers = df[["pt", "Ang1", "Tie2", "Ang2", "VEGFR1", "VEGFR2", "ca125"]].copy()
print("\n=== Clinical Data ===")
print(df_clinical.head())
print("\n=== Biomarker Data ===")
print(df_biomarkers.head())# use 'outer' if you want all patients

# on="pt" ensures matching is done by patient ID. 
# how="inner" keeps only patients present in both datasets. You could use how="outer" if you want all patients, even if some biomarkers are missing.
# After merging, you can continue your analysis with df_merged instead of splitting them.
# Step 11: Merge clinical and biomarker datasets back together (if needed)
df_merged = pd.merge(df_clinical, df_biomarkers, on="pt", how="inner")  

print("\n=== Merged Dataset ===")
print(df_merged.head())

# Step 12: Check dataset info
print("\n=== Merged Dataset Info ===")
df_merged.info()








