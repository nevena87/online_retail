import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# 1. STYLE (professional look)
# -----------------------------
sns.set_theme(style="whitegrid")

# -----------------------------
# 2. PATH SETUP
# -----------------------------
project_path = r"C:\Users\Nevena\Radna površina\OnlineRetail_Project"
data_path = os.path.join(project_path, "data")

input_file = os.path.join(data_path, "online_retail_clean.csv")

# -----------------------------
# 3. LOAD DATA
# -----------------------------
df = pd.read_csv(input_file)

df['InvoiceDate_clean'] = pd.to_datetime(df['InvoiceDate_clean'], errors='coerce')

print("✔ Data loaded:", df.shape)

# =========================================================
# 📊 1. TOP CUSTOMERS
# =========================================================
customer_spending = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False)
top_customers = customer_spending.head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_customers.values, y=top_customers.index, palette="viridis")
plt.xlabel("Total Spending (£)")
plt.ylabel("Customer ID")
plt.title("Top 10 Customers by Revenue")
plt.tight_layout()
plt.show()

# =========================================================
# 📈 2. MONTHLY SALES TREND
# =========================================================
df['YearMonth'] = df['InvoiceDate_clean'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('YearMonth')['TotalPrice'].sum().sort_index()

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.title("Monthly Revenue Trend")
plt.tight_layout()
plt.show()

# =========================================================
# 🌍 3. SALES BY COUNTRY
# =========================================================
country_sales = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=country_sales.values, y=country_sales.index, palette="Blues_r")
plt.xlabel("Revenue (£)")
plt.ylabel("Country")
plt.title("Top 10 Countries by Revenue")
plt.tight_layout()
plt.show()