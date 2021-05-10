import pandas as pd
import requests
import plotly.graph_objs as go
import dash
import dash_daq as daq
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from sidebar import *
import extras

external_stylesheets = [extras.theme]

countries = extras.vacc

app = dash.Dash(__name__, 
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/vaccine/')
app.layout = html.Div([
    html.Base(target="_parent"),
    navbar("Vaccine"),
    html.Div([
        dcc.Dropdown(
            id="countries",
            options=[{'label': name, 'value': name} for name in countries],
            value='India'
        ),
        html.H1(id="h")
    ]),
    dbc.Alert([
        html.Center(html.H5(id="Alert1txt"))
    ], color='info'),
    dbc.Row([
        dbc.Col([
            html.H4("Total Vaccinations"),
            daq.LEDDisplay(id="totvac", color="#66ff00", backgroundColor="#000000")], lg=4),
        dbc.Col([
            html.H4("People Vaccinated"),
            daq.LEDDisplay(id="pepvac", color="#66ff00", backgroundColor="#000000")], lg=4),
        dbc.Col([
            html.H4("Full Vaccinated People"),
            daq.LEDDisplay(id="pepfullvac", color="#66ff00", backgroundColor="#000000")], lg=4)
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(
                id='graph1'
        ), lg=6),
        dbc.Col(
            dcc.Graph(
                id='graph2'
        ), lg=6)
    ])
])

def gofig(self, x, y, name):
    self.add_trace(go.Scatter(x=x, y=y, name=name))

def upd_layout(fig):
    fig.update_layout(showlegend=False,
                      legend=dict(
                          font=dict(
                              color="white"
                          )
                      ),
                      margin=dict(
                          l=5,
                          r=5,
                          b=5,
                          t=0,
                          pad=0
                      ),
                      plot_bgcolor='#0f2537',
                      paper_bgcolor='#0f2537')
    fig.update_xaxes(tickangle=90, tickfont=dict(family='Rockwell', color='white'), rangeslider=dict(visible=True))
    fig.update_yaxes(tickfont=dict(family='Rockwell', color='white'))

def get_range(cases: list) -> list:
    diff = []
    start = 0
    for case in cases:
        diff.append(case - start)
        start = case

    return diff

@app.callback([Output("graph1", "figure"), Output("graph2", "figure"),
               Output("Alert1txt", "children"), Output("totvac", "value"),
               Output("pepvac", "value"), Output("pepfullvac", "value")],
         [Input("countries", "value")])
def cback1(val):
    URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/{}.csv"
    data = pd.read_csv(URL.format(val.replace(" ", "%20")))
    fig1 = go.Figure()
    fig1.add_trace(
        go.Scatter(x=data["date"], y=data["total_vaccinations"], name="Total Vaccinations", line=dict(color='orange'))
    )
    fig1.add_trace(
        go.Scatter(x=data["date"], y=data["people_vaccinated"], name="People Vaccinated", line=dict(color='yellow'))
    )
    fig1.add_trace(
        go.Scatter(x=data["date"], y=data["people_fully_vaccinated"], name="People Fully Vaccinated", line=dict(color='green'))
    )
    upd_layout(fig1)

    tot_vacs = get_range(data["total_vaccinations"])
    pep_vacs = get_range(data["people_vaccinated"])
    pep_full_vacs = get_range(data["people_fully_vaccinated"])
    dates = data["date"][1:]

    fig2 = go.Figure()
    fig2.add_trace(
        go.Scatter(x=dates, y=tot_vacs, name="New Total Vaccinations", line=dict(color='orange'))
    )
    fig2.add_trace(
        go.Scatter(x=dates, y=pep_vacs, name="New People Vaccinated", line=dict(color='yellow'))
    )
    fig2.add_trace(
        go.Scatter(x=dates, y=pep_full_vacs, name="New People Fully Vaccinated", line=dict(color='green'))
    )
    upd_layout(fig2)
    print(list(data["people_vaccinated"])[-1])
    return fig1, fig2, list(data["vaccine"])[-1], list(data["total_vaccinations"])[-1], list(data["people_vaccinated"])[-1], list(data["people_fully_vaccinated"])[-1]

app.index_string = extras.ind_str
app.title = 'Corona Tracker'

if __name__ == '__main__':
    app.run_server(debug=False)