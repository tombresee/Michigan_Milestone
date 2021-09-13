
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


tab_1_layout = html.Div([
    html.H4('Introduction'),
    html.Div([

        html.Div([
            html.H6('Select one:'),

            html.P("The following additional Python libaries are used by this dashboard:"),


            html.P(children=["This dashboard also uses CersiumJS for some of the visualziations.  ",
                                        html.A("CesiumJS", href='https://cesium.com/cesiumjs/', target="_blank"),
                                        " is an open source JavaScript library for creating a 3D map of the earth and creates interactive animations using their CZML language written in JSON."
                                    ]),
                                    

            # may need to put that back in 
            dcc.Dropdown(
                id='page-1-dropdown',
                options=[{'label': i, 'value': i} for i in ['A', 'B', 'C']],
                value='burger',
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
