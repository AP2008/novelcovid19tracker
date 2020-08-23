from modules import *
from web_scrape import *
from sidebar import *

external_stylesheets = [dbc.themes.SOLAR, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}
# def init():
    # print("HELLO")
    # url = 'https://www.mohfw.gov.in/'

    # web_content = requests.get(url).content
    # soup = bs(web_content, "html.parser")
    # extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
    # stats = []
    # all_rows = soup.find_all('tr')
    # for row in all_rows:
        # stat = extract_contents(row.find_all('td'))
        # if len(stat) == 6:
            # stats.append(stat)
    # new_cols = ["Sr.No", "States/UT", "Active", "Recovered","Deceased","Confirmed"]
    # state_data = pd.DataFrame(data = stats, columns = new_cols)
    # states = state_data['States/UT']
    # cases = state_data['Confirmed'].map(int)

    # with open("C:\Work\Igismap\listed.geojson") as geofile:
        # jdata = json.load(geofile)

    # i = 1
    # for feature in jdata['features']:
        # feature['id'] = i
        # i+=1

    # states2 = []
    # x = 0
    # for y in range(len(jdata['features'])):
        # states2.append(jdata['features'][x]['properties']['st_nm'])
        # x+=1

    # dictionary = {}
    # x = 0
    # for y in states:
        # dictionary[y] = cases[x]
        # x+=1

    # z = []
    # for x in states2:
        # if x in list(states):
            # z.append(dictionary[x])
        # else:
            # z.append(0)

    # mapboxt = 'pk.eyJ1IjoiYXIyMDA4IiwiYSI6ImNrOHduZGx2dzBjYTczZnFvNXE4dW5odjkifQ.xQGBYsA7sBziM2gfj9CrmA'

    # text = list(states2)
    # locations = [1+x for x in range(36)]

    # trace = go.Choroplethmapbox(z=z,
                                # locations=locations,
                                # colorscale='Reds',
                                # colorbar=dict(thickness=20, ticklen=3),
                                # geojson=jdata,
                                # text=text,
                                # hoverinfo='all',
                                # marker_line_width=0.1, marker_opacity=0.7)

    # layout = go.Layout(title_text='Choropleth Map of Confirmed Covid-19 cases in India',                       title_x=0.5,height=800,
                                     # plot_bgcolor='#111111',
                                     # paper_bgcolor='#111111',
                       # mapbox_style="dark", mapbox_accesstoken=mapboxt,
                       # mapbox = dict(center= dict(lat=20.5937, lon=78.9629),
                                     # accesstoken= mapboxt,
                                     # zoom=3
                                   # ))

    # fig = go.Figure(data=[trace], layout =layout)
    # print('S')
    # return fig
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/map/'
     )
app.layout = html.Div(children=[
    # html.A(html.Button('Home'),
                      # href='http://127.0.0.1:8080/home'),
    # html.A(html.Button('Bar'),
                      # href='http://127.0.0.1:8080/bar'),
    # html.A(html.Button('Pie'),
                      # href='http://127.0.0.1:8080/pie'),
    # html.A(html.Button('Map'),
                      # href='http://127.0.0.1:8080/map'),
    # html.A(html.Button('Table'),
                      # href='http://127.0.0.1:8080/table'),
    html.Div([navbar]),
    html.Div([
        dcc.Dropdown(
            id='drop',
            options=[
                {'label': 'World', 'value':'world'},
                {'label': 'India', 'value':'india'}
            ],
            style=dict(width='40%'),
            value='world'
        ),
        html.Div([
            dbc.Spinner(
                dcc.Graph(id='map'#,
                          # figure=init()
                )
            ),
            dcc.Interval(
                id='interval-map',
                interval=600000,
                n_intervals=0
            )
        ])
    ], style=CONTENT_STYLE)
],
    #style={'backgroundColor': colors['background'], 'color':'black'}
          #'color': colors['text']}
)

@app.callback(Output('map', 'figure'),
              [Input('interval-map', 'n_intervals'),
               Input('drop', 'value')])
