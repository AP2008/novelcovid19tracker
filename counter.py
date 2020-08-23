from web_scrape import *
from modules import *
from sidebar import *

external_stylesheets = [dbc.themes.SOLAR, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/counter/'
                )

page=requests.get("https://www.worldometers.info/coronavirus/")
soup=bs(page.content, 'html.parser')
results = soup.find_all(id='maincounter-wrap')
print("st")
value1 = int(get_ccii(results))
value2 = int(get_cdii(results))
value3 = int(get_crii(results))
print(value1)

url = "https://www.worldometers.info/coronavirus/"
web = requests.get(url)
print(web)
web_content = web.content
# parse the html content
soup2 = bs(web_content, "html.parser")
# remove any newlines and extra spaces from left and right
extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
# find all table rows and data cells within
stats = []
all_rows = soup.find_all('tr')
for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    if len(stat) == 19:
          stats.append(stat)
ncols = [
    "SR no.", "Country", "Cases", "New Cases", "Deaths", "New Deaths",
    "Recoveries", "New Recoveries", "Active", "Serious", "Cases/1M pop",
    "Deaths/1M pop", "Total Tests", "Tests/1M pop", "Population", "1 case every X ppl", 
    "1 Death every X ppl", "1 Test every X ppl", "Continent"]
df = pd.DataFrame(data=stats, columns=ncols)
ndf = df
l = list(ndf['Country'])
print(l)
l[l.index('USA')] = 'US'
l[l.index('Saudi Arabia')] = 'saudi-arabia'
l[l.index('UAE')] = 'United-Arab-Emirates'
l[l.index('S. Korea')] = 'South-Korea'
l[l.index('Czechia')] = 'Czec-Republic'
l[l.index('Dominican Republic')] = 'Dominican-Republic'
l[l.index('South Africa')] = 'South-Africa'
l[l.index('Bosnia and Herzegovina')] = 'Bosnia-and-Herzegovina'
l[l.index('New Zealand')] = 'New-Zealand'
l[l.index('North Macedonia')] = 'Macedonia'
l[l.index('Ivory Coast')] = 'Cote-d-Ivoire'
l[l.index('Hong Kong')] = 'Chine-Hong-Kong-sar'
l[l.index('Costa Rica')] = 'Costa-Rica'
country = dict(zip(l, l))
count = []
for x in l:
    count.append({'label':x, 'value':x})
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'color': '#FFFFFF'
}
app.layout = html.Div([
    html.Div([
        navbar
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
            value='India'
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
    page=requests.get("https://www.worldometers.info/coronavirus/")
    soup=bs(page.content, 'html.parser')
    results = soup.find_all(id='maincounter-wrap')
    print("st")
    return int(get_ccii(results)), int(get_cdii(results)), int(get_crii(results))

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
    page=requests.get("https://www.worldometers.info/coronavirus/country/"+val)
    soup=bs(page.content, 'html.parser')
    results = soup.find_all(id='maincounter-wrap')
    return int(get_ccii(results)), int(get_cdii(results)), int(get_crii(results)), 'COVID19 CASES IN '+ val, 'COVID19 DEATHS IN '+ val, 'COVID19 RECOVERIES IN '+val
app.title = 'Corona Tracker'

if __name__ == '__main__':
    app.run_server(debug=False)

