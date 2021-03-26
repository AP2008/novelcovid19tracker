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
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/map/'
     )
app.layout = html.Div(children=[
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
                dcc.Graph(id='map'#,
                          # figure=init()
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
#        url = 'https://www.mohfw.gov.in/'
#
#        web_content = requests.get(url, verify=False).content
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

#        with open(app.get_asset_url('listed.geojson')) as geofile:
#            jdata = json.load(geofile)
        jdata = json.loads(listed.k)

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

        layout = go.Layout(#title_text='Choropleth Map of Confirmed Covid-19 cases in India',
                           title_x=0.5,#height=800,
                                         plot_bgcolor='#2B3E50',
                                         paper_bgcolor='#2B3E50',
                           mapbox_style="dark", mapbox_accesstoken=mapboxt,
                           mapbox = dict(center= dict(lat=20.5937, lon=78.9629),
                                         accesstoken= mapboxt,
                                         zoom=3
                                       ))

        fig = go.Figure(data=[trace], layout =layout)
        print('S')
        return fig
    elif drop_val == 'world':
        temp = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.csv")
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
            z.append(single_list(dfData.loc[i]['total_cases']))
            text.append('' + str(dfData.loc[i]['location'][-1])
                    + '<br> Confirmed: ' + str(single_list(dfData.loc[i]['total_cases']))
                    + '<br> New Confirmed: ' + str(single_list(dfData.loc[i]['new_cases']))
                    + '<br> Deaths: ' + str(single_list(dfData.loc[i]['total_deaths']))
                    + '<br> New Deaths: ' + str(single_list(dfData.loc[i]['new_deaths'])))
        fig = go.Figure(data=go.Choropleth(locations=locations, z=z, colorscale='Reds', text=text, hoverinfo='text'))
#        fig.update_layout(
#                title_text='Choropleth Map of Confirmed Covid-19 cases'#,
#                height=800
#        )
        return fig


app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script async src="https://arc.io/widget.min.js#LHbAsxJ6"></script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""
app.title = 'Corona Tracker'
if __name__ == '__main__':
    app.run_server(debug=False)

