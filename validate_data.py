"""Profile and validate the sales CSV before it goes into the dashboard.

Run:  python scripts/validate_data.py data/sales_data.csv
Every check here is one the AI-generated dashboard must also pass:
the totals printed below should match the KPI cards.
"""
import sys
import pandas as pd

path = sys.argv[1] if len(sys.argv) > 1 else "data/sales_data.csv"
df = pd.read_csv(path)

# 1. Structure: columns, types, missing values
print("Columns:", list(df.columns))
print("Rows:", len(df), "| Missing values:", int(df.isna().sum().sum()))

# 2. Clean: "$88.00" is text, so convert it to a number
df["Price"] = df["Price"].str.replace(r"[$,]", "", regex=True).astype(float)
df["Date"] = pd.to_datetime(df["Date"], errors="raise")

# 3. Integrity: each product should have exactly one price
assert (df.groupby("Product")["Price"].nunique() == 1).all(), "Product with several prices"

# 4. Reference totals (compare with the dashboard KPIs)
orders = df["Order Number"].nunique()
revenue = df["Price"].sum()
print(f"Date range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Revenue: ${revenue:,.2f} | Orders: {orders} | Items: {len(df)} | AOV: ${revenue / orders:,.2f}")

# 5. Breakdowns to cross-check the charts
print("\nRevenue by product:\n", df.groupby("Product")["Price"].agg(["sum", "count"]).sort_values("sum", ascending=False))
print("\nRevenue by payment method:\n", df.groupby("Payment Method")["Price"].agg(["sum", "count"]))
