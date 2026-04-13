import pandas as pd
import mysql.connector
import os

# -----------------------------
# 1. MYSQL CONNECTION
# -----------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="analitika",
    database="online_retail"
)

# -----------------------------
# 2. EXTRACT DATA (filtered)
# -----------------------------
query = """
SELECT *
FROM online_retail
WHERE Quantity > 0
  AND UnitPrice > 0
"""

df = pd.read_sql(query, conn)

# -----------------------------
# 3. BASIC DATA CHECKS
# -----------------------------
print("✔ Data loaded successfully")
print("Shape:", df.shape)
print("\nColumns:", df.columns)
print("\nFirst 5 rows:\n", df.head())
print("\nInfo:")
print(df.info())

# -----------------------------
# 4. CREATE PROJECT FOLDER
# -----------------------------
project_path = r"C:\Users\Nevena\Radna površina\OnlineRetail_Project"
data_path = os.path.join(project_path, "data")
os.makedirs(data_path, exist_ok=True)

# -----------------------------
# 5. EXPORT CLEAN DATA
# -----------------------------
output_file = os.path.join(data_path, "online_retail_clean_extract.csv")
df.to_csv(output_file, index=False)

print(f"\n✔ File saved at: {output_file}")

# -----------------------------
# 6. CLOSE CONNECTION
# -----------------------------
conn.close()
print("✔ Database connection closed")