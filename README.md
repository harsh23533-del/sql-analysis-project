# 🛒 Superstore SQL Analysis Dashboard

An interactive SQL-powered business analytics dashboard built on the Global Superstore dataset, designed to surface key business insights through 10+ SQL queries and visualize them using an interactive Streamlit interface.

**🔗 Live Demo:** [sql-analysis-project.streamlit.app](https://sql-analysis-project-k95lhybxnsi7exabhgnjnc.streamlit.app/)

---

## 📊 Overview

This project takes raw retail sales data, loads it into a relational database, and runs business-focused SQL queries to extract actionable insights — all presented through a clean, interactive dashboard. It demonstrates the full data analytics pipeline: **data ingestion → SQL querying → visualization**.

## ✨ Features

The dashboard offers 8 different analysis views, selectable from a sidebar dropdown:

- **Revenue by Region** — breakdown of total revenue across geographic regions
- **Top 10 Products** — best-performing products by sales
- **Monthly Sales Trend** — time-series view of sales performance over months
- **Customer Lifetime Value** — top customers ranked by total lifetime spend
- **Profit Margin by Category** — profitability comparison across product categories
- **Discount Impact on Profit** — how discounting strategies affect overall profit
- **Top States by Revenue** — highest revenue-generating states
- **Shipping Mode Analysis** — performance and usage breakdown by shipping method

Each analysis combines a data table with an interactive Plotly chart for quick visual interpretation.

## 🛠️ Tech Stack

- **Python** — core application logic
- **SQL** (SQLite) — data storage and query engine
- **Streamlit** — interactive web dashboard framework
- **Plotly** — data visualization
- **Pandas** — data manipulation

## 📁 Project Structure

```
sql-analysis-project/
├── data/                # Raw dataset (Global Superstore)
├── database/             # SQLite database files
├── insights/              # Query outputs / saved insights
├── create_sql.py        # Creates database schema and tables
├── load_data.py          # Loads raw data into the database
├── run_queries.py        # Executes the 10 business SQL queries
├── app.py                  # Streamlit dashboard application
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

1. Clone the repository
   ```bash
   git clone https://github.com/harsh23533-del/sql-analysis-project.git
   cd sql-analysis-project
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database and load data
   ```bash
   python create_sql.py
   python load_data.py
   ```

4. Run the dashboard
   ```bash
   streamlit run app.py
   ```

5. Open `http://localhost:8501` in your browser

## 📌 Key Insights Generated

- Identification of top revenue-driving regions and states
- Highest lifetime-value customers driving repeat business
- Product categories with strongest profit margins
- Quantified impact of discounting on overall profitability
- Seasonal/monthly sales trends for forecasting

## 👤 Author

**Harsh Pandey**
B.Tech Data Science & Analytics, KNIT Sultanpur
[GitHub](https://github.com/harsh23533-del)
