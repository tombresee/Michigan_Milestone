
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_1_layout = html.Div([
    html.H5('Introduction'),
    html.Div([
        html.Div([
            html.H6('Select one:'),

                                    html.P(
                                        html.Ul(children=[
                                            html.Li(children=[
                                                html.A(href='https://www.space-track.org/',children="Space-Track.org", target="_blank"),
                                                " - For providing the TLE data",
                                            ]),
                                            html.Li(children=[
                                                html.A(href='https://celestrak.com/SOCRATES/',children="SOCRATES", target="_blank"),
                                                " - For upcoming satellite collision probability detection",
                                            ]),
                                            html.Li(children=[
                                                html.A(href='https://ntrs.nasa.gov/',children="NASA's History of On-Orbit Satellite Fragmentations", target="_blank"),
                                                " - For satellite breakup dates",
                                            ]),
                                        ])
                                    )


            # dcc.Dropdown(
            #     id='page-1-dropdown',
            #     options=[{'label': i, 'value': i} for i in ['burger', 'fries', 'milkshake']],
            #     value='burger',
            #     style = dict(
            #                 width = '70%',
            #                 display = 'inline-block',
            #                 verticalAlign = "middle"
            #                 ),
            # ),


        ], className='four columns'),
     

        html.Div([
            html.H6(id='page-1-content')
        ], className='eight columns'),
    ], className='twelve columns'),
], className='twelve columns')

