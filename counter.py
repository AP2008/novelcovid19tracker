from modules import *
from sidebar import *
import extras

external_stylesheets = [extras.theme, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

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
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'color': '#FFFFFF'
}
app.layout = html.Div([
    html.Div([
        navbar("Counter")
    ]),
    html.Div([
        html.H4("COVID19 CASES WORLDWIDE"),
        daq.LEDDisplay(
            id='ccii',
            value=value1,
            color='#0066ff',
            backgroundColor='#0d0d0d',
            style={'margin-left':'10px'}
        ),
        html.H4("COVID19 DEATHS WORLDWIDE"),
        daq.LEDDisplay(
            id='cdii',
            value=value2,
            color='#0066ff',
            backgroundColor='#0d0d0d',
            style={'margin-left':'10px'}
        ),
        html.H4("COVID19 RECOVERIES WORLDWIDE"),
        daq.LEDDisplay(
            id='crii',
            value=value3,
            color='#0066ff',
            backgroundColor='#0d0d0d',
            style={'margin-left':'10px'}
        ),
        dcc.Interval(
            id='interval',
            interval=5000,
            n_intervals=0
        ),
    ], style={'margin-top':'40px'},
      className='four columns'
    ),
    # html.A(html.Button('Home'),
                      # href='http://127.0.0.1:8080/'),
    # html.A(html.Button('Bar'),
                      # href='http://127.0.0.1:8080/bar'),
    # html.A(html.Button('Pie'),
                      # href='http://127.0.0.1:8080/pie'),
    # html.A(html.Button('Map'),
                      # href='http://127.0.0.1:8080/map'),
    # html.A(html.Button('Table'),
                      # href='http://127.0.0.1:8080/table'),
    # html.Div([
        # html.H4('COVID 19 DASHBOARD 2020'),
        # dcc.Graph(id='pie', figure = fig),
        # dcc.Interval(
            # id='intv',
            # interval=10000,
            # n_intervals=0
        # )
    # ], className='four columns'
    # ),
    html.Div([
        dcc.Dropdown(
            id='drop',
            options=count,
            style=dict(width='100%', color='black'),
            value='india'
        ),
        html.H4(id='c', children="COVID19 CASES IN India"),
        daq.LEDDisplay(
            id='cv',
            value=0,
            color='#0066ff',
            backgroundColor='#0d0d0d'
        ),
        html.H4(id='d', children="COVID19 DEATHS IN India"),

        daq.LEDDisplay(
            id='cd',
            value=0,
            color='#0066ff',
            backgroundColor='#0d0d0d'
        ),
        html.H4(id='r', children="COVID19 RECOVERIES IN India"),
        daq.LEDDisplay(
            id='cr',
            value=0,
            color='#0066ff',
            backgroundColor='#0d0d0d'
        ),
        dcc.Interval(
            id='interval-comp',
            interval=5000,
            n_intervals=0
        )
    ], className='four columns'
    )
],
style=CONTENT_STYLE,
#         'backgroundColor': colors['background'],
  className='row'
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
    return int(p_l["TotalConfirmed"][val]), int(p_l["TotalDeaths"][val]), int(p_l["TotalRecovered"][val]), 'COVID19 CASES IN '+ val, 'COVID19 DEATHS IN '+ val, 'COVID19 RECOVERIES IN '+val
app.title = 'Corona Tracker'

if __name__ == '__main__':
    app.run_server(debug=False)

