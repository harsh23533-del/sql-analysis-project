import sqlite3
import pandas as pd

df = pd.read_csv("data/superstore.csv", encoding="latin1")
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("-", "_")

print("Columns:", df.columns.tolist())
print("Shape:", df.shape)


conn = sqlite3.connect("data/superstore.db")
df.to_sql("orders", conn, if_exists="replace", index=False)
conn.close()

print("✅ Database ready! orders table created.")