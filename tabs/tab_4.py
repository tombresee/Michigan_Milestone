import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math





tab_4_layout = html.Div([
    html.H5('Machine Learning II'),
    html.Div([
        html.Div([
            html.H6('Select one:'),
            dcc.Slider(
                id='page-4-slider',
                min=1,
                max=8,
                step=0.1,
                marks={i:str(i) for i in range(1, 9)},
                value=5,
            ),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-4-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')