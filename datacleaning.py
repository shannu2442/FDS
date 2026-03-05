import pandas as pd

# -----------------------------------------
# Step 1: Read data from an Excel file
# -----------------------------------------
# Explicitly specify a sheet name if needed
df = pd.read_excel("employees.xlsx")
print("Original Data:")
print(df.head())

# -----------------------------------------
# Step 2: Basic Data Cleaning
# -----------------------------------------
# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values (example: fill missing salaries with mean)
if "salary" in df.columns:
    df["salary"] = df["salary"].fillna(df["salary"].mean())

# Strip whitespace from string columns
str_cols = df.select_dtypes(include=["object"]).columns
df[str_cols] = df[str_cols].apply(lambda col: col.str.strip())

# Drop rows where all values are missing
df = df.dropna(how="all")

print("\nCleaned Data:")
print(df.head())

# -----------------------------------------
# Step 3: Save cleaned data to HDF5 format
# -----------------------------------------
# Ensure PyTables is installed: pip install tables
df.to_hdf("cleaned_data.h5", key="employees", mode="w")

print("\nCleaned data saved to cleaned_data.h5")

# Read the HDF5 file
df_hdf = pd.read_hdf("cleaned_data.h5", key="employees")

# Display data from HDF5 File
print(df_hdf)