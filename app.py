#------------------------------------------------------------------------------------------------

#  Project:    Sensor Analysis Milestone
#  Authors:    - 
#  Good Ref:   https://github.com/Techfitlab/youtube_project/blob/main/app.py
#  Ref dbc:    https://dash-bootstrap-components.opensource.faculty.ai/
#              https://dash-bootstrap-components.opensource.faculty.ai/docs/

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
import json
import os

AWS_ACCESS_KEY_ID = os.environ.get("S3KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("S3SECRET")
#
from tabs import tab_1
from tabs import tab_2
from tabs import tab_3

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
                external_stylesheets=[dbc.themes.BOOTSTRAP])  # this looks better i think 
                # commented out this code:   external_stylesheets=external_css)

server = app.server

app.title=tabtitle

app.config['suppress_callback_exceptions'] = True  # DO I NEED THIS ? 

#------------------------------------------------------------------------------------------------
# --- Set up the layout ---

# --- Review all of this --- 
menu_tabs_styles = {
    'borderBottom': '1px solid #222d32',
    'padding': '0px 0px 0px 0px',
    'height': '46px',
    'width':'100%',
    'border': '1px solid',
    'border-color' : '#222d32'
}
menu_tab_style = {
    'border': '1px solid',
    'border-color' : '#222d32',
    'backgroundColor': '#222d32',
    'padding': '15px 5px 15px 15px',
    'display': 'block',
    'font-size': '14px',
    'color': '#b8c7ce',
    'text-align': 'left',
    'font-family': "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
}
menu_tab_selected_style = {
    'border': '1px solid',
    'border-color' : '#2c3b41',
    'backgroundColor': '#2c3b41',
    'padding': '15px 5px 15px 15px',
    'display': 'block',
    'font-size': '14px',
    'color': 'white',
    'text-align': 'left',
    'font-family': "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
}


app.layout = html.Div([
    html.H4(myheading1),
    dcc.Tabs( id="tabs-example", 
              value='tab-1-example',

              children=[
               dcc.Tab(label='Introduction', 
                       value='tab-1-example'),
               dcc.Tab(label='Dashboard', value='tab-2-example'),
               dcc.Tab(label='Unsupervised Learning', value='tab-3-example')]),
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

@app.callback(
    Output('click-data', 'figure'),
    Input('sensorLoc', 'clickData'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    [Input("sensor-dropdown", "value"),
    Input("subsystems-dropdown", "value"),
    Input("parameter-dropdown","value")])

def display_click_data(clickData,start_date,end_date,sensor,subsystem,parameter):
    node = clickData['points'][0]['hovertext']
    df = pd.read_parquet('s3://wolverine-tomahawk/aot/HourlyData/node-'+node+'_hourly_mean.parquet.gzip',storage_options={
                      "key":AWS_ACCESS_KEY_ID,
                      "secret":AWS_SECRET_ACCESS_KEY})
    df = df[(df['subsystem']==subsystem)&(df['sensor']==sensor)&(df['parameter']==parameter)]
    df['timestamp']=pd.to_datetime(df['timestamp'])
    df['value_hrf']=df['value_hrf'].astype('float')
    df = df[(df['timestamp']>=pd.to_datetime(start_date)) & (df['timestamp']<=pd.to_datetime(end_date))]
    #df = df.groupby(pd.Grouper(key='timestamp',freq='D')).mean()
    sensorsdf = pd.read_csv('s3://wolverine-tomahawk/aot/sensors_data.csv',storage_options={
                      "key":AWS_ACCESS_KEY_ID,
                      "secret":AWS_SECRET_ACCESS_KEY})
    sensorsdf = sensorsdf[(sensorsdf['subsystem']==subsystem)&(sensorsdf['sensor']==sensor)&(sensorsdf['parameter']==parameter)]
    label = sensorsdf['hrf_unit'].unique()[0]
    fig = px.line(df,x='timestamp',y='value_hrf')
    fig.update_layout(title = "{} Data for Node: {}".format(parameter,node),
                      yaxis_title=label)
    return fig

@app.callback(
    Output("sensor-dropdown", "options"),
    Input("subsystems-dropdown", "value")
)
def update_options(search_value):
    sensorsdf = pd.read_csv('s3://wolverine-tomahawk/aot/sensors_data.csv',storage_options={
                      "key":AWS_ACCESS_KEY_ID,
                      "secret":AWS_SECRET_ACCESS_KEY})
    sensorsdf = sensorsdf[sensorsdf['subsystem']==search_value]
    sensors = sensorsdf['sensor'].unique()
    return [{'label': i, 'value': i} for i in sensors]

@app.callback(
    Output("parameter-dropdown", "options"),
    [Input("sensor-dropdown", "value"),
    Input("subsystems-dropdown", "value")]
)
def update_parameter_options(sensorvalue,subsystemsvalue):
    sensorsdf = pd.read_csv('s3://wolverine-tomahawk/aot/sensors_data.csv',storage_options={
                  "key":AWS_ACCESS_KEY_ID,
                  "secret":AWS_SECRET_ACCESS_KEY})
    sensorsdf = sensorsdf[(sensorsdf['subsystem']==subsystemsvalue)&(sensorsdf['sensor']==sensorvalue)]
    parameters = sensorsdf['parameter'].unique()
    return [{'label': i, 'value': i} for i in parameters]

# Tab 3 callback
@app.callback(Output('page-3-content', 'children'),
              [Input('page-3-slider', 'value')])
def page_3_slider(value):
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







# """
# This app creates a simple sidebar layout using inline style arguments and the
# dbc.Nav component.

# dcc.Location is used to track the current location, and a callback uses the
# current location to render the appropriate page content. The active prop of
# each NavLink is set automatically according to the current pathname. To use
# this feature you must install dash-bootstrap-components >= 0.11.0.

# For more details on building multi-page Dash applications, check out the Dash
# documentation: https://dash.plot.ly/urls
# """
# import dash
# import dash_bootstrap_components as dbc
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output

# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# # the style arguments for the sidebar. We use position:fixed and a fixed width
# SIDEBAR_STYLE = {
#     "position": "fixed",
#     "top": 0,
#     "left": 0,
#     "bottom": 0,
#     "width": "16rem",
#     "padding": "2rem 1rem",
#     "background-color": "#f8f9fa",
# }

# # the styles for the main content position it to the right of the sidebar and
# # add some padding.
# CONTENT_STYLE = {
#     "margin-left": "18rem",
#     "margin-right": "2rem",
#     "padding": "2rem 1rem",
# }

# sidebar = html.Div(
#     [
#         html.H2("Sidebar", className="display-4"),
#         html.Hr(),
#         html.P(
#             "A simple sidebar layout with navigation links", className="lead"
#         ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Home", href="/", active="exact"),
#                 dbc.NavLink("Page 1", href="/page-1", active="exact"),
#                 dbc.NavLink("Page 2", href="/page-2", active="exact"),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     style=SIDEBAR_STYLE,
# )

# content = html.Div(id="page-content", style=CONTENT_STYLE)

# app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname == "/":
#         return html.P("This is the content of the home page!")
#     elif pathname == "/page-1":
#         return html.P("This is the content of page 1. Yay!")
#     elif pathname == "/page-2":
#         return html.P("Oh cool, this is page 2!")
#     # If the user tries to reach a different page, return a 404 message
#     return dbc.Jumbotron(
#         [
#             html.H1("404: Not found", className="text-danger"),
#             html.Hr(),
#             html.P(f"The pathname {pathname} was not recognised..."),
#         ]
#     )


# if __name__ == '__main__':
#     app.run_server(debug=True)