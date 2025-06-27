import pandas as pd
import glob

# Load and combine all CSVs
files = glob.glob("data/daily_sales_data_*.csv")
df = pd.concat([pd.read_csv(file) for file in files])

# Filter for pink morsel only
df = df[df["product"] == "pink morsel"]

# Remove "$" from price and convert to float
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

# Create 'sales' column
df["sales"] = df["price"] * df["quantity"]

# Select required columns
final_df = df[["sales", "date", "region"]]

# Save to new CSV
final_df.to_csv("data/formatted_sales_data.csv", index=False)

print("✅ Cleaned file created: data/formatted_sales_data.csv")
