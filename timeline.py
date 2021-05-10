from modules import *
from web_scrape import *
from sidebar import *
import extras

external_stylesheets = [extras.theme]

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

page_countries = eval(requests.get('https://cacheserver.pythonanywhere.com').content)
countries = pd.DataFrame.from_dict(page_countries)['Country'].values.tolist()
slugs = pd.DataFrame.from_dict(page_countries)['Slug'].values.tolist()
page = requests.get('https://cacheserver.pythonanywhere.com?c=india', verify=False)
dates = pd.DataFrame.from_dict(page.json())['Date'].values.tolist()
ddc = []
for i, country in enumerate(countries):
    ddc.append({'label': country, 'value': slugs[i]})

datesF = []
for i in dates:
    s = i.split('-')
    a = int(s[0])
    b = int(s[1])
    c = int(s[2][:2])
    datesF.append((a,b,c))

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/timeline/'
     )
CONTENT_STYLE = {
    "margin-left": "1rem",
    "margin-right": "1rem"
}

app.layout = html.Div([
    html.Base(target="_parent"),
        navbar("Timeline"),
html.Div([
    html.Div(id = 'Fe_He', children=[
        dcc.DatePickerRange(
            id='dat_',
            min_date_allowed=dt(datesF[0][0], datesF[0][1], datesF[0][2]),
            max_date_allowed=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]),
            initial_visible_month=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]),
            start_date=dt(datesF[0][0], datesF[0][1], datesF[0][2]).date(),
            end_date=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]).date(),
            display_format='MMM|Do|YY'
        )
    ]),
    html.Div([
        dcc.Dropdown(
            id = 'drop',
            options = ddc,
            style=dict(width='100%'),
            value='india'
        )
    ]),
    html.Div([
        html.H4(f'Timeline', id='nono_', style={'color':'white'}),
        dcc.Graph(id='update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=5000,
            n_intervals=0
        )
    ], className='box')],
style=CONTENT_STYLE)
  ]
)

@app.callback(Output('Fe_He', 'children'),
                [Input('drop', 'value')])
def fnucs(val_d):
    URL = 'https://cacheserver.pythonanywhere.com/?c=' + val_d
    page = requests.get(URL, verify=False)
    dates = pd.DataFrame.from_dict(page.json())['Date'].values.tolist()
    global datesF
    datesF = []
    for i in dates:
        s = i.split('-')
        a = int(s[0])
        b = int(s[1])
        c = int(s[2][:2])
        datesF.append((a,b,c))
    return dcc.DatePickerRange(
        id='dat_',
        min_date_allowed=dt(datesF[0][0], datesF[0][1], datesF[0][2]),
        max_date_allowed=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]),
        initial_visible_month=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]),
        start_date=dt(datesF[0][0], datesF[0][1], datesF[0][2]).date(),
        end_date=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]).date(),
        display_format='MMM|Do|YY'
    )


@app.callback(Output('update-graph', 'figure'),
              [Input('drop', 'value'),
               Input('interval-component', 'n_intervals'),
               Input('dat_', 'start_date'),
               Input('dat_', 'end_date')
                ])
def plot_bar(val, n, start, end):
    '''
    Plots the collected data
    '''
    start = start.split('-')
    end = end.split('-')
    start_index = datesF.index((int(start[0]), int(start[1]), int(start[2])))
    end_index = datesF.index((int(end[0]), int(end[1]), int(end[2]))) + 1
    print(start_index, end_index)
    page = requests.get('https://cacheserver.pythonanywhere.com/?c=' + val)
    dfc = pd.DataFrame.from_dict(page.json())
    fig = ms(rows = 2, cols=2,
        specs=[[{}, {}],
               [{"colspan": 2}, None]],
    )
    print(len(dfc['Date']))
    fig.add_trace(go.Bar(x=dfc['Date'][start_index:end_index], y=dfc['Deaths'][start_index:end_index], name='Deaths'),1,1)
    fig.add_trace(go.Scatter(x=dfc['Date'][start_index:end_index], y=dfc['Deaths'][start_index:end_index], name='Deaths'),1,1)
    fig.add_trace(go.Bar(x=dfc['Date'][start_index:end_index], y=dfc['Recovered'][start_index:end_index], name='Recoveries'),1,2)
    fig.add_trace(go.Scatter(x=dfc['Date'][start_index:end_index], y=dfc['Recovered'][start_index:end_index], name='Recoveries'),1,2)
    fig.add_trace(go.Bar(x=dfc['Date'][start_index:end_index], y=dfc['Confirmed'][start_index:end_index], name='Confirmed Cases'),2,1)
    fig.add_trace(go.Scatter(x=dfc['Date'][start_index:end_index], y=dfc['Confirmed'][start_index:end_index], name='Confirmed Cases'),2,1)
    fig.update_layout(showlegend=False,
                      legend=dict(
                          font=dict(
                              color="white"
                          )
                      ),
                      margin=dict(
                      l=0,
                      r=0,
                      t=0,
                      pad=0
                            ),
                      paper_bgcolor='#2B3E50')
    fig.update_xaxes(tickangle=90, tickfont=dict(family='Rockwell', color='white'))
    fig.update_yaxes(tickfont=dict(family='Rockwell', color='white'))
    return fig
app.index_string = extras.ind_str
app.title = 'Corona Tracker'
if __name__ == '__main__':
    app.run_server(debug=False)
