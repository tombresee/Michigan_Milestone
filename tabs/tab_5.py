import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


# tab_5_layout = html.Div([
#     html.H5('Temporary'),
#     html.Div([
#         html.Div([
#             html.H6('Select one:'),
#             dcc.Slider(
#                 id='page-5-slider',
#                 min=1,
#                 max=8,
#                 step=0.1,
#                 marks={i:str(i) for i in range(1, 9)},
#                 value=5,
#             ),
#         ], className='four columns'),
#         html.Div([
#             html.H6(id='page-5-content')
#         ], className='eight columns'),
#     ], className='twelve columns'),
# ], className='twelve columns')



########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'
#  githublink='https://github.com/austinlasseter/flying-dog-beers'
#  sourceurl='https://www.flyingdog.com/beers/'


########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


tab_5_layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    )])







