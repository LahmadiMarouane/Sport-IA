from dash import Dash, dcc, html, Input, Output, callback
import pandas as pd
import plotly.graph_objs as go
import radar_chart
import chord
import dash_bootstrap_components as dbc
from holoviews.plotting.plotly.dash import to_dash

from holoviews import opts, dim
import holoviews as hv
import base64
import flask
app = Dash(
    
    __name__, suppress_callback_exceptions=True)

server = app.server

df = pd.read_excel ('FINALFINAL.xlsx')
df2 = pd.read_excel ('FINALFINALDetail.xlsx')
df3 = pd.read_excel ('Transfert_dollar3.xlsx',
            sheet_name = 'DATA',
            usecols=['Team In','Team Left'])

figure=chord.chord_diagram(df3)

#components = to_dash(app, [figure], graph_class = 'graph1')
#print(type(components))
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
    
])

fig = go.Figure()
index_page = html.Div([
    
    html.H1(className='middle' , children=[' Sport IA - Comment les transferts vont impacter les équipes de la MLS en 2022 ?']),
    dcc.Link('Historique des transferts', href='/page-1',className='link1'),


    dcc.Link('Impact des transferts sur les clubs ', href='/page-2', className='link2'),

    dcc.Link('Comparaison entre les clubs ', href='/page-3',className='link3'),
])


d1= {'Atlanta United FC' : 'Atlanta_Utd_2022','Austin FC' : 'Austin_FC_2022','CF Montréal' : 'CF_Montreal_2022','Charlotte FC' : 'Charlotte_FC_2022','Chicago Fire FC' : 'Chicago_Fire_2022','Colorado Rapids' : 'Colorado_Rapids_2022','Columbus Crew' : 'Columbus_Crew_2022','D.C. United' : 'D.C._United_2022','FC Cincinnati' : 'FC_Cincinnati_2022','FC Dallas' : 'FC_Dallas_2022','Houston Dynamo FC' : 'Houston_Dynamo_2022','Inter Miami CF' : 'Inter_Miami_2022','LA Galaxy' : 'LA_Galaxy_2022','Los Angeles FC' : 'Los_Angeles_FC_2022','Minnesota United FC' : 'Minnesota_Utd_2022','Nashville SC' : 'Nashville_2022','New England Revolution' : 'New_England_2022','New York City FC' : 'NYCFC_2022','New York Red Bulls' : 'NY_Red_Bulls_2022','Orlando City SC' : 'Orlando_City_2022','Philadelphia Union' : 'Philadelphia_2022','Portland Timbers' : 'Portland_Timbers_2022','Real Salt Lake' : 'Real_Salt_Lake_2022','San Jose Earthquakes' : 'San_Jose_2022','Seattle Sounders FC' : 'Seattle_2022','Sporting Kansas City' : 'Sporting_KC_2022','Toronto FC' : 'Toronto_FC_2022','Vancouver Whitecaps FC' : 'Vancouver_2022'}
d2 = {'Atlanta United FC' : 'Atlanta_Utd_2021','Austin FC' : 'Austin_FC_2021','CF Montréal' : 'CF_Montreal_2021','Charlotte FC' : 'Charlotte_FC_2021','Chicago Fire FC' : 'Chicago_Fire_2021','Colorado Rapids' : 'Colorado_Rapids_2021','Columbus Crew' : 'Columbus_Crew_2021','D.C. United' : 'D.C._United_2021','FC Cincinnati' : 'FC_Cincinnati_2021','FC Dallas' : 'FC_Dallas_2021','Houston Dynamo FC' : 'Houston_Dynamo_2021','Inter Miami CF' : 'Inter_Miami_2021','LA Galaxy' : 'LA_Galaxy_2021','Los Angeles FC' : 'Los_Angeles_FC_2021','Minnesota United FC' : 'Minnesota_Utd_2021','Nashville SC' : 'Nashville_2021','New England Revolution' : 'New_England_2021','New York Red Bulls' : 'NY_Red_Bulls_2021','New York City FC' : 'NYCFC_2021','Orlando City SC' : 'Orlando_City_2021','Philadelphia Union' : 'Philadelphia_2021','Portland Timbers' : 'Portland_Timbers_2021','Real Salt Lake' : 'Real_Salt_Lake_2021','San Jose Earthquakes' : 'San_Jose_2021','Seattle Sounders FC' : 'Seattle_2021','Sporting Kansas City' : 'Sporting_KC_2021','Toronto FC' : 'Toronto_FC_2021','Vancouver Whitecaps FC' : 'Vancouver_2021'}
L = ['Vancouver Whitecaps FC','Toronto FC','Sporting Kansas City', 'Seattle Sounders FC','San Jose Earthquakes','Real Salt Lake','Portland Timbers','Philadelphia Union','Orlando City SC','New York Red Bulls','New York City FC','New England Revolution','Nashville SC','Minnesota United FC','Los Angeles FC','LA Galaxy','Inter Miami CF','Houston Dynamo FC','FC Dallas','FC Cincinnati','D.C. United','Columbus Crew','Colorado Rapids','Chicago Fire FC','Charlotte FC','CF Montréal','Austin FC','Atlanta United FC']

