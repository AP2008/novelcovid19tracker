from modules import *
from web_scrape import *
from sidebar import *

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

tab_style = {
    'height': '20px',
    'width': '100px',
    'color': 'white',
    'backgroundColor': 'black'
}

tab_selected_style = {
    'height': '20px',
    'width': '100px',
    'color': 'red',
    'backgroundColor': 'grey'
}
s1 = {
    'height': '20px',
    'width': '200px',
    'color': 'white',
    'backgroundColor': 'black'
}
s2 = {
    'height': '20px',
    'width': '200px',
    'color': 'red',
    'backgroundColor': 'grey'
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    #"padding": "2rem 1rem",
}
external_stylesheets = [dbc.themes.SOLAR, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
               requests_pathname_prefix='/table/'
)
app.layout = html.Div(children=[
    html.Div([
        navbar
    ]),
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
html.Div([
    html.Div(id='dropper', children=[
        dcc.Dropdown(
            id='drop',
            options=[
                {'label': 'World', 'value':'world'},
                {'label': 'India', 'value':'india'}
            ],
            style=dict(width='40%'),
            value='india'
        )
    ]),
    html.Div(id='tabs', children=[
        dcc.Tabs(id='tabs-table'),
        dcc.Tabs(id='india-tabs')
    ]),
    html.Div(id='name99', style={'display':'none'}),
    html.Div(id='name88', style={'display':'none'}),
    html.Div(id='dropper-ind', children=[
        dcc.Dropdown(
            id='dhop'
        )
    ]),
    html.Div(id='testing'),
    html.Div(id='tenten', style={'display':'none'}),
    html.Div(id='table_div', children=[
        dash_table.DataTable(
            id='table',
            style_header={'backgroundColor': 'rgb(30, 30, 30)','color':'white'},
            style_cell={
                'backgroundColor': 'rgb(50,50,50)',
                'color': 'white'
            },
            filter_action="native",
            sort_action="native"
        ),
        dcc.Interval(
            id='interval-com',
            interval=10000,
            n_intervals=0
            )
    ]),
    html.Div(id='tablet_div', children=[
        dash_table.DataTable(
            id='tablet',
            style_header={'backgroundColor': 'rgb(30, 30, 30)','color':'white'},
            style_cell={
                'backgroundColor': 'rgb(50, 50, 50)',
                'color': 'white'
            },
            filter_action="native",
            sort_action="native"
        ),
        dcc.Interval(
                    id='interval-component',
                    interval=10000,
                    n_intervals=0
                )
    ]),
], style=CONTENT_STYLE)
],
#    style={'backgroundColor': colors['background'],
#          'color': colors['text']}
)
def call_name_time(fe):
    global zone
    zone = fe
def vst(v):
    print(zone)
    global ret
    ret = v
def single_g(variable):
    global varsingle
    varsingle = variable

def multi_g(vars1, vars2):
    global varmulti1
    varmulti1 = vars1
    global varmulti2
    varmulti2 = vars2
def get_dist(value):
    URL = 'https://api.covid19india.org/csv/latest/district_wise.csv'
    page = requests.get(URL).content
    df = pd.read_csv(io.StringIO(page.decode('utf-8')))
    df = df[['District', 'Confirmed', 'Active', 'Deceased', 'Recovered', 'State']]
    df = df.fillna(0)
    url = 'https://api.covid19india.org/zones.json'
    districts = []
    zones = []
    data = pd.read_json(url)
    for i in range(len(data)):
        districts.append(list(data.xs(i))[0]['district'])
        zones.append(list(data.xs(i))[0]['zone'])
    hadf = pd.DataFrame()
    hadf['District'] = districts
    hadf['Zone'] = zones
    df = df.merge(hadf)
    bool_list = df['State'] == value
    df = df[bool_list]
    return df
@app.callback(Output('tabs', 'children'),
              [Input('drop', 'value')])
def tab(value):
    if value=='world':
        return dcc.Tabs(id='tabs-table',
                        value='All',
                        children=[
                            dcc.Tab(label='All', value='All', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='Europe', value='Europe', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='North America', value='North America', style=s1, selected_style=s2),
                            dcc.Tab(label='South America', value='South America', style=s1, selected_style=s2),
                            dcc.Tab(label='Asia', value='Asia', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='Africa', value='Africa', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='Oceania', value='Oceania', style=tab_style, selected_style=tab_selected_style)
                        ]
                )
    else:
        print('gone through')
        return dcc.Tabs(id='india-tabs',
                        value='States',
                        children=[
                            dcc.Tab(label='States', value='States', style=tab_style, selected_style=tab_selected_style),
                            dcc.Tab(label='Districts', value='Districts', style=tab_style, selected_style=tab_selected_style)
                        ]
                )

