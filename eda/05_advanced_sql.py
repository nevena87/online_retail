import pandas as pd
import mysql.connector
import os

# -------------------------
# 1. PATH SETUP
# -------------------------
project_path = r"C:\Users\Nevena\Radna površina\OnlineRetail_Project"
data_path = os.path.join(project_path, "data")
os.makedirs(data_path, exist_ok=True)

# -------------------------
# 2. DATABASE CONNECTION
# -------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="analitika",
    database="online_retail"
)

# Load data
df = pd.read_sql("SELECT * FROM online_retail", conn)

# Close connection (IMPORTANT)
conn.close()

print("✔ Data loaded:", df.shape)

# -------------------------
# 3. DATA PREP
# -------------------------
df['InvoiceDate_clean'] = pd.to_datetime(df['InvoiceDate_clean'], errors='coerce')

# Remove invalid rows (safety layer)
df = df.dropna(subset=['CustomerID', 'InvoiceDate_clean'])

# Ensure numeric safety
df['TotalPrice'] = pd.to_numeric(df['TotalPrice'], errors='coerce')

# -------------------------
# 4. CUSTOMER LIFETIME VALUE (CLV)
# -------------------------
clv = df.groupby('CustomerID').agg(
    TotalSpent=('TotalPrice', 'sum'),
    NumOrders=('InvoiceNo', 'nunique'),
    AvgOrderValue=('TotalPrice', 'mean')
).sort_values('TotalSpent', ascending=False)

print("\n🏆 Top 10 CLV Customers:")
print(clv.head(10))

clv.to_csv(os.path.join(data_path, "clv.csv"))

# -------------------------
# 5. RFM ANALYSIS (CORE BUSINESS METRIC)
# -------------------------
snapshot_date = df['InvoiceDate_clean'].max() + pd.Timedelta(days=1)

rfm = df.groupby('CustomerID').agg(
    Recency=('InvoiceDate_clean', lambda x: (snapshot_date - x.max()).days),
    Frequency=('InvoiceNo', 'nunique'),
    Monetary=('TotalPrice', 'sum')
).sort_values('Monetary', ascending=False)

print("\n📊 Top 10 RFM Customers:")
print(rfm.head(10))

rfm.to_csv(os.path.join(data_path, "rfm.csv"))

# -------------------------
# 6. ADVANCED METRICS
# -------------------------

# Rank customers by spending
df['CustomerRank'] = df.groupby('CustomerID')['TotalPrice'].transform('sum') \
    .rank(method='dense', ascending=False)

# Monthly sales trend + cumulative revenue
df['YearMonth'] = df['InvoiceDate_clean'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('YearMonth')['TotalPrice'].sum().sort_index()
monthly_cumsum = monthly_sales.cumsum()

monthly_cumsum.to_csv(os.path.join(data_path, "monthly_sales_cumsum.csv"))

# Average order value per invoice
invoice_avg = df.groupby(['CustomerID', 'InvoiceNo'])['TotalPrice'].sum().reset_index()
invoice_avg['AvgOrderValue'] = invoice_avg.groupby('CustomerID')['TotalPrice'].transform('mean')

invoice_avg.to_csv(os.path.join(data_path, "avg_order_per_customer.csv"))

print("\n✔ All analytics files saved successfully in /data")