image_filename = 'chord.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

page_1_layout = html.Div([
    html.H1('Historique des transferts'),
    html.Br(),html.Br(),html.Br(),html.Br(),
    
    #dcc.Graph(id = "graph1", figure=components.children ),
    #html.Div(components.children),
    html.Img(className = 'img', src='data:image/png;base64,{}'.format(encoded_image.decode())),
    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Home', href='/',className='link1'),

    dcc.Link('Impact des transferts sur les clubs ', href='/page-2', className='link2'),

    dcc.Link('Comparaison entre les clubs ', href='/page-3',className='link3'),
])




page_2_layout = html.Div([
    html.H1('Impact des transferts sur les clubs'),
    #dcc.Link('Home', href='/', className='link'),
    html.Br(),
    html.Br(),
    html.Br(),
    dcc.Dropdown(L, '', id='page-2-dropdown'),
    html.Div(id='page-2-content'),
    html.Br(),
    html.Br(),
    dcc.Graph(id = "selected-data3", figure=radar_chart.radar_chart(df, "CF_Montreal_2022", "CF_Montreal_2021")),
    html.Br(),
    html.Br(),html.Br(),
    html.H1('Comparaison Detaillée'),
    html.Br(),html.Br(),
    dcc.Graph(id = "selected-data4", figure=radar_chart.radar_det(df2, "CF_Montreal_2022", "CF_Montreal_2021") ),
    dcc.Link('Historique des transferts', href='/page-1',className='link2'),

    dcc.Link('Home ', href='/', className='link1'),

    dcc.Link('Comparaison entre les clubs ', href='/page-3',className='link3'),
   
])

@callback(Output('selected-data3', 'figure'),
                Output('selected-data4', 'figure'),
              [Input('page-2-dropdown', 'value')]
              )
def page_2_radios(value):
    if value == '': 
        return radar_chart.radar_chart(df, "CF_Montreal_2022", "CF_Montreal_2021"),radar_chart.radar_det(df2, "CF_Montreal_2022", "CF_Montreal_2021")
    else:
        fig1 = radar_chart.radar_chart(df, d1[value], d2[value])
        fig2 = radar_chart.radar_det(df2, d1[value], d2[value])
        return fig1, fig2
page_3_layout = html.Div([
   html.H1('Comparaison entre les clubs'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(className='dropdown',
    children=[
    dcc.Dropdown(L, '', id='page-3-dropdown'),
    dcc.Dropdown(L, '', id='page-3-dropdown2')]),
    html.Div(id='page-3-content'), 
    html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
    dcc.Graph(id = "selected-data", figure=radar_chart.radar_chart(df, "CF_Montreal_2022", "CF_Montreal_2022")),
    html.Br(),html.Br(),
    html.H1('Comparaison Detaillée'),
    html.Br(),html.Br(),
    dcc.Graph(id = "selected-data2", figure=radar_chart.radar_det(df2, "CF_Montreal_2022", "CF_Montreal_2022") ),
    dcc.Link('Historique des transferts', href='/page-1',className='link2'),

    dcc.Link('Impact des transferts sur les clubs ', href='/page-2', className='link3'),

    dcc.Link('Home ', href='/',className='link1'),
])

@callback(Output('selected-data', 'figure'),
                Output('selected-data2', 'figure'),
              [Input('page-3-dropdown', 'value')],
              [Input('page-3-dropdown2', 'value')])
def page_3_radios(value1, value2):
    if value1 == '' or value2 =='' : 
        return radar_chart.radar_chart(df, "CF_Montreal_2022", "CF_Montreal_2022"),radar_chart.radar_det(df2, "CF_Montreal_2022", "CF_Montreal_2022")
    else:
        fig1 = radar_chart.radar_chart(df, d1[value1], d1[value2])
        fig2 = radar_chart.radar_det(df2, d1[value1], d1[value2])
        return fig1, fig2



# Update the index
@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here

if __name__ == '__main__':
    app.run_server(debug=True)