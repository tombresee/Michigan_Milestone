
# core libraries 
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
from tabs import tab_1
from tabs import tab_2
from tabs import tab_3




########### Define variables ########### 

myheading1 = 'Sensor Analysis - AoT Cluster'
# any way of making this font smaller ? 

tabtitle = 'Array_of_Things Analysis'

sourceurl = 'https://dash.plot.ly/dash-core-components/tabs'
# what does this do ? 

# original code:  
# githublink = 'https://github.com/austinlasseter/dash-multitab-simple'
githublink = 'https://github.com/tombresee/Michigan_Milestone'



########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle
app.config['suppress_callback_exceptions'] = True



########### Set up the layout ###########

app.layout = html.Div([
    html.H3(myheading1),
    dcc.Tabs(id="tabs-example", value='tab-1-example',
            children=[
                dcc.Tab(label='Introduction', value='tab-1-example'),
                dcc.Tab(label='Analysis', value='tab-2-example'),
                dcc.Tab(label='Machine Learning', value='tab-3-example'),
    ]),


    html.Div([
        html.Div(id='tabs-content-example'),
    ], className='twelve columns',
        style={'marginBottom': 50, 'marginTop': 25}),


    html.Div([
        html.A('Code on Github', href=githublink),
        html.Br(),
        html.A("Data Source", href=sourceurl),
    ], className='twelve columns',
        style={'textAlign':'right',
                'fontColor':'#FFFFFF',
                'backgroundColor':'#D3D3D3',})
])




@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])

# this is the tab definitions 
def render_content(tab):
    if tab == 'tab-1-example':
        return tab_1.tab_1_layout
    elif tab == 'tab-2-example':
        return tab_2.tab_2_layout
    elif tab == 'tab-3-example':
        return tab_3.tab_3_layout



# Tab 1 callback
@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)



# Tab 2 callback
@app.callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)


# Tab 3 callback
@app.callback(Output('page-3-content', 'children'),
              [Input('page-3-slider', 'value')])
def page_3_slider(value):
    return f'You have selected "{str(value)}"'




############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
