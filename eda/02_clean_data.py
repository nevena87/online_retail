import os
import pandas as pd

# -----------------------------
# 1. PATH SETUP
# -----------------------------
project_path = r"C:\Users\Nevena\Radna površina\OnlineRetail_Project"
data_path = os.path.join(project_path, "data")

os.makedirs(data_path, exist_ok=True)

input_file = os.path.join(data_path, "online_retail_clean_extract.csv")
output_file = os.path.join(data_path, "online_retail_clean.csv")

# -----------------------------
# 2. LOAD DATA
# -----------------------------
df = pd.read_csv(input_file)

print("✔ Data loaded:", df.shape)

# -----------------------------
# 3. DATA CLEANING
# -----------------------------

# Remove duplicates
df = df.drop_duplicates()

# Convert numeric columns safely
df['CustomerID'] = pd.to_numeric(df['CustomerID'], errors='coerce').astype('Int64')
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# Convert datetime safely
df['InvoiceDate_clean'] = pd.to_datetime(df['InvoiceDate_clean'], errors='coerce')

# Remove invalid rows (core business logic)
df = df[
    (df['Quantity'] > 0) &
    (df['UnitPrice'] > 0)
]

# Remove rows without customer (optional but common in analytics)
df = df.dropna(subset=['CustomerID'])

# -----------------------------
# 4. FEATURE ENGINEERING
# -----------------------------

df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

# Optional: time features (useful for SQL/Python analysis)
df['Year'] = df['InvoiceDate_clean'].dt.year
df['Month'] = df['InvoiceDate_clean'].dt.to_period('M').astype(str)

# -----------------------------
# 5. QUALITY CHECK
# -----------------------------
print("\n✔ Final Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# -----------------------------
# 6. SAVE CLEAN DATA
# -----------------------------
df.to_csv(output_file, index=False)

print(f"\n✔ Clean dataset saved at: {output_file}")