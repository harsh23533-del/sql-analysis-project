import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

conn = sqlite3.connect("data/superstore.db")

st.set_page_config(page_title="SQL Analysis Dashboard", layout="wide")
st.title("🛒 Superstore SQL Analysis Dashboard")

# Sidebar
query_choice = st.sidebar.selectbox("Select Analysis", [
    "Revenue by Region",
    "Top 10 Products",
    "Monthly Sales Trend",
    "Customer Lifetime Value",
    "Profit Margin by Category",
    "Discount Impact on Profit",
    "Top States by Revenue",
    "Shipping Mode Analysis",
    "Sub-Category Profit Ranking"
])

if query_choice == "Revenue by Region":
    df = pd.read_sql("SELECT Region, ROUND(SUM(Sales),2) AS Total_Revenue, ROUND(SUM(Profit),2) AS Total_Profit FROM orders GROUP BY Region ORDER BY Total_Revenue DESC", conn)
    st.subheader("💰 Revenue by Region")
    fig = px.bar(df, x="Region", y="Total_Revenue", color="Total_Profit", title="Revenue & Profit by Region")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

elif query_choice == "Top 10 Products":
    df = pd.read_sql("SELECT Product_Name, ROUND(SUM(Sales),2) AS Total_Sales FROM orders GROUP BY Product_Name ORDER BY Total_Sales DESC LIMIT 10", conn)
    st.subheader("🏆 Top 10 Products by Sales")
    fig = px.bar(df, x="Total_Sales", y="Product_Name", orientation="h", title="Top 10 Products")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

elif query_choice == "Monthly Sales Trend":
    df = pd.read_sql("SELECT SUBSTR(Order_Date,1,7) AS Month, ROUND(SUM(Sales),2) AS Monthly_Sales FROM orders GROUP BY Month ORDER BY Month", conn)
    st.subheader("📈 Monthly Sales Trend")
    fig = px.line(df, x="Month", y="Monthly_Sales", title="Monthly Sales Trend")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

elif query_choice == "Customer Lifetime Value":
    df = pd.read_sql("SELECT Customer_Name, COUNT(DISTINCT Order_ID) AS Total_Orders, ROUND(SUM(Sales),2) AS Lifetime_Value FROM orders GROUP BY Customer_Name ORDER BY Lifetime_Value DESC LIMIT 10", conn)
    st.subheader("👤 Top 10 Customers by Lifetime Value")
    fig = px.bar(df, x="Lifetime_Value", y="Customer_Name", orientation="h", title="Customer LTV")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

elif query_choice == "Profit Margin by Category":
    df = pd.read_sql("SELECT Category, ROUND(SUM(Sales),2) AS Sales, ROUND(SUM(Profit),2) AS Profit, ROUND(SUM(Profit)*100.0/SUM(Sales),2) AS Margin_Pct FROM orders GROUP BY Category", conn)
    st.subheader("📊 Profit Margin by Category")
    fig = px.pie(df, names="Category", values="Margin_Pct", title="Profit Margin %")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

elif query_choice == "Discount Impact on Profit":
    df = pd.read_sql("SELECT CASE WHEN Discount=0 THEN 'No Discount' WHEN Discount<=0.2 THEN 'Low' WHEN Discount<=0.4 THEN 'Medium' ELSE 'High' END AS Discount_Band, ROUND(AVG(Profit),2) AS Avg_Profit, COUNT(*) AS Orders FROM orders GROUP BY Discount_Band", conn)
    st.subheader("🏷️ Discount Impact on Profit")
    fig = px.bar(df, x="Discount_Band", y="Avg_Profit", color="Avg_Profit", title="Avg Profit by Discount Band")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

elif query_choice == "Top States by Revenue":
    df = pd.read_sql("SELECT State, ROUND(SUM(Sales),2) AS Revenue FROM orders GROUP BY State ORDER BY Revenue DESC LIMIT 10", conn)
    st.subheader("🗺️ Top 10 States by Revenue")
    fig = px.bar(df, x="Revenue", y="State", orientation="h", title="Top States")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

elif query_choice == "Shipping Mode Analysis":
    df = pd.read_sql("SELECT Ship_Mode, COUNT(*) AS Orders, ROUND(AVG(Sales),2) AS Avg_Order_Value FROM orders GROUP BY Ship_Mode ORDER BY Avg_Order_Value DESC", conn)
    st.subheader("🚚 Shipping Mode Analysis")
    fig = px.bar(df, x="Ship_Mode", y="Avg_Order_Value", title="Avg Order Value by Ship Mode")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

elif query_choice == "Sub-Category Profit Ranking":
    df = pd.read_sql("SELECT Sub_Category, ROUND(SUM(Sales),2) AS Sales, ROUND(SUM(Profit),2) AS Profit FROM orders GROUP BY Sub_Category ORDER BY Profit DESC", conn)
    st.subheader("📦 Sub-Category Profit Ranking")
    fig = px.bar(df, x="Sub_Category", y="Profit", color="Profit", title="Profit by Sub-Category")
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df)

conn.close()
