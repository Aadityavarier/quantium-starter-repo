import pandas as pd
import dash
from dash import html, dcc, Output, Input
import plotly.express as px

# Load and prepare data
df = pd.read_csv("data/formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Start Dash app
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Visualizer"

# App layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer", style={"textAlign": "center", "color": "#880E4F"}),

    html.Div([
        html.Label("Select Region:", style={"fontWeight": "bold", "marginRight": "10px"}),
        dcc.RadioItems(
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            id="region-filter",
            labelStyle={"display": "inline-block", "margin": "10px"},
            inputStyle={"marginRight": "5px"}
        )
    ], style={"textAlign": "center", "marginBottom": "30px"}),

    dcc.Graph(id="sales-line-chart")
], style={"fontFamily": "Arial", "backgroundColor": "#FCE4EC", "padding": "20px"})

# Callback to update chart
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]
    
    grouped = filtered_df.groupby("date")["sales"].sum().reset_index()
    fig = px.line(grouped, x="date", y="sales", title=f"Sales in Region: {selected_region.title() if selected_region != 'all' else 'All'}")
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        plot_bgcolor="#F8BBD0",
        paper_bgcolor="#FCE4EC",
        title_x=0.5
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
