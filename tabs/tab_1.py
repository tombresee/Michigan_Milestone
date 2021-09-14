
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_1_layout = html.Div([
    html.H5('Introduction'),
    html.Div([
        html.Div([
            html.H6('Select one:'),

                                  html.Div(className='box-body',children=[
                                    html.P("Space, and more specifically low-earth orbit, is about to get a whole lot busier and this is making many concerned. At present, there are about 2,000 operational satellites in low-earth orbit and more than double that in defunct satellites. But last year in October, SpaceX requested permission to launch 30,000 Starlink satellites into low-earth orbit. This is in addition to the 12,000 that already received approval. These satellites have already begun interrupting astronomical observations, creating light pollution and increasing collision risks in an environment where a collision could trigger a chain reaction which not only endangers current and future satellites but also human lives."),
                                    html.P(children=[
                                        "This dashboard consists of a few demonstrations of how congested space has become and where it is going.  This dashboard website is written in Python using ",
                                        html.A(children="Plotly Dash",href="https://plotly.com/dash/", target="_blank"),
                                        ".  The layout for the dashboard comes from ",
                                        html.A(children="AdminLTE", href="https://adminlte.io/", target="_blank"),
                                        ", a free open-source implemenation of Bootstrap. The data used to compile these visuals come from the following sources:"
                                    ]), 
                                    

            dcc.Dropdown(
                id='page-1-dropdown',
                options=[{'label': i, 'value': i} for i in ['burger', 'fries', 'milkshake']],
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