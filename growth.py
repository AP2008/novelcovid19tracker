import pandas as pd
import requests
import plotly.graph_objs as go
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from sidebar import *
import extras
import time
from dash.exceptions import PreventUpdate


external_stylesheets = [extras.theme]
page_countries = eval(requests.get("https://cacheserver.pythonanywhere.com/").content)
n = pd.DataFrame.from_dict(page_countries)
countries = n['Country'].values.tolist()
slugs = n['Slug'].values.tolist()
ddc = []
for i, country in enumerate(countries):
    ddc.append({'label': country, 'value': slugs[i]})

def get_df(country: str) -> pd.DataFrame:
    url = 'https://cacheserver.pythonanywhere.com/?c=' + country
    page = requests.get(url, verify=False)
    df = pd.DataFrame.from_dict(page.json())
    dates = df['Date'].values.tolist()
    ddc = []
    for i, country in enumerate(countries):
        ddc.append({'label': country, 'value': slugs[i]})

    datesF = []
    for i in dates:
        s = i.split('-')
        a = int(s[0])
        b = int(s[1])
        c = int(s[2][:2])
        datesF.append((a, b, c))

    df = df.reset_index()
    df = df[['Confirmed', 'Recovered', 'Deaths', 'Date']]

    return df

def get_range(cases: list) -> list:
    diff = []
    start = 0
    for case in cases:
        diff.append(case - start)
        start = case

    return diff


app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/growth/')
CONTENT_STYLE = {
}
app.layout = html.Div([
    html.Base(target="_parent"),
    navbar("Growth"),
    html.Div([
        dcc.Dropdown(
            id = 'drop',
            options = ddc,
            style=dict(width='100%'),
            value='india'
        ),
        html.Div([
            dcc.Dropdown(id="ind_drop")],
            id='net'),
        html.Div([
            dcc.Dropdown(id="drop2"),
            dcc.Dropdown(id="drop3"),
            dcc.Dropdown(id="drop4")],
            id='net2'),
        html.Div([
            dcc.Graph(
                id='graph'
            ),
            dcc.Interval(
                id='interval_component',
                interval=10000,
                n_intervals=0
            )
        ], className="box")
    ])
])


@app.callback([Output("net", "children"), Output("net2", "style")],
        [Input("drop", "value")])
def net_c(val):
    if val == "india":
        return [
            dcc.Dropdown(
                id="ind_drop",
                options=[
                    {'label': 'Districts', 'value': 'district'},
                    {'label': 'State', 'value': 'state'}],
                value="state")], {'display': 'block'}
    else:
        return [], {'display': 'none'}

@app.callback(Output("net2", "children"),
        [Input("ind_drop", "value")])
def net2_c(val):
    k = pd.read_csv("https://api.covid19india.org/csv/latest/district_wise.csv")
    states = list(set(k["State"]))
    states.sort()
    s = list(k.loc[k["State"] == "Andhra Pradesh"]["District"])
    s.sort()
    if val == "state":
        return [
            dcc.Dropdown(
                id="drop4",
                options=[{'label': x, 'value': x} for x in states] + [{'label': 'All', 'value': 'all'}],
                value="all", style={"display": "block"}),
            dcc.Dropdown(
                id="drop2",
                options=[{'label': x, 'value': x} for x in states],
                value="Andhra Pradesh", style={"display": "none"}),
            dcc.Dropdown(
                id="drop3",
                options=[{'label': x, 'value': x} for x in s],
                value=s[0], style={"display": "none"}
            )
        ]
    elif val=="district":
        return [
            dcc.Dropdown(
                id="drop4",
                options=[{'label': x, 'value': x} for x in states],
                value="Andhra Pradesh", style={"display": "none"}),
            dcc.Dropdown(
                id="drop2",
                options=[{'label': x, 'value': x} for x in states],
                value="Andhra Pradesh", style={"display": "block"}),
            dcc.Dropdown(
                id="drop3",
                options=[{'label': x, 'value': x} for x in s],
                value=s[0], style={"display": "block"}
            )
        ]

