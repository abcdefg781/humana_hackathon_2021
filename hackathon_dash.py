################################################################
# Humana Hackathon Dashboard
# Team AICO
# February 5, 2021

################################################################
# Import Required packages
import warnings

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# import dash_table
# import numpy as np
# import pandas as pd
# import plotly.graph_objects as go
from dash.dependencies import Input, Output

################################################################
# Dash App Setup and Style Sheets
BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/lux/bootstrap.min.css"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True
server = app.server
app.title = "Pandemic Mental Health Dashboard"
warnings.filterwarnings("ignore")

################################################################
# Import Data

################################################################
# Functions Within App

################################################################
# App Layout
app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),
        dcc.Location(id='url-output', refresh=False),
        dcc.Store(id="store"),
        html.Br(),
        html.Br(),
        html.H1("Pandemic Mental Health Risk Assessment"),
        dbc.Tabs(
            [
                dbc.Tab(label="Home", tab_id="home", children=[
                    html.Br(),
                    html.P(
                        "In the midst of a pandemic, mental health is a serious issue that cannot be ignored. "
                        "Quarantine orders, financial strain, pandemic-related stress, and other aspects can "
                        "contribute to depression, anxiety, and other mental health risks. To complete your "
                        "mental health assessment and get resources for your mental health during the pandemic, "
                        "please answer the following questions."),
                    dbc.Input(type="text", id="example-name", placeholder="Name"),
                    html.Br(),
                    dbc.Input(type="text", id="example-zip", placeholder="Zip Code"),
                    # dcc.Dropdown(className='div-for-dropdown', id='standings_year', value=2020, clearable=False,
                    #              options=[{'label': i, 'value': i} for i in races_df['year'].unique()]),
                    html.Div(id='outcome'),
                ]),
                dbc.Tab(label="Resources", tab_id="resources", children=[
                    html.Br(),
                    html.P(
                        "Please remember to drink plenty of water, eat 3 meals a day, get 8 hours of sleep, and "
                        "get physical exercise in the midst of the pandemic. You are also encouraged to reach out to "
                        "friends and family virtually and engage in meaningful hobbies in a safe manner."),
                    html.Br(),
                    html.P(
                        "The following is a list of national resources and hotlines that are available at this time:"
                    ),
                    html.Br(),
                    html.P(
                        "Additionally, Humana has the following resources to help cope with the stress of the "
                        "pandemic."
                    )
                ])
            ],
            id="tabs",
            active_tab="home",
        )
    ]
)

################################################################
# App Callback
@app.callback(
    [Output(component_id='outcome', component_property='value')],
    [Input(component_id='example-name', component_property='value'),
     Input(component_id='example-zip', component_property='value')]
)
def get_output(input_value):
    output = 3
    return 'Your predicted mental health risk score is: {}'.format(output)


################################################################
# Load to Dash
if __name__ == "__main__":
    app.run_server(debug=True)