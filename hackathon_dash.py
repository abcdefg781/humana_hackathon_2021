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

# local modules
from Model import *
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
                                html.Img(src=app.get_asset_url("man_photo.PNG"), style={'height': '105%', 'width': '105%'})
                            )
                        ),
                        dbc.Col(
                            html.Div(
                                html.Img(src=app.get_asset_url("humanalogo.png"))
                            )
                        ),
                        dbc.Col(
                            html.Div(
                                html.Img(src=app.get_asset_url("woman.PNG"))
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
                    # Q0.1: State
                    html.P("In what state do you currently reside?"),
                    dcc.Dropdown(className='div-for-dropdown', id="example-state", clearable=True,
                                 options=[{'label': i, 'value': i} for i in states_df['State']]),
                    html.Br(),
                    # Q0.2: County
                    html.P("In what county do you currently reside?"),
                    dbc.Input(type="text", id="example-county", placeholder="County Name"),
                    html.Br(),
                    # Q1: Gender
                    html.P("What is your current self-identified gender?"),
                    dcc.Dropdown(className='div-for-dropdown', id="q1", clearable=True,
                                 options=[
                                     {'label': 'Male', 'value': 0},
                                     {'label': 'Female', 'value': 1},
                                     {'label': 'Other', 'value': 1}
                                 ]),
                    html.Br(),
                    # Q2: Age
                    html.P("What is your age?"),
                    dbc.Input(type="number", id="q2", placeholder="Age"),
                    html.Br(),
                    # Q3: Children
                    html.P("Do you have children aged 18 or below and/or living with you?"),
                    dbc.Input(type="number", id="q3", placeholder="Number of Children"),
                    html.Br(),
                    # Q4: Work Hours
                    html.P("In the past week, how many hours were you working for pay?"),
                    dbc.Input(type="number", id="q4", placeholder="Number of Working Hours"),
                    html.Br(),
                    # Q5: Mentally Unhealthy Days
                    html.P("In the past 30 days, how many days have you felt mentally unhealthy?"),
                    dbc.Input(type="number", id="q5", placeholder="Please enter a number less than 30"),
                    html.Br(),
                    html.P("The following questions use a scale from 1-10. Please provide your answer using the scale"
                           " with 1 indicating the lowest and 10 indicating the highest."),
                    # Q6: Anxiety Increase
                    html.P("In the past 30 days, on a scale from 1-10, what would you say is the level of your anxiety"
                           " and stress?"),
                    dcc.Slider(id='q6', min=1, max=10, value=5,
                               marks={
                                   1: {'label': '1'},
                                   2: {'label': '2'},
                                   3: {'label': '3'},
                                   4: {'label': '4'},
                                   5: {'label': '5'},
                                   6: {'label': '6'},
                                   7: {'label': '7'},
                                   8: {'label': '8'},
                                   9: {'label': '9'},
                                   10: {'label': '10'}
                               }),
                    html.Br(),
                    # Q7: Home Stress
                    html.P("On a scale from 1-10, how stressed are you about your home (including financial status, "
                           "relationships, and other home-related factors.)"),
                    dcc.Slider(id='q7', min=1, max=10, value=5,
                               marks={
                                   1: {'label': '1'},
                                   2: {'label': '2'},
                                   3: {'label': '3'},
                                   4: {'label': '4'},
                                   5: {'label': '5'},
                                   6: {'label': '6'},
                                   7: {'label': '7'},
                                   8: {'label': '8'},
                                   9: {'label': '9'},
                                   10: {'label': '10'}
                               }),
                    html.Br(),
                    # Q8: Future Stress
                    html.P("On a scale from 1-10, how stressed are you about your future, generally?"),
                    dcc.Slider(id='q8', min=1, max=10, value=5,
                               marks={
                                   1: {'label': '1'},
                                   2: {'label': '2'},
                                   3: {'label': '3'},
                                   4: {'label': '4'},
                                   5: {'label': '5'},
                                   6: {'label': '6'},
                                   7: {'label': '7'},
                                   8: {'label': '8'},
                                   9: {'label': '9'},
                                   10: {'label': '10'}
                               }),
                    html.Br(),
                    # Q9: Satisfaction
                    html.P("On a scale from 1-10, how satisfied are you with life, generally?"),
                    dcc.Slider(id='q9', min=1, max=10, value=5,
                               marks={
                                   1: {'label': '1'},
                                   2: {'label': '2'},
                                   3: {'label': '3'},
                                   4: {'label': '4'},
                                   5: {'label': '5'},
                                   6: {'label': '6'},
                                   7: {'label': '7'},
                                   8: {'label': '8'},
                                   9: {'label': '9'},
                                   10: {'label': '10'}
                               }),
                    html.Br(),
                    # Q10: Happiness
                    html.P("On a scale from 1-10, how happy are you with life, generally?"),
                    dcc.Slider(id='q10', min=1, max=10, value=5,
                               marks={
                                   1: {'label': '1'},
                                   2: {'label': '2'},
                                   3: {'label': '3'},
                                   4: {'label': '4'},
                                   5: {'label': '5'},
                                   6: {'label': '6'},
                                   7: {'label': '7'},
                                   8: {'label': '8'},
                                   9: {'label': '9'},
                                   10: {'label': '10'}
                               }),
                    html.Br(),
                    # Optional Ask
                    html.P("Is there anything else you would like to share? Anything else we should know about your"
                           " mental health state, or any feedback you would like to provide?"),
                    dcc.Textarea(id='text-area-example', value='', style={'width': '100%', 'height': 100}),
                    html.Br(),
                    html.Br(),
                    html.Button(id='submit-button', n_clicks=0, children='Submit'),
                    html.Br(),
                    html.Br(),
                    html.Div(id='outcome'),
                    html.Br()
                ]),
                # Tab 2: Personalized Recommendations
                dbc.Tab(label="Personalized Recommendations", tab_id="recommendations", children=[
                    html.Br(),
                    dcc.Markdown('''
                    ## Personalized Recommendations Tailored to Your Needs
                    Below are some personalized recommendations based on your mental health risk score. These are 
                    suggestions based on the top factors influencing your risk score. Please remember that your score
                    is fluid and does not define who you are.
                    ''')
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
                    html.Br(),
                    html.Img(src=app.get_asset_url("deck1_photo.PNG"), style={'height':'80%', 'width':'80%'}),
                    dcc.Markdown('''
                    During the pandemic in 2020, it is estimated that mental distress has increased by three times. Even
                    worse, this year, more than 35 million more people will need mental health services. Pandemics are
                    known to increase the amount of isolation, job insecurity, fear of losing loved ones, anxiety,
                    depression, and much more. To combat this, we need a tool that is based on behavioral health and
                    can bring awareness to mental health and hopefully improve it.
                    '''),
                    dcc.Markdown('''## Solution We Propose'''),
                    html.Img(src=app.get_asset_url("deck2_photo.PNG"), style={'height':'80%', 'width':'80%'}),
                    dcc.Markdown('''
                    Minds Matter is driven by immeasurable impacts of behavioral health interventions and great desire
                    to help those who have suffered mental health distress during the pandemic. Our solution is an
                    interactive tool built out of a database containing both individual behavioral and geospatial data.
                    
                    Minds Matter prioritizes evaluating mental health risks early on to make users aware of their 
                    risk early on in a personalized, private, and time-efficient space.
                    '''),
                    html.Br(),
                    html.Br(),
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
                            html.Div(children=[
                                dcc.Markdown('''
                                    **Minh Luu**                              
                                    Behavioral Health/Data Scientist
                                    '''),
                                html.Img(src=app.get_asset_url("minh.jpg"))
                            ])
                        ),
                    ]),
                    html.Br(),
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
                    html.Br(),
                    html.Br(),
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
        output = get_model_output(name_input=name_input,
                                  gender=q1,
                                  age=q2,
                                  children=q3,
                                  work_hrs=q4,
                                  Unhealth_Days=q5,
                                  anxiety_increase=q6,
                                  stress_home=q7,
                                  stress_future=q8,
                                  satisfied=q9,
                                  happy=q10)
        if output <= 1:
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