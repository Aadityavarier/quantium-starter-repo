import pandas as pd
import glob
import dash
from dash import html, dcc
import plotly.express as px

# Step 1: Load and combine CSVs
files = glob.glob("data/daily_sales_data_*.csv")
df = pd.concat([pd.read_csv(file) for file in files])

# Step 2: Clean and process data
df = df[df["product"] == "pink morsel"]  # Filter for pink morsel
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
df["revenue"] = df["price"] * df["quantity"]
df["date"] = pd.to_datetime(df["date"])

# Step 3: Group by date
grouped = df.groupby("date")["revenue"].sum().reset_index()

# Step 4: Create Dash app
app = dash.Dash(__name__)
app.title = "Quantium Dashboard"

# Step 5: Create figure
fig = px.line(grouped, x="date", y="revenue", title="Daily Revenue - Pink Morsel")

# Step 6: Layout
app.layout = html.Div([
    html.H1("Quantium Sales Dashboard", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

# Step 7: Run
if __name__ == "__main__":
    app.run(debug=True)
