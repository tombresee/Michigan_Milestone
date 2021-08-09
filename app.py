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
mytitle='ML Tactics'
tabtitle='sensor_ML'
myheading='Sensor Data Analysis'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

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


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    
    html.H3(myheading),

    html.H4('Tactics for ML'),

    # dcc.Graph(
    #     id='flyingdog',
    #     figure=beer_fig
    # ),
    
    html.A('Code on Github', href=githublink),
    
    html.Br(),
    
    html.A('Data Source', href=sourceurl),
    
    ])



if __name__ == '__main__':
    app.run_server()





#################  ORIGINAL TRYING CODE #########

# import core libraries 
# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output, State
# import plotly.graph_objs as go


# # import specific pages
# from oc_dash_tab_home import homepage
# tab_home = homepage()


# ########### Define your variables
# beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
# ibu_values=[35, 60, 85, 75]
# abv_values=[5.4, 7.1, 9.2, 4.3]
# color1='darkred'
# color2='orange'
# mytitle='Beer Comparison'
# tabtitle='beer!'
# myheading='Flying Dog Beers'
# label1='IBU'
# label2='ABV'
# githublink='https://github.com/austinlasseter/flying-dog-beers'
# sourceurl='https://www.flyingdog.com/beers/'



# #  DO I NEED THIS ????
# #  githublink='https://github.com/tombresee/Michigan_Milestone'
# #  githublink='https://github.com/austinlasseter/flying-dog-beers'
# #  sourceurl='https://www.flyingdog.com/beers/'



# menu_tabs_styles = {
#     'borderBottom': '1px solid #222d32',
#     'padding': '0px 0px 0px 0px',
#     'height': '46px',
#     'width':'100%',
#     'border': '1px solid',
#     'border-color' : '#222d32',
#     'width': '230px'
# }


# menu_tab_style = {
#     'border': '1px solid',
#     'border-color' : '#222d32',
#     'backgroundColor': '#222d32',
#     'padding': '15px 5px 15px 15px',
#     'display': 'block',
#     'font-size': '14px',
#     'color': '#b8c7ce',
#     'text-align': 'left',
#     'font-family': "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
# }


# menu_tab_selected_style = {
#     'border': '1px solid',
#     'border-color' : '#2c3b41',
#     'backgroundColor': '#2c3b41',
#     'padding': '15px 5px 15px 15px',
#     'display': 'block',
#     'font-size': '14px',
#     'color': 'white',
#     'text-align': 'left',
#     'font-family': "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
# }



# #-------------------------------------------------------------------------------------
# # Generate the dashboard (w/ tabs)
# #-------------------------------------------------------------------------------------


# ########### Initiate the app/dashboard 

# # external_stylesheets = ['http://code.ionicframework.com/ionicons/2.0.0/css/ionicons.min.css',
# #                 'https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css',
# #                 'https://cesium.com/downloads/cesiumjs/releases/1.76/Build/Cesium/Widgets/widgets.css']


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# app = dash.Dash(__name__, 
#     title='Sensor Analysis', 
#     external_stylesheets=external_stylesheets)


# server = app.server



# ################ app.title=tabtitle




# # Setup the main dashboard with navigation sidebar
# # app.layout = html.Div(className='skin-blue', children=[
# #     html.Div(className='wrapper',children=[
# #         html.Header(className='main-header',children=[
# #             html.A(className='logo',children=[
# #                 html.B(children='Orbital Congestion')
# #             ]),
# #             html.Nav(className='navbar navbar-static-top',role='navigation', children=[
# #                 html.A(className='sidebar-toggle', role="button", **{'data-toggle':'offcanvas'}, 
# #                        children=[
# #                     html.Span(className='sr-only',children='Toggle navigation')
# #                 ])
# #             ])
# #         ]),
# #         html.Aside(className='main-sidebar',children=[
# #             html.Section(className='sidebar',children=[
# #                 html.Div(className='user-panel', children=[
# #                     html.Div(className='pull-left image',children=[
# #                         html.Img(className='img-circle',src='./assets/hat.png')
# #                     ]),
# #                     html.Div(className='pull-left info',children='MADS Hatters')
# #                 ]),
# #                 html.Ul(className='sidebar-menu',children=[
# #                     html.Li(className='header', children='MAIN NAVIGATION'),
# #                     html.Li(children=[
# #                         dcc.Tabs(id="menu-tabs", vertical=True,
# #                                  parent_style={'float': 'left'},
# #                                  value='menu-item-home',
# #                                  className="treeview-menu",
# #                                  style=menu_tabs_styles,
# #                                  children=[
# #                             dcc.Tab(label='Home',
# #                                     value='menu-item-home',
# #                                     style=menu_tab_style,
# #                                     selected_style=menu_tab_selected_style),
# #                                         ]),
# #                         html.Div(id='ui_dummy', style={'display': 'none'}),
# #                         html.Div(id='csk', style={'display': 'none'}, children="ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnFkR2tpT2lJd05tSXdORGN5WkMwNE5tUTBMVFExTnpRdFltVTNOeTAxWVRabFpUVTRNRFUzWkRVaUxDSnBaQ0k2TkRBeE5ESXNJbWxoZENJNk1UWXdPRE0xTkRZNE9IMC5uT1pBQ291ay0tZnhQX2V1cXRnRmt3d05TMi02NEJaODFBTWVNbzlwZ1lj")
# #                     ])
# #                 ])
# #             ])
# #         ]),
# #         html.Div(id='page-content', className='content-wrapper')
# #     ])
# # ])


# ########### Set up the layout
# app.layout = html.Div(children=[
#     html.H1(myheading),
#     dcc.Graph(
#         id='flyingdog',
#         figure=beer_fig
#     ),
#     html.A('Code on Github', href=githublink),
#     html.Br(),
#     html.A('Data Source', href=sourceurl),
#     ]
# )



# if __name__ == '__main__':
#     app.run_server(debug=True)

