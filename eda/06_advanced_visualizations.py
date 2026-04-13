import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------
# STYLE (PROFESSIONAL LOOK)
# -------------------------
sns.set_theme(style="whitegrid")

# -------------------------
# PATH SETUP
# -------------------------
project_path = r"C:\Users\Nevena\Radna površina\OnlineRetail_Project"
data_path = os.path.join(project_path, "data")

print("✔ Loading data from:", data_path)

# =====================================================
# 1. CLV VISUALIZATION
# =====================================================
clv = pd.read_csv(os.path.join(data_path, "clv.csv"))

top10_clv = clv.head(10).copy()

plt.figure(figsize=(10, 6))
sns.barplot(
    x=top10_clv["CustomerID"].astype(str),
    y=top10_clv["TotalSpent"],
    palette="viridis"
)
plt.xticks(rotation=45)
plt.title("Top 10 Customers by CLV (Total Spending)")
plt.xlabel("Customer ID")
plt.ylabel("Total Spent (£)")
plt.tight_layout()
plt.show()

# =====================================================
# 2. RFM DISTRIBUTION
# =====================================================
rfm = pd.read_csv(os.path.join(data_path, "rfm.csv"))

plt.figure(figsize=(10, 6))
sns.histplot(rfm["Monetary"], bins=50, kde=True)
plt.title("Customer Monetary Value Distribution (RFM)")
plt.xlabel("Total Spending")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# =====================================================
# 3. CUMULATIVE REVENUE TREND
# =====================================================
monthly_cumsum = pd.read_csv(
    os.path.join(data_path, "monthly_sales_cumsum.csv"),
    index_col=0
)

plt.figure(figsize=(12, 6))
plt.plot(monthly_cumsum.index, monthly_cumsum.values, marker='o')
plt.xticks(rotation=45)
plt.title("Cumulative Monthly Revenue Trend")
plt.xlabel("Year-Month")
plt.ylabel("Cumulative Revenue (£)")
plt.tight_layout()
plt.show()

# =====================================================
# 4. AVERAGE ORDER VALUE DISTRIBUTION
# =====================================================
avg_orders = pd.read_csv(os.path.join(data_path, "avg_order_per_customer.csv"))

plt.figure(figsize=(10, 6))
sns.histplot(avg_orders["AvgOrderValue"], bins=50, kde=True)
plt.title("Average Order Value per Customer")
plt.xlabel("Average Order Value (£)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("\n✔ All visualizations completed successfully")