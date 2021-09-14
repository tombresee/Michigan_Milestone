import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='t-SNE Visualization'
label1='IBU'
label2='ABV'
#  githublink='https://github.com/austinlasseter/flying-dog-beers'
#  sourceurl='https://www.flyingdog.com/beers/'


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

tab_6_layout = html.Div(children=[
    html.H6(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    )])
