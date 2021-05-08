from modules import *
from sidebar import *
import extras

external_stylesheets = [extras.theme]

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/counter/'
                )

URL = "https://api.covid19api.com/summary"
page = json.loads(requests.get(URL, verify=False).content)

glob = page["Global"]
value1 = int(glob["TotalConfirmed"])
value2 = int(glob["TotalDeaths"])
value3 = int(glob["TotalRecovered"])

d_c = pd.read_json(requests.get("https://api.covid19api.com/countries", verify=False).content)
l = d_c
count = []
for x, y in zip(d_c["Country"], d_c["Slug"]):
    count.append({'label':x, 'value':y})

CONTENT_STYLE = {
    'color': '#FFFFFF'
}

app.layout = html.Div([
    navbar("Counter"),
    html.Base(target="_parent"),
    dbc.Row([
        dbc.Col([
            html.H4("CASES - WORLD"),
            daq.LEDDisplay(
                id='ccii',
                value=value1,
                color='#FFA500',
                backgroundColor='#0d0d0d',
                style={'margin-left':'10px'}
            ),
            html.H4("DEATHS - WORLD"),
            daq.LEDDisplay(
                id='cdii',
                value=value2,
                color='#ae0700',
                backgroundColor='#0d0d0d',
                style={'margin-left':'10px'}
            ),
            html.H4("RECOVERIES - WORLD"),
            daq.LEDDisplay(
                id='crii',
                value=value3,
                color='#66ff00',
                backgroundColor='#0d0d0d',
                style={'margin-left':'10px'}
            ),
            dcc.Interval(
                id='interval',
                interval=5000,
                n_intervals=0
            )
        ], width=12, lg=6),
        dbc.Col([
            dcc.Dropdown(
                id='drop',
                options=count,
                style=dict(width='100%', color='black'),
                value='india'
            ),
            html.H4(id='c', children="CASES - India"),
            daq.LEDDisplay(
                id='cv',
                value=0,
                color='#FFA500',
                backgroundColor='#0d0d0d'
            ),
            html.H4(id='d', children="DEATHS - India"),

            daq.LEDDisplay(
                id='cd',
                value=0,
                color='#ae0700',
                backgroundColor='#0d0d0d'
            ),
            html.H4(id='r', children="RECOVERIES - India"),
            daq.LEDDisplay(
                id='cr',
                value=0,
                color='#66ff00',
                backgroundColor='#0d0d0d'
            ),
            dcc.Interval(
                id='interval-comp',
                interval=300000,
                n_intervals=0
            )
        ], width=12, lg=6)
    ])
],
style=CONTENT_STYLE
)

@app.callback([Output('ccii', 'value'),
              Output('cdii', 'value'),
              Output('crii', 'value')],
              [Input('interval','n_intervals')])
def func(n):
    page = json.loads(requests.get(URL, verify=False).content)
    glob = page["Global"]
    value1 = int(glob["TotalConfirmed"])
    value2 = int(glob["TotalDeaths"])
    value3 = int(glob["TotalRecovered"])
    return value1, value2, value3

@app.callback([Output('cv', 'value'),
                Output('cd', 'value'),
                Output('cr', 'value'),
                Output('c', 'children'),
                Output('d', 'children'),
                Output('r', 'children')],
              [Input('interval-comp', 'n_intervals'),
                Input('drop', 'value')]
              )
def funct(n, val):
    p_l = pd.DataFrame(json.loads(requests.get(URL, verify=False).content)["Countries"]).set_index("Slug")
    return int(p_l["TotalConfirmed"][val]), int(p_l["TotalDeaths"][val]), int(p_l["TotalRecovered"][val]), 'CASES -  '+ val, 'DEATHS - '+ val, 'RECOVERIES - '+val
app.index_string = extras.ind_str
app.title = 'Corona Tracker'

if __name__ == '__main__':
    app.run_server(debug=False)

