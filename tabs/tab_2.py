
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math
import os
import datetime

AWS_ACCESS_KEY_ID = os.environ.get("S3KEY")
AWS_SECRET_ACCESS_KEY = os.getenv("S3SECRET")

nodesdf = pd.read_csv('s3://wolverine-tomahawk/aot/nodes.csv',storage_options={
                      "key":AWS_ACCESS_KEY_ID,
                      "secret":AWS_SECRET_ACCESS_KEY})
nodesdf['implemented'] = 'No'
nodesdf.index = nodesdf['node_id']
nodes=['001e06107e5d',
     '001e0610b9e5',
     '001e0610b9e7',
     '001e0610ba13',
     '001e0610ba15',
     '001e0610ba16',
     '001e0610ba18',
     '001e0610ba3b',
     '001e0610ba46',
     '001e0610ba8b',
     '001e0610ba8f',
     '001e0610bbe5',
     '001e0610bbf9',
     '001e0610bbff',
     '001e0610bc07',
     '001e0610bc10',
     '001e0610ea5a',
     '001e0610ee33',
     '001e0610ee41',
     '001e0610eef4',
     '001e0610ef26',
     '001e0610ef29',
     '001e0610f02f',
     '001e0610f668',
     '001e0610f730',
     '001e0610f8f4']
for activenode in nodes:
    nodesdf.loc[activenode,'implemented'] = 'Yes'
nodesdf['start_timestamp'] = pd.to_datetime(nodesdf['start_timestamp'])

sensorsdf = pd.read_csv('s3://wolverine-tomahawk/aot/sensors_data.csv',storage_options={
                      "key":AWS_ACCESS_KEY_ID,
                      "secret":AWS_SECRET_ACCESS_KEY})
subsystems = sensorsdf['subsystem'].unique()
sensors = sensorsdf['sensor'].unique()
parameters = sensorsdf['parameter'].unique()

fig = px.scatter_mapbox(
    nodesdf,
    lat='lat',
    lon='lon',
    color='implemented',
    hover_name='node_id',
    zoom=9,
    hover_data=['address','description'],
    mapbox_style='open-street-map')
fig.update_layout(clickmode='event+select')
fig.update_traces(marker_size=10)

tab_2_layout = html.Div([
    html.Div([
        html.H1('Sensor Data'),
        ],style={
        'text-align':'center'}
    ),
    html.Br(),
    html.Div([
        html.Div([
            html.H4('Date Range'),
            ]
        ,style = {'text-align':'center','width':'25%'}),
        html.Div([
            html.H4('Subsystem'),
            ]
        ,style = {'text-align':'center','width':'25%'}),
        html.Div([
            html.H4('Sensor'),
            ]
        ,style = {'text-align':'center','width':'25%'}),
        html.Div([
            html.H4('Parameter'),
            ]
        ,style = {'text-align':'center','width':'25%'}),
        ],className='row'
    ),
    html.Div([
        html.Div([
            dcc.DatePickerRange(
                id='my-date-picker-range',
                min_date_allowed=datetime.date(2018, 1, 1),
                max_date_allowed=datetime.datetime.now(),
                initial_visible_month=datetime.date(2018, 1, 1),
                start_date=datetime.date(2018,1,1),
                end_date=datetime.datetime.now()
                )
            ],
            style = {'text-align':'center','width':'25%','padding-right':'30px','padding-left':'30px'}
            ),
        html.Div([
            dcc.Dropdown(
                id='subsystems-dropdown',
                options=[{'label': i, 'value': i} for i in subsystems],
                ),
            ],
            style = {'text-align':'center','width':'25%','padding-right':'30px','padding-left':'30px'}
            ),
        html.Div([
            dcc.Dropdown(
                id='sensor-dropdown',
                ),
            ],
            style = {'text-align':'center','width':'25%','padding-right':'30px','padding-left':'30px'}
            ),
        html.Div([
            dcc.Dropdown(
                id='parameter-dropdown',
                ),
            ],
            style = {'text-align':'center','width':'25%','padding-right':'30px','padding-left':'30px'}
            ),
        ],
        className='row'
    ),
    html.Br(),
    html.Div([
        html.Div([
            html.H4('Sensor Locations'),
            ]
        ,style = {'text-align':'center','width':'50%'}),
        html.Div([
            html.H4('Sensor Data'),
            ]
        ,style = {'text-align':'center','width':'50%'}),
        ],className='row'
    ),
    html.Div([
        dcc.Graph(id='sensorLoc',figure=fig, style={'width':'50%','height':'700px'}),
        dcc.Graph(id='click-data', style={'width':'50%','height':'700px'}),
        ],
        className='row'
    )

])