@app.callback([Output("drop3", "options"), Output("drop3", "value")],
            [Input("drop2", "value")])
def drop2_c(val):
    if val:
        k = pd.read_csv("https://api.covid19india.org/csv/latest/district_wise.csv")
        s = list(k.loc[k["State"] == val]["District"])
        s.sort()
        return [{'label': x, 'value': x} for x in s], s[0]
    else:
        raise PreventUpdate


def plot_data(dates, confirmed_diff, deaths_diff, recovered_diff, active_diff):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=dates, y=confirmed_diff, name='New Cases', line=dict(color='orange'))
    )
    fig.add_trace(
        go.Scatter(x=dates, y=deaths_diff, name='New Deaths', line=dict(color='red'))
    )
    fig.add_trace(
        go.Scatter(x=dates, y=recovered_diff, name='New Recoveries', line=dict(color='green'))
    )
    fig.add_trace(
        go.Scatter(x=dates, y=active_diff, name='New Active', line=dict(color='yellow'))
    )
    fig.update_layout(showlegend=False,
                      legend=dict(
                          font=dict(
                              color="white"
                          )
                      ),
                      margin=dict(
                          l=5,
                          r=0,
                          b=5,
                          t=0,
                          pad=0
                      ),
                      plot_bgcolor='#0f2537',
                      paper_bgcolor='#0f2537')
    fig.update_xaxes(tickangle=90, tickfont=dict(family='Rockwell', color='white'), rangeslider=dict(visible=True))
    fig.update_yaxes(tickfont=dict(family='Rockwell', color='white'))
    return fig

@app.callback(Output('graph', 'figure'),
            [Input("drop3", "value"), Input("drop", "value"), Input("drop4", "value"), Input("drop2", "value")])
def drop3_c(val, val2, val3, val4):
    ctx = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    print("{}: {}", ctx, [val, val2, val3, val4])
    if ctx == "drop3":
        k = pd.read_csv("https://api.covid19india.org/csv/latest/districts.csv")
        row = k.loc[k["State"] == val4]
        rows = row.loc[row["District"] == val]
        cdf = rows["Confirmed"]
        confirmed_diff = get_range(list(cdf))
        #print(confirmed_diff)
        ddf = list(rows["Deceased"])
        deaths_diff = get_range(list(ddf))
        rdf = list(rows["Recovered"])
        recovered_diff = get_range(list(rdf))
        adf = list(rows["Confirmed"] - (rows["Recovered"] + rows["Deceased"]))
        active_diff = get_range(adf)
        fig = plot_data(list(rows["Date"]), confirmed_diff, deaths_diff, recovered_diff, active_diff)
    elif ctx == "drop":
        fig = glob_plot(val2)
    elif ctx == "drop4":
        if val3 == "all":
            fig = glob_plot("india")
        else:
            k = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
            rows = k.loc[k["State"] == val3]
            cdf = rows["Confirmed"]
            confirmed_diff = get_range(list(cdf))
            ddf = list(rows["Deceased"])
            deaths_diff = get_range(list(ddf))
            rdf = list(rows["Recovered"])
            recovered_diff = get_range(list(rdf))
            adf = list(rows["Confirmed"] - (rows["Recovered"] + rows["Deceased"]))
            active_diff = get_range(adf)
            fig = plot_data(list(rows["Date"]), confirmed_diff, deaths_diff, recovered_diff, active_diff)

    return fig

def glob_plot(value):
    dfc = get_df(value)
    dates = dfc['Date']
    confirmed_diff = get_range(dfc['Confirmed'])
    deaths_diff = get_range(dfc['Deaths'])
    recovered_diff = get_range(dfc['Recovered'])
    dfa = pd.DataFrame(dfc['Confirmed'] - (dfc['Deaths'] + dfc['Recovered']))
    active_diff = get_range(dfa[dfa.columns[0]])
    fig = plot_data(dates, confirmed_diff, deaths_diff, recovered_diff, [])
    return fig


app.index_string = extras.ind_str
app.title = 'Corona Tracker'

if __name__ == '__main__':
    app.run_server(debug=False)
