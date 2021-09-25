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



tab_3_layout = html.Div([
    html.H1('Unsupervised Machine Learning - Anomaly Detection using DBSCAN'),
    html.Div([
        html.Div([
            html.H6('''Prior to starting this analysis, Michael had an idea of where anomalies may
            be due to him living in Chicago during a large portion of this time frame. At the end of
            January 2019, there was a Polar Vortex that hit the area. 
            Link Here: https://en.wikipedia.org/wiki/January%E2%80%93February_2019_North_American_cold_wave#:~:text=In%20late%20January%202019%2C%20a,killing%20at%20least%2022%20people.&text=As%20a%20result%2C%20February%202019,on%20record%20in%20these%20regions.
            This caused a drastic drop in temperatures which led to record lows during the period.
            To ensure that our model was working correctly, we felt that this instance must 
            show up in our anomalies.''')
        ]),
        html.Div([
            html.H6('To start, we took a look at the Chicago temperature data from January 1, 2019 to March 1, 2019.'),
            html.Img(src='assets/single_subsensor_temp_data_plotted_two_months.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('After we had our temperature data, we used DBSCAN to detect anomalies'),
            html.Img(src='assets/dbr_1.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('Anomalies were detected and we see that the model picked up the Polar Vortex'),
            html.Img(src='assets/pow.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('We tweaked the model a touch by changing eps from .01 to .003.'),
            html.Img(src='assets/pow_tuned_2.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('Here, we take a deeper look into the temperature data from January 30th to 31st. Nearly the entire time frame is an anomaly.'),
            html.Img(src='assets/dbr_1_r2e.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('We also took a look at the anomalous high that took place on January 5th.'),
            html.Img(src='assets/dbr_1_r1.png',height='400px',width='1200px')
        ], className='four columns'),
        
        
        
        
    ], className='twelve columns'),
], style={'margin-right':'60px','margin-left':'60px'})