import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Load your data
df = pd.read_csv(r'C:\Users\komal khatri\OneDrive\Desktop\Details\Details.csv')

# Initialize the Dash app with a custom Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Define the layout of the dashboard
app.layout = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H1("🛋 Fancy Furniture Sales Dashboard", className="display-3", style={'color': '#46266D'}),
                        html.P(
                            "Visualize and analyze furniture sales data.",
                            className="lead",
                        ),
                    ]
                )
            ],
            className="mb-3",
            style={'background-color': '#b19cd9', 'border-color': '#46266D'}
        ),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Graph(
                        id='scatter-plot',
                        figure=px.scatter(
                            df, x='Amount', y='Profit', color='Category',
                            hover_data=['Sub-Category'], title='Sales Scatter Plot'
                        ).update_layout(
                            margin=dict(l=0, r=0, t=30, b=0),
                            plot_bgcolor='#f9f9f9',
                            paper_bgcolor='#f9f9f9',
                        )
                    ),
                    md=6,
                ),
                dbc.Col(
                    dcc.Graph(
                        id='histogram',
                        figure=px.histogram(
                            df, x='Amount', color='Category', marginal='rug',
                            title='Sales Amount Histogram'
                        ).update_layout(
                            margin=dict(l=0, r=0, t=30, b=0),
                            plot_bgcolor='#f9f9f9',
                            paper_bgcolor='#f9f9f9',
                        )
                    ),
                    md=6,
                ),
            ],
        ),
    ],
    fluid=True,
    style={'background-color': '#f9f9f9'}
)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
