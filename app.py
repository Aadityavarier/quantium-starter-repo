import pandas as pd
import dash
from dash import html, dcc
import plotly.express as px

# Load the cleaned sales data
df = pd.read_csv("data/formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Group sales by date
daily_sales = df.groupby("date")["sales"].sum().reset_index()

# Create figure
fig = px.line(daily_sales, x="date", y="sales", title="Daily Sales of Pink Morsel")
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales ($)",
    title_x=0.5  # center the title
)

# Create the Dash app
app = dash.Dash(__name__)
app.title = "Soul Foods Sales Dashboard"

# Layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

# Run
if __name__ == "__main__":
    app.run(debug=True)