@app.callback(Output('dropper-ind', 'children'),
            [Input('drop', 'value'),
            Input('india-tabs', 'value'),
            Input('interval-component', 'n_intevals')])
def dop(v1, v2, nernw):
    if v1 == 'india' and v2 == 'Districts':
        op = []
        ###############################
        lst =  ['Andaman and Nicobar Islands', 'Andhra Pradesh',
        'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
        'Chhattisgarh', 'Delhi',
        'Dadra and Nagar Haveli and Daman and Diu', 'Goa', 'Gujarat',
        'Himachal Pradesh', 'Haryana', 'Jharkhand', 'Jammu and Kashmir',
        'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Maharashtra',
        'Meghalaya', 'Manipur', 'Madhya Pradesh', 'Mizoram', 'Nagaland',
        'Odisha', 'Punjab', 'Puducherry', 'Rajasthan', 'Sikkim',
        'Telangana', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh',
        'Uttarakhand', 'West Bengal']
        for n in lst:
            op.append({'label':n, 'value':n})
        return dcc.Dropdown(
                    id='dhop',
                    options=op,
                    value='Andaman and Nicobar Islands',
                    style=dict(width='40%')
                )
    else:
        pass
@app.callback([Output('table_div', 'style'),
            Output('tablet_div', 'style'),
            Output('name99', 'style'),
            Output('name88', 'style')],
            [Input('drop', 'value')])
def anakin(valet):
    if valet == 'india':
        return  {'display':'none'}, {'display':'block'}, \
                {'display':'none'}, {'display':'block'}
    elif valet == 'world':
        return {'display':'block'}, {'display':'none'}, \
               {'display':'block'}, {'display':'none'}



@app.callback([Output('table', 'columns'),
            Output('table', 'data')],
            [Input('tabs-table', 'value'),
            Input('drop', 'value'),
            Input('interval-com', 'n_intervals')])
def hansolo(val, value, nwemmw):
    print(value)
    if value == 'world':
        URL = "https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv"
        df2 = pd.read_csv(URL)
        country2 = list(df2['COUNTRY'])
        r = 0
        for i in country2:
            if i =='"Bahamas, The"':
                country2[r] = 'Bahamas'
            elif i == '"Congo, Democratic Republic of the"':
                country2[r] = 'DRC'
            elif i == '"Congo, Republic of the"':
                country2[r] = 'Congo'
            elif i == '"Gambia, The"':
                country2[r] = 'Gambia'
            elif i == '"Korea, North"':
                country2[r] = 'North Korea'
            elif i == '"Korea, South"':
                country2[r] = 'S. Korea'
            elif i == 'Virgin Islands':
                country2[r] = 'British Virgin Islands'
            elif i == 'United States':
                country2[r] = 'USA'
            elif i == 'United Kingdom':
                country2[r] = 'UK'
            elif i == 'United Arab Emirates':
                country2[r] = 'UAE'
            elif i == 'Saint Vincent and the Grenadines':
                country2[r] = 'St. Vincent Grenadines'
            elif i == 'Saint Pierre and Miquelon':
                country2[r] = 'Saint Pierre Miquelon'
            r+=1
        url = "https://www.worldometers.info/coronavirus/#countries"

        web_content = requests.get(url).content
        # parse the html content
        soup = bs(web_content, "html.parser")
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
            "Deaths/1M pop", "Total Tests", "Tests/1M pop", "Population", "Continent", "1 case every X ppl", 
            "1 Death every X ppl", "1 Test every X ppl"]
        df = pd.DataFrame(data=stats, columns=ncols)
        ndf = df
        country = list(ndf['Country'])
        ncountry = []
        x = 0
        for i in country:
            if i not in country2:
                ncountry.append(x)
            x+=1
        vdf = ndf.drop(ncountry)
        vdf.drop_duplicates(subset ="Country", keep = 'last', inplace = True)
        ndf=vdf
        ndf['Cases'] = ndf['Cases'].str.replace(',','')
        ndf['Cases'] = ndf['Cases'].apply(pd.to_numeric)
        ndf['Continent'] = ndf['Continent'].str.replace('Australia/Oceania', 'Oceania')
        vst(df)
        ls = [vdf[x] for x in ncols]
        ncols = [{'name': col, 'id': col} for col in vdf.columns]
        data=vdf.to_dict(orient = 'records')
        index = [x for x in range(len(list(vdf['Country'])))]
        def fun(val, ndf):
            asia = []
            x=0
            for i in ndf['Continent']:
                if i == val:
                    asia.append(x)
                x+=1
            ndf = ndf.reset_index()
            dec = list(range(len(ndf['Country'])))
            diff = list(set(dec) - set(asia))
            ndf = ndf.drop('index', axis=1)
            data1 = ndf.drop(diff)
            return data1
        if val != 'All':
            data1 = fun(val, ndf)
            data = data1.to_dict(orient='records')
            vst(data1)

        return ncols, data #, {'display':'none'}, {'display':'block'}





