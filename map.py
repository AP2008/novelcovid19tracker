from modules import *
from web_scrape import *
from sidebar import *
import listed
import extras

external_stylesheets = [extras.theme]

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}
CONTENT_STYLE = {
    "margin-left": "1rem",
    "margin-right": "1rem"
}
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/map/'
     )
app.layout = html.Div(children=[
    html.Base(target="_parent"),
    html.Div([navbar("Map")]),
    html.Div([
        dcc.Dropdown(
            id='drop',
            options=[
                {'label': 'World', 'value':'world'},
                {'label': 'India', 'value':'india'}
            ],
            style=dict(color='black'),
            value='world'
        ),
        html.Div([
            dbc.Spinner(
                dcc.Graph(id='map',
                          style={
                              'width': '100vw',
                              'height': '80vh',
                              'overflowY': True
                          }
                )
            ),
            dcc.Interval(
                id='interval-map',
                interval=600000,
                n_intervals=0
            )
        ], className='box')
    ], style=CONTENT_STYLE)
],
)

def single_list(h):
    try:
        return int(h[-1])
    except:
        return int(h)

@app.callback(Output('map', 'figure'),
              [Input('interval-map', 'n_intervals'),
               Input('drop', 'value')])
def map(n, drop_val):
    print(drop_val)
    if drop_val == 'india':
        print("HELLO")
        URL = 'https://api.covid19india.org/csv/latest/state_wise.csv'
        page = requests.get(URL, verify=False).content
        df = pd.read_csv(io.StringIO(page.decode('utf-8')))
        ncols = ['State', 'Confirmed', 'Recovered', 'Deaths', 'Active']
        df = df[ncols]
        df = df.drop([0, 36])

        new_cols = list(df.columns)
        states = list(df['State'])
        cases = list(df['Confirmed'].map(int))

        dictionary = {}
        x = 0
        for y in states:
            dictionary[y] = cases[x]
            x+=1

        z = []
        text = []
        df.index = df[new_cols[0]]

        for x in states:
            print(x, x in list(states))
            state = x
            if x in list(states):
                z.append(dictionary[x])
                text.append('' + state
                    + '<br> Confirmed: ' + str(df.loc[state][new_cols[1]])
                    + '<br> Recovered: ' + str(df.loc[state][new_cols[2]])
                    + '<br> Deceased: ' + str(df.loc[state][new_cols[3]])
                    + '<br> Active: ' + str(df.loc[state][new_cols[4]]))
            else:
                text.append('State: ' + state
                    + '<br> Confirmed: ' + str(0)
                    + '<br> Recovered: ' + str(0)
                    + '<br> Deceased: ' + str(0)
                    + '<br> Active: ' + str(0))
                z.append(0)

        trace = go.Choropleth(z=z,
                                    featureidkey='properties.ST_NM',
                                    locations=states,
                                    colorscale='Reds',
                                    colorbar=dict(thickness=20, ticklen=3),
                                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                    text=text,
                                    hoverinfo='text',
                                    marker_line_width=0.1, marker_opacity=0.7)

        layout = go.Layout(#title_text='Choropleth Map of Confirmed Covid-19 cases in India',
                           title_x=0.5,
                                         plot_bgcolor='#2B3E50',
                                         paper_bgcolor='#2B3E50'
                                       )

        fig = go.Figure(data=[trace], layout =layout)
        fig.update_geos(
            visible=False,
            projection=dict(
                type='conic conformal',
                parallels=[12.472944444, 35.172805555556],
                rotation={'lat': 24, 'lon': 80}
            ),
            lonaxis={'range': [68, 98]},
            lataxis={'range': [6, 38]}
        )
        fig.update_layout(
            title=dict(
                xanchor='center',
                x=0.5,
                yref='paper',
                yanchor='bottom',
                y=1,
                pad={'b': 10}),
            margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
            height=550,
            width=550
        )
        return fig
    elif drop_val == 'world':
        temp = requests.get("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv")
        temp = io.StringIO(temp.content.decode('utf-8'))
        dfData = pd.read_csv(temp)
        dfData = dfData.fillna(0)
        mapDf = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
        dfData.index = dfData['iso_code']

        countrycodes = set(dfData['iso_code'])
        mapcountrycodes = set(mapDf['CODE'])

        locations = list(countrycodes.intersection(mapcountrycodes))
        z = []
        text = []
        for i in locations:
            n = dfData.loc[i]['total_cases']
            z.append((single_list(dfData.loc[i]['total_cases'])/single_list(dfData.loc[i]['population']))*100)
            text.append('' + str(dfData.loc[i]['location'])
                    + '<br> Confirmed: ' + str(single_list(dfData.loc[i]['total_cases']))
                    + '<br> New Confirmed: ' + str(single_list(dfData.loc[i]['new_cases']))
                    + '<br> Deaths: ' + str(single_list(dfData.loc[i]['total_deaths']))
                    + '<br> New Deaths: ' + str(single_list(dfData.loc[i]['new_deaths'])))
        fig = go.Figure(data=go.Choropleth(locations=locations, z=z, colorscale='Reds', text=text, hoverinfo='text+z'))
#        fig.update_traces(showscale=False)
        fig.update_layout(#autosize=True,
                                         plot_bgcolor='#2B3E50',
                                         paper_bgcolor='#2B3E50',
                margin={"r":0,"t":0,"l":0,"b":0}
        )
        return fig


app.index_string = extras.ind_str
app.title = 'Corona Tracker'
if __name__ == '__main__':
    app.run_server(debug=False)

