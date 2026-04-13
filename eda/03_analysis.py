import pandas as pd
import os

# -----------------------------
# 1. PATH SETUP
# -----------------------------
project_path = r"C:\Users\Nevena\Radna površina\OnlineRetail_Project"
data_path = os.path.join(project_path, "data")
os.makedirs(data_path, exist_ok=True)

input_file = os.path.join(data_path, "online_retail_clean.csv")

# -----------------------------
# 2. LOAD DATA
# -----------------------------
df = pd.read_csv(input_file)

df['InvoiceDate_clean'] = pd.to_datetime(df['InvoiceDate_clean'], errors='coerce')

print("✔ Data loaded:", df.shape)

# -----------------------------
# 3. KPI 1 — TOP CUSTOMERS (VALUE + DIVERSITY)
# -----------------------------
customer_summary = df.groupby('CustomerID').agg(
    TotalSpending=('TotalPrice', 'sum'),
    UniqueProducts=('StockCode', 'nunique'),
    Transactions=('InvoiceNo', 'nunique')
).sort_values(by='TotalSpending', ascending=False)

print("\n🏆 Top 10 Customers:")
print(customer_summary.head(10))

# -----------------------------
# 4. KPI 2 — MONTHLY SALES TREND
# -----------------------------
df['YearMonth'] = df['InvoiceDate_clean'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('YearMonth')['TotalPrice'].sum().sort_index()

print("\n📊 Monthly Sales:")
print(monthly_sales)

# -----------------------------
# 5. KPI 3 — SALES BY COUNTRY
# -----------------------------
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)

print("\n🌍 Top 10 Countries by Revenue:")
print(country_sales.head(10))

# -----------------------------
# 6. KPI 4 — TOP PRODUCTS
# -----------------------------
top_products = df.groupby(['StockCode', 'Description'])['Quantity'].sum().sort_values(ascending=False)

print("\n🛍️ Top 10 Products:")
print(top_products.head(10))