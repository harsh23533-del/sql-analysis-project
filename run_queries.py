import sqlite3
import pandas as pd
import os

conn = sqlite3.connect("data/superstore.db")

queries = {
    "q1_revenue_by_region": """
        SELECT Region, ROUND(SUM(Sales),2) AS Total_Revenue, ROUND(SUM(Profit),2) AS Total_Profit
        FROM orders GROUP BY Region ORDER BY Total_Revenue DESC""",

    "q2_top_products": """
        SELECT Product_Name, ROUND(SUM(Sales),2) AS Total_Sales
        FROM orders GROUP BY Product_Name ORDER BY Total_Sales DESC LIMIT 10""",

    "q3_monthly_trend": """
        SELECT SUBSTR(Order_Date,1,7) AS Month, ROUND(SUM(Sales),2) AS Monthly_Sales
        FROM orders GROUP BY Month ORDER BY Month""",

    "q4_customer_ltv": """
        SELECT Customer_Name, COUNT(DISTINCT Order_ID) AS Total_Orders, ROUND(SUM(Sales),2) AS Lifetime_Value
        FROM orders GROUP BY Customer_Name ORDER BY Lifetime_Value DESC LIMIT 10""",

    "q5_profit_margin": """
        SELECT Category, ROUND(SUM(Sales),2) AS Sales, ROUND(SUM(Profit),2) AS Profit,
        ROUND(SUM(Profit)*100.0/SUM(Sales),2) AS Margin_Pct
        FROM orders GROUP BY Category ORDER BY Margin_Pct DESC""",

    "q6_rfm": """
        SELECT Customer_Name, COUNT(DISTINCT Order_ID) AS Frequency,
        ROUND(SUM(Sales),2) AS Monetary, MAX(Order_Date) AS Last_Order_Date
        FROM orders GROUP BY Customer_Name ORDER BY Monetary DESC LIMIT 20""",

    "q7_discount_impact": """
        SELECT CASE WHEN Discount=0 THEN 'No Discount' WHEN Discount<=0.2 THEN 'Low'
        WHEN Discount<=0.4 THEN 'Medium' ELSE 'High' END AS Discount_Band,
        ROUND(AVG(Profit),2) AS Avg_Profit, COUNT(*) AS Orders
        FROM orders GROUP BY Discount_Band""",

    "q8_top_states": """
        SELECT State, ROUND(SUM(Sales),2) AS Revenue
        FROM orders GROUP BY State ORDER BY Revenue DESC LIMIT 10""",

    "q9_shipping": """
        SELECT Ship_Mode, COUNT(*) AS Orders, ROUND(AVG(Sales),2) AS Avg_Order_Value
        FROM orders GROUP BY Ship_Mode ORDER BY Avg_Order_Value DESC""",

    "q10_subcategory": """
        SELECT Sub_Category, ROUND(SUM(Sales),2) AS Sales, ROUND(SUM(Profit),2) AS Profit
        FROM orders GROUP BY Sub_Category ORDER BY Profit DESC"""
}

os.makedirs("insights", exist_ok=True)

for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    df.to_csv(f"insights/{name}.csv", index=False)
    print(f"✅ {name} — {len(df)} rows")

conn.close()
print("\n🎉 All 10 queries done! Check insights/ folder.")
