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
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import math

tab_1_layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Welcome to Chicago AOT Sensor Analysis'),
            html.H2('By: Tom Bresee and Michael Phillips'),
            html.Br(),
            html.H6("""As a continuing investigation into the realm of real-world sensor analytics,
                we focus on a massive Internet of Things (IoT) cluster known as the Array of Things,
                hosted in the city of Chicago and part of a continuing effort for smart city enablement. 
                It is expected that smart city initiatives will progress, 
                as Chicago takes the lead in deploying it's AoT cluster. 
                In recent years, the smart city concept has gone from theoretical to actual live production networks.
                We leverage unsupervised machine learning tactics to dive deeper into a large set of this extensive AoT sensor data. 
                The Array of Things (AoT) Chicago sensor network is an extensive cluster with software-defined units performing multiple sensing duties,
                as a true predecesor to a 'smart city'. We have Folium (python geo-mapper) to plot all 126 current sensor node locations on the Dashboard Tab, 
                where clicking or hovering on the node shows its address and unique node_id. 
                This project was initially funded by the National Science Foundation to design and
                build a new kind of national-scale reusable cyberinfrastructure to enable AI at the edge. 
                The project leverages open source hardware/software developed by Argonne National Laboratory.
                """),
            html.Br(),
            html.H6("""
                The IoT sector is expected to be a billion dollar market as advances in computing,
                lower cost sensors, and 5G cellular technology progress. We anticipate more and more
                IoT-related AI research is done into subjects such as sensor parameter key performance 
                indicator (KPI) anomaly detection, sensor predictive maintenance, sensor malfunction estimation, 
                and sensor status. Our investigation revolved around clustering sensor data KPI values into 
                'normal' vs 'anomalous', as well as comparing individual cluster node data with other nodes. 
                Specific unsupervised learning techniques involved are isolation forest, DBSCAN, and clustering. 
                Part of the motivation for this project is the fact that this dataset represents a huge real-world
                non-synthetic view of sensor IoT program. Many datasets from UCI or Kaggle are synthetic or run 
                under laboratory-like conditions, however this dataset represents insight into how IoT sensors 
                really perform, the good, the bad, the practical...
                One of our goals is to create code to cluster streams of time-series data into normal, non-normal, and anomalous.")
                """),
            html.Br(),
            html.H6('The dataset can be found at https://www.mcs.anl.gov/research/projects/waggle/downloads/datasets/index.php')
        ], className='four columns'),
    ], className='twelve columns'),
], style={'margin-right':'60px','margin-left':'60px'})

