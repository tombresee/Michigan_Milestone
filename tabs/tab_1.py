# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output

# tab_1_layout = html.Div([
#     html.H5('Introduction'),
#     html.Div([
#         html.Div([
#             html.H6('Select one:'),
#             dcc.RadioItems(
#                 id='page-1-radios',
#                 options=[{'label': i, 'value': i} for i in ['Sensor', 'Node', 'KPI']],
#                 value='Orange',
#                 style = dict(
#                     width = '70%',
#                     display = 'inline-block',
#                     verticalAlign = "middle"
#                     ),
#             )
#         ], className='four columns'),
#         html.Div([
#             html.H6(id='page-1-content')
#         ], className='eight columns'),
#     ], className='twelve columns'),
# ], className='twelve columns')


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math

tab_1_layout = html.Div([
    html.H5('Introduction'),
    html.Div([
        html.Div([
            html.H6('Select'),
            dcc.RadioItems(
                id='page-1-radios',
                options=[{'label': i, 'value': i} for i in ['Sensor', 'Node', 'KPI']],
                value='Orange',
                style = dict(
                    width = '70%',
                    display = 'inline-block',
                    verticalAlign = "middle"
                    ),
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-1-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')

