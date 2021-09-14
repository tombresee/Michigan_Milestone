
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_1_layout = html.Div([
    html.H5('Introduction'),
    html.Div([
        html.Div([
            html.H6('Introduction:'),
        ], className='four columns'),
        html.Div([
            html.H6(id='page-2-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')

