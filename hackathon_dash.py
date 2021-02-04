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

import random
# import dash_table
# import numpy as np
import pandas as pd
# import plotly.graph_objects as go
from dash.dependencies import Input, Output, State


################################################################
# Dash App Setup and Style Sheets
BS = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/lux/bootstrap.min.css"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True
server = app.server
app.title = "Minds Matter"
warnings.filterwarnings("ignore")

################################################################
# Import Data
states_df = pd.read_csv("./data/states.csv")
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
        html.H1("Minds Matter"),
        dbc.Tabs(
            [
                # Tab 1: Home Page
                dbc.Tab(label="Home", tab_id="home", children=[
                    html.Br(),
                    dcc.Markdown('''
                    ## Pandemic Mental Health Risk Assessment
                    '''),
                    html.Br(),
                    dbc.Row([
                            dbc.Col(
                                html.Div(
                                    html.Img(src=app.get_asset_url("healthymind.png"))
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    html.Img(src=app.get_asset_url("humanalogo.png"))
                                )
                            ),
                            dbc.Col(
                                html.Div(
                                    html.Img(src=app.get_asset_url("pandemic.png"))
                                )
                            ),
                    ]),
                    dcc.Markdown('''
                    In the midst of a pandemic, mental health is a serious issue that cannot be ignored. Quarantine 
                    orders, financial strain, and pandemic-related stress can contribute to depression, anxiety, 
                    and other mental health risks. This tool provides a mental health risk assessment to bring awareness
                    of your mental health status and provides resources for your mental health during the pandemic. To
                    complete the assessment, please answer the following questions below.
                    >
                    > **Disclaimer**: This tool is meant to be used as a risk assessment tool for self-awareness. It is not
                    > meant to replace a professional assessment or a psychiatric evaluation. Please note that the
                    > number you receive does not define you and can change based on a number of circumstances.
                    >
                    '''),
                    # Name
                    html.P("What is your name?"),
                    dbc.Input(type="text", id="example-name", placeholder="Name"),
                    html.Br(),
                    # Q1: State
                    html.P("In what state do you currently reside?"),
                    dcc.Dropdown(className='div-for-dropdown', id="q1", clearable=True,
                                 options=[{'label': i, 'value': i} for i in states_df['State']]),
                    html.Br(),
                    # Q2: County
                    html.P("In what county do you currently reside?"),
                    dbc.Input(type="text", id="q2", placeholder="County Name"),
                    html.Br(),
                    # Q3: Age
                    html.P("What is your age?"),
                    dbc.Input(type="number", id="q3", placeholder="Age"),
                    html.Br(),
                    # Q4: Gender
                    html.P("What is your gender?"),
                    dcc.Dropdown(className='div-for-dropdown', id="q4", clearable=True,
                                 options=[
                                      {'label': 'Male', 'value': 0},
                                      {'label': 'Female', 'value': 1},
                                      {'label': 'Transgender Female', 'value': 2},
                                      {'label': 'Transgender Male', 'value': 3},
                                      {'label': 'Non-Binary', 'value': 4}
                                  ]),
                    html.Br(),
                    # Q5: Children
                    html.P("How many children do you have?"),
                    dbc.Input(type="number", id="q5", placeholder="Number of Children"),
                    html.Br(),
                    # Q6: Smoking
                    html.P("Do you currently smoke?"),
                    dcc.Dropdown(className='div-for-dropdown', id="q6", clearable=False,
                                 options=[
                                     {'label': 'Yes', 'value': 1},
                                     {'label': 'No', 'value': 0}
                                 ]),
                    html.Br(),
                    # Q7: Work Hours
                    html.P("In the past week, how many hours were you working for pay?"),
                    dbc.Input(type="number", id="q7", placeholder="Number of Working Hours"),
                    html.Br(),
                    # Q8: Happy Days
                    html.P("On a scale of 0-10, how happy would you say you are, generally?"),
                    dbc.Input(type="number", id="q8", placeholder="Please enter a number from 0-10"),
                    html.Br(),
                    # Q9: Mentally Unhealthy Days
                    html.P("In the past 30 days, how many days have you felt mentally unhealthy?"),
                    dbc.Input(type="number", id="q9", placeholder="Please enter a number less than 30"),
                    html.Br(),
                    # Q10: Anxiety Increase
                    html.P("In the past 30 days, have you felt more anxious than previously?"),
                    dcc.Dropdown(className='div-for-dropdown', id="q10", clearable=False,
                                 options=[
                                     {'label': 'Yes', 'value': 1},
                                     {'label': 'No', 'value':0}
                                 ]),
                    html.Br(),
                    html.Button(id='submit-button', n_clicks=0, children='Submit'),
                    html.Br(),
                    html.Br(),
                    html.Div(id='outcome'),
                    html.Br()
                ]),
                # Tab 2: Resources
                dbc.Tab(label="Resources", tab_id="resources", children=[
                    html.Br(),
                    dcc.Markdown('''
                        Remember that you are not alone, and there are many people and resources available to you. The
                        pandemic has been extremely stressful for many others as well. While we understand that each
                        person's situation is different, here are some resources for help.
                        ### Maintaining Mental and Physical Health
                        Please remember to:
                        * Drink plenty of water and eat 3 meals a day
                        * Get at least 6-8 hours of sleep
                        * Participate in physical activity
                        * Reach out to friends and family virtually
                        * Engage in meaningful activities and hobbies in a safe manner
                        ### National Resources
                        * [Financial Assistance for Disasters](https://www.usa.gov/disaster-help-food-housing-bills)
                        * [US Department of Labor Resources for Unemployment and Financial Strain]
                        (https://www.dol.gov/coronavirus)
                        ### Hotlines
                        * [National Suicide Prevention Lifeline](https://suicidepreventionlifeline.org/): 
                        1-800-273-TALK (8255) for English, 1-888-628-9454 for Spanish, or 
                        [Lifeline Crisis Chat](https://suicidepreventionlifeline.org/chat/)
                        * [National Domestic Violence Hotline](https://www.thehotline.org/): 
                        1-800-799-7233 or text LOVEIS to 22522 
                        * [National Child Abuse Hotline](https://www.childhelp.org/hotline/): 
                        1-800-4AChild (1-800-422-4453) or text 1-800-422-4453 
                        * [National Sexual Assault Hotline](https://rainn.org/): 1-800-656-HOPE (4673) or 
                        [Online Chat](https://hotline.rainn.org/online)
                        * [Veteran’s Crisis Line](https://www.veteranscrisisline.net/): 1-800-273-TALK (8255) 
                        or [Crisis Chat](https://www.veteranscrisisline.net/get-help/chat) or text: 8388255 
                        * [Disaster Distress Helpline](https://www.samhsa.gov/disaster-preparedness): CALL or 
                        TEXT 1-800-985-5990 (press 2 for Spanish)
                        * [The Eldercare Locator](https://eldercare.acl.gov/Public/Index.aspx): 1-800-677-1116 – 
                        TTY Instructions 
                        ### Humana Resources
                        * Apply for a [Healthy Food Card](https://www.humana.com/logon/) from Humana to get 
                        supplemental spending on food
                        * Participate in our [Loneliness Prevention Program](https://www.humana.com/logon/), 
                        which connects you with college students virtually to have weekly engaging and 
                        meaningful conversations with someone new
                        * Find a [Mental Health Provider](https://www.humana.com/logon/) in your area
                    '''),
                ]),
                dbc.Tab(label="Why Minds Matter", tab_id="deck", children=[
                    html.Br(),
                    dcc.Markdown('''## Problems We Face'''),
                    html.Img(src=app.get_asset_url("deck1.png")),
                    dcc.Markdown('''
                    Text here. Behavioral Health is the cornerstone of any public health efforts.
                    '''),
                    dcc.Markdown('''## Solution We Propose'''),
                    html.Img(src=app.get_asset_url("deck2.png")),
                ]),
                dbc.Tab(label="Our Team", tab_id="team", children=[
                    html.Br(),
                    html.P(
                        "We are a group of data scientists and behavioral health experts within the AI Integration"
                        " CPS and OHAA (AICO) team at Humana."
                    ),
                    html.Br(),
                    dbc.Row([
                        dbc.Col(
                            html.P("Eshan Bhatt")
                        ),
                        dbc.Col(
                            html.P("Nibhrat Lohia")
                        ),
                        dbc.Col(
                            html.P("Minh Luu")
                        ),
                    ]),
                    dbc.Row([
                        dbc.Col(
                            html.P("Sreedevi Madhusoodhanan Lalithambika")
                        ),
                        dbc.Col(
                            html.P("Poornima Ramalingam")
                        ),
                        dbc.Col(
                            html.Div(children=[
                                dcc.Markdown('''
                                **Adeline Shin**                              
                                Data Scientist
                                '''),
                                html.Img(src=app.get_asset_url("adeline.JPG"))
                            ])
                        ),
                    ]),
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
    Output(component_id='outcome', component_property='children'),
    [Input(component_id='submit-button', component_property='n_clicks')],
    [State(component_id='example-name', component_property='value'),
     State(component_id='q1', component_property='value'),
     State(component_id='q2', component_property='value'),
     State(component_id='q3', component_property='value'),
     State(component_id='q4', component_property='value'),
     State(component_id='q5', component_property='value'),
     State(component_id='q6', component_property='value'),
     State(component_id='q7', component_property='value'),
     State(component_id='q8', component_property='value'),
     State(component_id='q9', component_property='value'),
     State(component_id='q10', component_property='value')]
)
def get_output(n_clicks, name_input, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    click_value = n_clicks
    if click_value is None:
            raise dash.exceptions.PreventUpdate
    elif click_value >= 1:
        output = random.randint(0,10)
        if output <=1:
            output_category = "low"
            category_suggestions = "" \
                                   "Because your mental health risk score is low, it is suggested that you to " \
                                   "continue to take care of yourself in the same manner. Should anything change, " \
                                   "feel free to complete the assessment again."
        elif output <= 3:
            output_category = "moderate"
            category_suggestions = "" \
                                   "Because your mental health score is moderate, it is suggested that you "
        elif output <= 6:
            output_category = "high"
            category_suggestions = "" \
                                   "Because your mental health risk score is high, "
        else:
            output_category = "very high"
            category_suggestions = "" \
                                   "Because your mental health risk score is very high, "
        return u'''
            {}, your mental health risk score is: {}, which is considered {} on our scale. Please check our 
            resources tab for more information on ways to improve your mental health and get help during the pandemic.
            {}
        '''.format(name_input, output, output_category, category_suggestions)

################################################################
# Load to Dash
if __name__ == "__main__":
    app.run_server(debug=True)
