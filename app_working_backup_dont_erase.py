#------------------------------------------------------------------------------------------------

#  Project:    Sensor Analysis Milestone
#  Authors:    - 
#  Good Ref:   https://github.com/Techfitlab/youtube_project/blob/main/app.py
#  Ref dbc:    https://dash-bootstrap-components.opensource.faculty.ai/
#  

#------------------------------------------------------------------------------------------------

# Libraries 
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
#
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math
#
from tabs import tab_1
from tabs import tab_2
from tabs import tab_3
from tabs import tab_4
from tabs import tab_5
from tabs import tab_6

#------------------------------------------------------------------------------------------------

# --- Variables ---
myheading1 = 'Sensor Analysis - AoT Cluster'
tabtitle = 'Array_of_Things Analysis'
sourceurl = 'https://dash.plot.ly/dash-core-components/tabs'
githublink = 'https://github.com/tombresee/Michigan_Milestone'

#------------------------------------------------------------------------------------------------

# --- Initiate the app ---
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_css =         ['http://code.ionicframework.com/ionicons/2.0.0/css/ionicons.min.css',
                        'https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css']
# --- Standard ---
app = dash.Dash(__name__, 
	            external_stylesheets=external_css)

server = app.server

app.title=tabtitle

app.config['suppress_callback_exceptions'] = True  # DO I NEED THIS ? 

#------------------------------------------------------------------------------------------------
# --- Set up the layout ---
app.layout = html.Div([
    html.H4(myheading1),
    dcc.Tabs(id="tabs-example", value='tab-1-example',
             children=[
               dcc.Tab(label='Introduction', value='tab-1-example'),
               dcc.Tab(label='Data Analysis', value='tab-2-example'),
               dcc.Tab(label='Visualization', value='tab-3-example'),
               dcc.Tab(label='Unsupervised Machine Learning', value='tab-4-example'),
               dcc.Tab(label='Temp', value='tab-5-example'),
               dcc.Tab(label='Verbage', value='tab-6-example')]),
    html.Div([
        html.Div(id='tabs-content-example'),
    ], className='twelve columns',
       style={'marginBottom': 50, 'marginTop': 25}),
    html.Div([
       html.A('Code on Github', href=githublink),
       html.Br(),
       html.A("Data Source", href=sourceurl),
             ], className='twelve columns',
                style={'textAlign':'right','fontColor':'#FFFFFF', 'backgroundColor':'white',})
                      ])

#------------------------------------------------------------------------------------------------

# --- Pressing main menu buttons ---
@app.callback(
	Output('tabs-content-example', 'children'),
    [Input('tabs-example', 'value')])   # SOMETIMES THEY DON'T USE THE BRACKETS 
def render_content(tab):
    if tab == 'tab-1-example':
        return tab_1.tab_1_layout
        # return tab_1.tab_something_function()
    elif tab == 'tab-2-example':
        return tab_2.tab_2_layout
    elif tab == 'tab-3-example':
        return tab_3.tab_3_layout
    elif tab == 'tab-4-example':
        return tab_4.tab_4_layout
    elif tab == 'tab-5-example':
        return tab_5.tab_5_layout
    elif tab == 'tab-6-example':
        return tab_6.tab_6_layout

#------------------------------------------------------------------------------------------------

# --- Tab definitions callbacks ---

# ---Old code don't use ---
# @app.callback(dash.dependencies.Output('display-value', 'children'),
#               [dash.dependencies.Input('dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)

# Tab 1 callback
@app.callback(Output('page-1-content', 'children'),
              [Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return None

# Tab 2 callback
@app.callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])
def page_2_radios(value):
    return None

# Tab 3 callback
@app.callback(Output('page-3-content', 'children'),
              [Input('page-3-slider', 'value')])
def page_3_slider(value):
    return None

# Tab 4 callback
@app.callback(Output('page-4-content', 'children'),
              [Input('page-4-slider', 'value')])
def page_4_slider(value):
    return None

# Tab 5 callback
@app.callback( Output('page-5-content', 'children'),
              [Input('page-5-slider', 'value')])
def page_5_slider(value):
    return None

# Tab 6 callback
@app.callback( Output('page-6-content', 'children'),
              [Input('page-6-slider', 'value')])
def page_6_slider(value):
    return None

# use ? keep ? 
# Suppress errors (tabs)
# app.config['suppress_callback_exceptions'] = True

#------------------------------------------------------------------------------------------------

# --- Deploy ---
if __name__ == '__main__':
    app.run_server(debug=True)

# if __name__ == '__main__':
#     app.run_server(debug=True, use_reloader=False)

# - Add anything else ? - 
#    + abc 





