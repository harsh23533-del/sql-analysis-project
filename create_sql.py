sql_content = """-- =============================================
-- SUPERSTORE SQL ANALYSIS PROJECT
-- =============================================

-- 1. Revenue by Region
SELECT Region, 
       ROUND(SUM(Sales), 2) AS Total_Sales,
       ROUND(SUM(Profit), 2) AS Total_Profit,
       COUNT(DISTINCT [Order ID]) AS Total_Orders
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;

-- 2. Top 10 Products by Profit
SELECT [Product Name],
       ROUND(SUM(Profit), 2) AS Total_Profit,
       ROUND(SUM(Sales), 2) AS Total_Sales,
       SUM(Quantity) AS Units_Sold
FROM superstore
GROUP BY [Product Name]
ORDER BY Total_Profit DESC
LIMIT 10;

-- 3. Monthly Sales Trend
SELECT SUBSTR([Order Date], 1, 7) AS Month,
       ROUND(SUM(Sales), 2) AS Monthly_Sales,
       ROUND(SUM(Profit), 2) AS Monthly_Profit
FROM superstore
GROUP BY Month
ORDER BY Month;

-- 4. Customer Lifetime Value (Top 10)
SELECT [Customer Name],
       ROUND(SUM(Sales), 2) AS Lifetime_Value,
       COUNT(DISTINCT [Order ID]) AS Total_Orders,
       ROUND(AVG(Sales), 2) AS Avg_Order_Value
FROM superstore
GROUP BY [Customer Name]
ORDER BY Lifetime_Value DESC
LIMIT 10;

-- 5. Category Performance
SELECT Category, [Sub-Category],
       ROUND(SUM(Sales), 2) AS Total_Sales,
       ROUND(SUM(Profit), 2) AS Total_Profit,
       ROUND(AVG(Discount)*100, 1) AS Avg_Discount_Pct
FROM superstore
GROUP BY Category, [Sub-Category]
ORDER BY Category, Total_Profit DESC;

-- 6. Discount Impact on Profit
SELECT 
  CASE 
    WHEN Discount = 0 THEN '0% - No Discount'
    WHEN Discount <= 0.1 THEN '1-10%'
    WHEN Discount <= 0.2 THEN '11-20%'
    WHEN Discount <= 0.3 THEN '21-30%'
    ELSE '30%+ Heavy Discount'
  END AS Discount_Range,
  COUNT(*) AS Orders,
  ROUND(AVG(Profit), 2) AS Avg_Profit,
  ROUND(SUM(Sales), 2) AS Total_Sales
FROM superstore
GROUP BY Discount_Range
ORDER BY Avg_Profit DESC;

-- 7. Shipping Mode Analysis
SELECT [Ship Mode],
       COUNT(*) AS Total_Orders,
       ROUND(SUM(Sales), 2) AS Total_Sales,
       ROUND(AVG(Profit), 2) AS Avg_Profit
FROM superstore
GROUP BY [Ship Mode]
ORDER BY Total_Orders DESC;

-- 8. Loss-making Products
SELECT [Product Name], [Sub-Category],
       ROUND(SUM(Profit), 2) AS Total_Profit,
       ROUND(SUM(Sales), 2) AS Total_Sales,
       COUNT(*) AS Times_Ordered
FROM superstore
GROUP BY [Product Name]
HAVING Total_Profit < 0
ORDER BY Total_Profit ASC
LIMIT 15;

-- 9. Year-over-Year Growth
SELECT 
  SUBSTR([Order Date], 7, 4) AS Year,
  ROUND(SUM(Sales), 2) AS Total_Sales,
  ROUND(SUM(Profit), 2) AS Total_Profit,
  COUNT(DISTINCT [Order ID]) AS Total_Orders
FROM superstore
GROUP BY Year
ORDER BY Year;

-- 10. RFM Segmentation
SELECT [Customer Name],
       COUNT(DISTINCT [Order ID]) AS Frequency,
       ROUND(SUM(Sales), 2) AS Monetary,
       MAX([Order Date]) AS Last_Order_Date,
       CASE 
         WHEN COUNT(DISTINCT [Order ID]) >= 10 AND SUM(Sales) >= 5000 THEN 'Champion'
         WHEN COUNT(DISTINCT [Order ID]) >= 5 AND SUM(Sales) >= 2000 THEN 'Loyal'
         WHEN COUNT(DISTINCT [Order ID]) >= 3 THEN 'Potential'
         ELSE 'At Risk'
       END AS RFM_Segment
FROM superstore
GROUP BY [Customer Name]
ORDER BY Monetary DESC;
"""

with open('queries/analysis.sql', 'w') as f:
    f.write(sql_content)

print('analysis.sql created successfully!')