def map(n, drop_val):
    print(drop_val)
    if drop_val == 'india':
        print("HELLO")
        URL = 'https://api.covid19india.org/csv/latest/state_wise.csv'
        page = requests.get(URL).content
        df = pd.read_csv(io.StringIO(page.decode('utf-8')))
        ncols = ['State', 'Confirmed', 'Recovered', 'Deaths', 'Active']
        df = df[ncols]
        df = df.drop([0, 36])
#        url = 'https://www.mohfw.gov.in/'
#
#        web_content = requests.get(url).content
#        soup = bs(web_content, "html.parser")
#        extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
#        stats = []
#        all_rows = soup.find_all('tr')
#        for row in all_rows:
#            stat = extract_contents(row.find_all('td'))
#            if len(stat) == 6:
#                stats.append(stat)
#        new_cols = ["Sr.No", "States/UT", "Active", "Recovered","Deceased","Confirmed"]
#        state_data = pd.DataFrame(data = stats, columns = new_cols)
#        state_data = state_data.drop(len(state_data)-1)
#        state_data = state_data.drop(len(state_data)-1)
#        print(state_data)
        new_cols = list(df.columns)
        states = list(df['State'])
        cases = list(df['Confirmed'].map(int))

        with open("listed.geojson") as geofile:
            jdata = json.load(geofile)

        i = 1
        for feature in jdata['features']:
            feature['id'] = i
            i+=1

        states2 = []
        x = 0
        print(states)
        for y in range(len(jdata['features'])):
            print(jdata['features'][x]['properties']['st_nm'], end=', ')
            states2.append(jdata['features'][x]['properties']['st_nm'])
            x+=1

        dictionary = {}
        x = 0
        for y in states:
            dictionary[y] = cases[x]
            x+=1
        print(dictionary)
        locations = [x+1 for x in range(len(states2))]
        z = []
        text = []
        df.index = df[new_cols[0]]
        for x in states2:
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

        mapboxt = 'pk.eyJ1IjoiYXIyMDA4IiwiYSI6ImNrOHduZGx2dzBjYTczZnFvNXE4dW5odjkifQ.xQGBYsA7sBziM2gfj9CrmA'

#        locations = [1+x for x in range(len(states))]
        
#        state_data.index = state_data[new_cols[1]]
        trace = go.Choroplethmapbox(z=z,
                                    locations=locations,
                                    colorscale='Reds',
                                    colorbar=dict(thickness=20, ticklen=3),
                                    geojson=jdata,
                                    text=text,
                                    hoverinfo='text',
                                    marker_line_width=0.1, marker_opacity=0.7)

        layout = go.Layout(title_text='Choropleth Map of Confirmed Covid-19 cases in India',
                           title_x=0.5,height=800,
                                         plot_bgcolor='#111111',
                                         paper_bgcolor='#111111',
                           mapbox_style="dark", mapbox_accesstoken=mapboxt,
                           mapbox = dict(center= dict(lat=20.5937, lon=78.9629),
                                         accesstoken= mapboxt,
                                         zoom=3
                                       ))

        fig = go.Figure(data=[trace], layout =layout)
        print('S')
        return fig
    elif drop_val == 'world':
        dfData = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
        dfData = dfData.fillna(0)
        mapDf = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
        dfData.index = dfData['iso_code']

        countrycodes = set(dfData['iso_code'])
        mapcountrycodes = set(mapDf['CODE'])

        locations = list(countrycodes.intersection(mapcountrycodes))
        z = []
        text = []
        for i in locations:
            z.append(int(dfData.loc[i]['total_cases'][-1]))
            text.append('' + str(dfData.loc[i]['location'][-1])
                    + '<br> Confirmed: ' + str(dfData.loc[i]['total_cases'][-1])
                    + '<br> New Confirmed: ' + str(dfData.loc[i]['new_cases'][-1])
                    + '<br> Deaths: ' + str(dfData.loc[i]['total_deaths'][-1])
                    + '<br> New Deaths: ' + str(dfData.loc[i]['new_deaths'][-1]))
        fig = go.Figure(data=go.Choropleth(locations=locations, z=z, colorscale='Reds', text=text, hoverinfo='text'))
        fig.update_layout(
                title_text='Choropleth Map of Confirmed Covid-19 cases',
                height=800
        )
        return fig


app.title = 'Corona Tracker'
if __name__ == '__main__':
    app.run_server(debug=False)

