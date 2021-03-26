from modules import *
from web_scrape import *
from sidebar import *
from werkzeug.wsgi import FileWrapper
from flask import Response
import extras

df = pd.DataFrame([[1,2,3],
                   [4,5,6]])
df.columns = ["a", "b", "c"]

start_table_df = pd.DataFrame(columns=[''])

color1 = '#48536D'
color2 = '#5A6D81'

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
    "margin-left": "1rem",
    "margin-right": "1rem",
    #"padding": "2rem 1rem",
}
external_stylesheets = [extras.theme]

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
               requests_pathname_prefix='/datatable/'
)
app.layout = html.Div(children=[
    html.Div([
        navbar("DataTable")
    ]),
html.Div([
    html.Div(id='dropper', children=[
        dcc.Dropdown(
            id='drop',
            options=[
                {'label': 'World', 'value':'world'},
                {'label': 'India', 'value':'india'}
            ],
            value='world',
            searchable=False,
            clearable=False
        )
    ]),
    html.Div(id='tabs', children=[
        dcc.Dropdown(id='tabs-table'),
        dcc.Dropdown(id='india-tabs')
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
            data=start_table_df.to_dict('records'),
            columns = [{'id': c, 'name': c} for c in start_table_df.columns],
            style_header={'backgroundColor': 'rgb(30, 30, 30)','color':'white'},
            style_cell={
                'backgroundColor': color1,
                'color': 'white'
            },
            style_data_conditional = [
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': color2
                },
            ],
            sort_mode="multi",
            row_selectable="multi",
            fixed_rows={'headers': True},
            selected_rows=[],
            page_current=0,
            page_size=20,
            style_table={
                #"overflowY": "auto",
                "overflowX": "auto",
                "height": "80vh",
                "borderRadius": "15px"},
            filter_action="native",
            sort_action="native",

        ),
        dcc.Interval(
            id='interval-com',
            interval=10000000,
            n_intervals=0
            )
    ], className="spb"),
    html.Div(id='tablet_div', children=[
        dash_table.DataTable(
            id='tablet',
            style_header={'backgroundColor': 'rgb(30, 30, 30)','color':'white'},
            style_cell={
                'backgroundColor': color1,
                'color': 'white'
            },
            fixed_rows={'headers': True},
            page_size=20,
#            row_selectable="multi",
#            selected_rows=[],
            style_table={
                #"overflowY": "auto",
                "overflowX": "auto",
                "height": "80vh",
                "borderRadius": "15px"},
            filter_action="native",
            sort_action="native"
        ),
        dcc.Interval(
                    id='interval-component',
                    interval=10000,
                    n_intervals=0
                )
    ], className="spb"),
    html.Div(id="bbbl")
], style=CONTENT_STYLE)
],
#    style={'backgroundColor': colors['background'],
#          'color': colors['text']}
)

@app.callback(Output('bbbl', 'children'),
              [Input('table', 'selected_rows')])
def useless(n):
    return html.P("hi")

zone = 0
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
    page = requests.get(URL, verify=False).content
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
        return dcc.Dropdown(id='tabs-table',
                        value='All',
                        options=[
                            dict(label='All', value='All'),
                            dict(label='Europe', value='Europe'),
                            dict(label='North America', value='North America'),
                            dict(label='South America', value='South America'),
                            dict(label='Asia', value='Asia'),
                            dict(label='Africa', value='Africa'),
                            dict(label='Oceania', value='Oceania')
                        ],
                        searchable=False,
                        clearable=False
                )
    else:
        print('gone through')
        return dcc.Dropdown(id='india-tabs',
                        value='Districts',
                        options=[
                            dict(label='States', value='States'),
                            dict(label='Districts', value='Districts')
                        ],
                        searchable=False,
                        clearable=False
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
                    clearable=False
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
        URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.json"
        df1 = pd.read_json(requests.get(URL, verify=False).content).transpose()
        country = df1["location"]
        ncols = ['location', 'continent', 'total_cases',  'total_deaths', 'new_cases', 'new_deaths', 'total_tests', 'tests_per_case', 'total_vaccinations']
        col_names = ["Country", "Continent", "Confirmed Case", "Confirmed Deaths",
                     "New Cases", "New Deaths", "Total Tests", "Tests / Case", "Total Vaccinations"]
        df2 = df1[ncols]
        df2.columns = col_names
        vst(df2)
        data = list(df2.to_dict(orient = 'records'))
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
            data1 = fun(val, df2)
            data = list(data1.to_dict(orient='records'))
            vst(data1)
        df2 = df2.drop("Continent", axis=1)
        columns = [{'name':col, 'id':col} for col in df2.columns]
        return columns, data
    """
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

        web_content = requests.get(url, verify=False).content
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
        """





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
        URL = 'https://api.covid19india.org/csv/latest/state_wise.csv'
        page = requests.get(URL, verify=False).content
        df = pd.read_csv(io.StringIO(page.decode('utf-8')))
        ncols = ['State', 'Confirmed', 'Recovered', 'Deaths', 'Active']
        df = df[ncols]
        vst(df)
        ncols = [{'name': col, 'id': col} for col in df.columns]
        data=list(df.to_dict("records"))
        print(ncols, data)
        return ncols, data, [
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': color2
                },
            ]
    elif i_tabs == 'Districts':
        df = get_dist(i_drop)
        vst(df)
        data=list(df.to_dict("records"))
        ncols = [{'name':col, 'id':col} for col in df.columns]
        return ncols, data, [
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': color2
                },
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
                    'color': '#FFA500'
                },
                {
                    'if': {
                        'filter_query': '{Zone} = Green',
                        'columns_id': 'Zone'
                    },
                    'color': '#66ff00'
                }
            ]


@app.callback(Output('name99', 'children'),
            [Input('drop', 'value'),
            Input('tabs-table', 'value')])
def lint1(ur, utp):
    vent = time.time()
    call_name_time(vent)
    return dbc.Button('Download Data as xlsx', href = 'http://thunder2020.pythonanywhere.com/table/corona-report/urlToDownload?value={}'.format(str(vent)), color="dark", id="nen")

@app.callback(Output('name88', 'children'),
            [Input('india-tabs', 'value'),
            Input('dhop', 'value')])
def lint2(ur2, utp2):
    vent = time.time()
    call_name_time(vent)
    return dbc.Button('Download Data as xlsx', href = 'http://thunder2020.pythonanywhere.com/table/corona-report/urlToDownload?value={}'.format(str(vent)), color="dark", id="nen2")


def r():
    return ret

@app.server.route('/corona-report/urlToDownload')
def ex():
    kf = r()
    print(kf)
    print('ha!')
    strIO = io.BytesIO()
    excel_writer = pd.ExcelWriter(strIO, engine="xlsxwriter")
    kf.to_excel(excel_writer, sheet_name="sheet1")
    print("Ello")
    excel_writer.close()
    strIO.seek(0)
    w = FileWrapper(strIO)
    #file_wrapper = FileWrapper(excel_writer)
#    headers = {
#        'Content-Disposition': 'attachment; filename=output.xlsx'
#    }
    return Response(w, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", direct_passthrough=True)
app.index_string = extras.ind_str
app.title = 'Corona Tracker'

if __name__ == '__main__':
    app.run_server(debug=False)
