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

tab_6_layout = html.Div(className='row',children=[
                        html.Div(className='col-md-12',children=[
                            html.Div(className='box',children=[
                                html.Div(className='box-header with-border',children=[
                                    html.H3(className='box-title',children='Background')
                                ]),
                                html.Div(className='box-body',children=[
                                    html.P("Paragraph I"),
                                        html.P("The following additional Python libaries are used by this dashboard:"),
                                    html.P(
                                        html.Ul(children=[
                                            html.Li(html.A("Pandas", href='https://pypi.org/project/pandas/', target="_blank")),
                                            html.Li(html.A("Numpy", href='https://pypi.org/project/numpy/', target="_blank")),
                                            html.Li(html.A("Plotly", href='https://plotly.com/', target="_blank")),
                                            html.Li(html.A("Matplotlib", href='https://matplotlib.org/', target="_blank"))
                                        ])
                                    ),

                                    html.P("This work is a collaboration of the following individuals:"),
                                    html.P(
                                        html.Ul(children=[
                                            html.Li(html.A(href='https://github.com/tombresee',children="Tom Bresee", target="_blank")),
                                            html.Li(html.A(href='https://github.com/tombresee',children="Michael Phillips", target="_blank")),
                                        ])
                                    ),
                                    

                                    html.P(children=[
                                        "For the full report of this sensor analysis, please ",
                                        html.A(href='https://mads-hatters.github.io/',children="Click Here", target="_blank"),
                                        ". The code for this dashboard and the report are open source under the MIT license and can be found ",
                                        html.A(href='https://github.com/tombresee',children="Here", target="_blank"),
                                    ]),
                                    
                                ])
                            ])
                        ])
                    ])


