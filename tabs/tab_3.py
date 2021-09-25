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
    html.H2('Unsupervised Machine Learning - Anomaly Detection using DBSCAN and Isolation Forest'),
    html.Div([
        html.Div([
            html.H6('''Prior to starting this analysis, Michael had an idea of where anomalies may
            be due to him living in Chicago during a large portion of this time frame. At the end of
            January 2019, there was a Polar Vortex that hit the area. '''),
            html.A('Polar Vortex Link Here',href='https://en.wikipedia.org/wiki/January%E2%80%93February_2019_North_American_cold_wave#:~:text=In%20late%20January%202019%2C%20a,killing%20at%20least%2022%20people.&text=As%20a%20result%2C%20February%202019,on%20record%20in%20these%20regions.'),
            html.H6('''
            This caused a drastic drop in temperatures which led to record lows during the period.
            To ensure that our model was working correctly, we felt that this instance must 
            show up in our anomalies.''')
        ]),
        html.Div([
            html.H6('To start, we took a look at the Chicago temperature data from January 1, 2019 to March 1, 2019:'),
            html.Img(src='assets/single_subsensor_temp_data_plotted_two_months.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('After we had our temperature data, we used DBSCAN to detect anomalies:'),
            html.Img(src='assets/dbr_1.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('Anomalies were detected and we see that the model picked up the Polar Vortex:'),
            html.Img(src='assets/pow.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('We tweaked the model a touch by changing eps from .01 to .003. This identified more anomalies:'),
            html.Img(src='assets/pow_tuned_2.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('Here, we take a deeper look into the temperature data from January 30th to 31st. Nearly the entire time frame is an anomaly:'),
            html.Img(src='assets/dbr_1_r2e.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('We also took a look at the anomalous high that took place on January 5th:'),
            html.Img(src='assets/dbr_1_r1.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            
            html.Br(),
            html.H6('Using isolation forest anomaly detection mechanisms, we were able to produce the following plots.'),
            html.Div([
            html.H6('Examining the following '),
            html.A(' data',href='https://rawcdn.githack.com/tombresee/SensorAnalysis/ceeb9b02bad78c4e138f6a451b62c1943764e145/ENTER/results/iso_forest_base_data_plotted.html'),
            html.H6(', we were able to create a histogram:'),
            ],className='row'),
            html.Img(src='assets/histogram_isolation_forest.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('We were then able to process the data with isolation forest to determine the individual data point anomaly scores, which when plotted on the following graph, show us the points that are associated as anomalies and those that were not:'),
            html.Img(src='assets/histogram_anomaly_scores_isolation_forest.png',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('After leveraging the isolation forest to calculate outliers based on the contamination percentage, we were able to plot all data and anomalies for over a year of data:'),
            html.Img(src='assets/iso_forest_final_AD_plotted_2.svg',height='400px',width='1200px')
        ], className='four columns'),
        html.Div([
            html.Br(),
            html.H6('NOTE - We have also uploaded a true interactive plotly-based graph of the anomalies and data, to be stored at the following '),
            html.A('here.',href='https://rawcdn.githack.com/tombresee/SensorAnalysis/ceeb9b02bad78c4e138f6a451b62c1943764e145/ENTER/results/isolation_forest_final_AD_plotted_superhighres.html')
        ], className='row'),
        
    ], className='twelve columns'),
], style={'margin-right':'60px','margin-left':'60px'})