@app.callback([Output('tablet', 'columns'),
            Output('tablet', 'data'),
            Output('tablet', 'style_data_conditional')],
#            Output('table_div', 'style')],
            [Input('india-tabs', 'value'),
            Input('dhop', 'value')])
def lukeskywalker(i_tabs, i_drop):
    # print('hell " o ')
    # return [1,2,3], [1,2,3]
    print('entered')
    print(i_tabs)
    if i_tabs == 'States':
        print('hellllllllllllofwrfkr3jgklr4tgkg45g4kglkl4')
#        url = 'https://www.mohfw.gov.in/'

#        web_content = requests.get(url).content
#        soup = bs(web_content, "html.parser")
#        extract_contents = lambda row: [x.text.replace('\n', '') for x in row]
#        stats = []
#        all_rows = soup.find_all('tr')
#        for row in all_rows:
#            stat = extract_contents(row.find_all('td'))
#            print(len(stat))
#            if len(stat) == 6:
#                stats.append(stat)
#        ncols = ["Sr.No", "States/UT", "Active", "Recovered","Deceased","Confirmed"]
#        state_data = pd.DataFrame(data = stats, columns = ncols)
#        print(stats)
        URL = 'https://api.covid19india.org/csv/latest/state_wise.csv'
        page = requests.get(URL).content
        df = pd.read_csv(io.StringIO(page.decode('utf-8')))
        ncols = ['State', 'Confirmed', 'Recovered', 'Deaths', 'Active']
        df = df[ncols]
#        df['Confirmed'] = df['Confirmed'].apply(pd.to_numeric)
        vst(df)
        ncols = [{'name': col, 'id': col} for col in df.columns]
        data=list(df.to_dict("records"))
        print(ncols, data)
        return ncols, data, []
    elif i_tabs == 'Districts':
        df = get_dist(i_drop)
        vst(df)
        data=list(df.to_dict("records"))
        ncols = [{'name':col, 'id':col} for col in df.columns]
        return ncols, data, [
                {
                    'if': {
                        'filter_query': '{Zone} = Red',
                        'columns_id': 'Zone'
                    },
                    'color': 'red'
                },
                {
                    'if': {
                        'filter_query': '{Zone} = Orange',
                        'columns_id': 'Zone'
                    },
                    'color': 'orange'
                },
                {
                    'if': {
                        'filter_query': '{Zone} = Green',
                        'columns_id': 'Zone'
                    },
                    'color': 'green'
                }
            ]


@app.callback(Output('name99', 'children'),
            [Input('drop', 'value'),
            Input('tabs-table', 'value')])
def lint1(ur, utp):
    vent = time.time()
    call_name_time(vent)
    return html.A(id = 'nen', children = [html.Button('Download Data as xlsx')], href = 'https://novelcovid19tracker.herokuapp.com/table/corona-report/urlToDownload?value={}'.format(str(vent)))

@app.callback(Output('name88', 'children'),
            [Input('india-tabs', 'value'),
            Input('dhop', 'value')])
def lint2(ur2, utp2):
    vent = time.time()
    call_name_time(vent)
    return html.A(id = 'nen2', children = [html.Button('Download Data as xlsx')], href = 'https://novelcovid19tracker.herokuapp.com/table/corona-report/urlToDownload?value={}'.format(str(vent)))


def r():
    return ret

@app.server.route('/corona-report/urlToDownload')
def ex():
    kf = r()
    print('ha!')
    strIO = io.BytesIO()
    excel_writer = pd.ExcelWriter(strIO, engine="xlsxwriter")
    kf.to_excel(excel_writer, sheet_name="sheet1")
    excel_writer.save()
    excel_data = strIO.getvalue()
    strIO.seek(0)
    return send_file(strIO,
                     attachment_filename='Output.xlsx',
                     as_attachment=True)
app.title = 'Corona Tracker'

if __name__ == '__main__':
    app.run_server(debug=False)
