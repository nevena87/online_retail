# 🛍️ E-commerce Customer Analytics Project
## 🎯 Objective

This project simulates a real-world e-commerce analytics system designed to support business decision-making in customer retention, revenue optimization, and marketing strategy.

Using transactional retail data, the goal was to transform raw data into actionable insights through SQL analysis, Python data processing, and Power BI visualization.

---

## 📌 Project Overview

This project analyzes an e-commerce dataset to extract business insights about:

Customer behavior
Revenue trends
Customer segmentation
Customer Lifetime Value (CLV)
At-risk customers

The goal was to simulate a real-world Data Analyst workflow from raw data to interactive business dashboard.

---
## 🛠️ Tech Stack
SQL (MySQL)
Python 3.12
pandas
numpy
matplotlib
seaborn
Power BI Desktop

--- 

## 📂 Project Structure

```bash

OnlineRetail_Project/
│
├── data/
│   ├── online_retail_clean.csv
│   ├── online_retail_full.csv
│   ├── clv.csv
│   ├── rfm.csv
│   ├── rfm_scored.csv
│   ├── rfm_segmented.csv
│   ├── monthly_sales_cumsum.csv
│   ├── avg_order_per_customer.csv
│
├── sql/
│   ├── queries.sql
│   ├── sql analysis.sql
│
├── eda/
│   ├── 01_load_data.py
│   ├── 02_clean_data.py
│   ├── 03_analysis.py
│   ├── 04_visualizations.py
│   ├── 05_advanced_sql.py
│   ├── 06_advanced_visualizations.py
│   ├── 07_rfm_scoring.py
│   ├── 08_rfm_segmentation.py
│
├── requirements.txt
├── venv/
└── Online Retail.pbix

```
---

## 🔎 Phase 1 – SQL Analysis

The dataset was first imported into a MySQL database and explored using SQL queries.

Key operations included:
- Data import and schema design
- Aggregations and grouping
- Customer-level analysis
- Revenue breakdown by country and product
- Window functions for ranking and cumulative metrics

Key metrics calculated:
- Total Revenue
- Number of Customers
- Average Order Value
- Monthly Sales Trends
- Customer Ranking

---

## 🐍 Phase 2 – Python Data Cleaning & EDA

Data was extracted from MySQL and processed using Python.

Steps performed:
- Handling missing values
- Removing duplicates
- Date formatting and transformation
- Feature engineering (TotalPrice)
- Exploratory Data Analysis

Outputs were saved as structured CSV files for further BI usage.

---

## 📊 Phase 3 – Advanced Analytics

### 💰 Customer Lifetime Value (CLV)

CLV analysis was used to identify the most valuable customers based on:
- Total spending
- Number of orders
- Average order value

This helps in identifying high-value customer segments.

### 👥 RFM Analysis

Customers were segmented using the RFM model:
- Recency – Days since last purchase
- Frequency – Number of purchases
- Monetary – Total spending
- RFM Scoring (Quartiles 1–4)

Each customer was scored based on percentile distribution:
- Recency (lower is better)
- Frequency (higher is better)
- Monetary (higher is better)

### 🧠 Customer Segmentation

Based on RFM scores, customers were grouped into:
- 🏆 Champions
- 💎 Loyal Customers
- 🌱 Potential Loyalists
- ⚠️ At Risk Customers
- ❌ Lost Customers

---

## 📈 Power BI Dashboard

An interactive Power BI dashboard was built to visualize key insights.

- KPI Cards
- Total Customers
- Total Revenue
- Average Revenue per Customer
- Visualizations
- Revenue by Customer Segment
- Customer Distribution by Segment
- Cumulative Revenue Trend
- Top 10 Customers
- Interactive Filters (Slicers)

---

## 💡 Key Business Insights
- A small percentage of customers generates the majority of revenue (Pareto principle).
- Champions and Loyal Customers contribute the highest revenue share.
- At Risk customers represent a key opportunity for retention strategies.
- Revenue shows consistent cumulative growth over time.
- Customer behavior varies significantly across segments.

---

## 🎯 Skills Demonstrated

This project demonstrates:
- End-to-end data pipeline development
- SQL data analysis and aggregation
- Python data cleaning and transformation
- Business-oriented KPI development
- Customer segmentation (RFM model)
- Customer Lifetime Value analysis
- Data visualization and storytelling
- Power BI dashboard development

---

## 🚀 How to Run
### SQL
Import dataset into MySQL and execute queries.

### Python
Run scripts in order:
- python eda/01_load_data.py
- python eda/02_clean_data.py
- python eda/03_analysis.py
- python eda/04_visualizations.py
- python eda/05_advanced_sql.py
- python eda/06_advanced_visualizations.py
- python eda/07_rfm_scoring.py
- python eda/08_rfm_segmentation.py

### Power BI
Open:
Online Retail.pbix

---

## 📬 Author

Nevena Ćulibrk
Aspiring Data Analyst | SQL | Python | Power BI
Serbia
