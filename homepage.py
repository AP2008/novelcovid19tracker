from modules import *
from sidebar import *
from cop import create_cop
import extras

external_stylesheets = [extras.theme] #'https://codepen.io/chriddyp/pen/bWLwgP.css']
sn = {'color':'white'}


app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/home/')
CORONA_LOGO = 'https://cdn.cnn.com/cnnnext/dam/assets/200204130938-cdc-coronavirus-illustration-exlarge-169.jpg'
app.layout = html.Div(children=[
    html.Div(id="PEST"),
        navbar("Home"),
        html.Div([
            dbc.Row(
                dbc.Col(
                    html.Center(html.H1('Corona Tracker', id="n-c"))
                    #width={'offset': 3.3}
                ),
                no_gutters=True
            ),
#            dcc.Interval(id="i-c", interval=3*1000, n_intervals=0),
#            html.Div([
#                dbc.Navbar([
#                    html.A(
#                        dbc.Row([
#                            dbc.Col(html.Img(src=CORONA_LOGO, height="30px", className="responsive")),
#                            dbc.Col(dbc.ButtonGroup([
#                                        dbc.Button("Home", href="https://thunder2020.pythonanywhere.com/", color='success'),
#                                        dbc.Button("Timeline", href="https://thunder2020.pythonanywhere.com/timeline/", color='success'),
#                                        dbc.Button("Map", href="https://thunder2020.pythonanywhere.com/map/", color='success'),
#                                        dbc.Button("DataTable", href="https://thunder2020.pythonanywhere.com/table/", color='success'),
#                                        dbc.Button("Counter", href="https://thunder2020.pythonanywhere.com/counter/", color='success'),
#                                        dbc.Button("Growth", href="https://thunder2020.pythonanywhere.com/growth/", color='success'),
#                                        dbc.Button("Infocenter", href="https://thunder2020.pythonanywhere.com/infocentre/", color='success'),
#                                        dbc.Button("About", href="https://thunder2020.pythonanywhere.com/aboutme/", color='success')
#                                    ], size='lg', className='mr-1'), align='right')
#                        ])
#                )
#                ], color="dark", dark=True)
#            ]),
            dbc.Row([
                dbc.Col(
                    dbc.Card([
#                        html.Iframe(src=https://thunder2020.pythonanywhere.com/timeline", width=300, height=800),
                        dbc.Button(dbc.CardImg(src=app.get_asset_url('bar_g.jpg'), className="responsive"), href='https://thunder2020.pythonanywhere.com/timeline'),
                        dbc.CardBody([
                            html.H4('Timeline', style=sn),
                            html.P('The TIMELINE page shows the Covid-19 data of most of the countries as a time-series.', style=sn),
                            dbc.Button('Timeline', color='primary', href='https://thunder2020.pythonanywhere.com/timeline', size='lg')
                        ])
                    ], className="z-depth-3"), width=12, lg=4),
                dbc.Col(
                    dbc.Card([
                        dbc.Button(dbc.CardImg(src=app.get_asset_url('counter_g.jpg'), className="responsive"), href='https://thunder2020.pythonanywhere.com/counter'),
                        dbc.CardBody([
                            html.H4('Counter', style=sn),
                            html.P('The COUNTER page shows the Worldwide Covid-19 cases, deaths and recoveries. You can also choose a country to show its statistics.', style=sn),
                            dbc.Button('Counter', color='primary', href='https://thunder2020.pythonanywhere.com/counter', size='lg')
                        ])
                    ], className="z-depth-3")
                , width=12, lg=4),
                dbc.Col(
                    dbc.Card([
                        dbc.Button(dbc.CardImg(src=app.get_asset_url('table_g.jpg'), className="responsive"), href='https://thunder2020.pythonanywhere.com/datatable'),
                        dbc.CardBody([
                            html.H4('Data Table', style=sn),
                            html.P('The TABLE page shows the COVID-19 data of India district-wise and state-wise. It also shows the World COVID-19 data continent-wise.', style=sn),
                            dbc.Button('Table', color='primary', href='https://thunder2020.pythonanywhere.com/table', size='lg')
                        ])
                    ], className="z-depth-3"),
                width=12, lg=4),
            dbc.Col(
                dbc.Card([
                    dbc.Button(dbc.CardImg(src=app.get_asset_url('map_g.jpg'), className="responsive"), href='https://thunder2020.pythonanywhere.com/map'),
                    dbc.CardBody([
                        html.H4('Choropleth map', style=sn),
                        html.P('The MAP page shows a Choropleth map of the confirmed cases in India state-wise and the confirmed cases of most of the countries.', style=sn),
                        dbc.Button('Choropleth Map', color='primary', href='https://thunder2020.pythonanywhere.com/map', size='lg')
                    ])
                ], className="z-depth-3"),
                width=12, lg=4),
            dbc.Col(
                dbc.Card([
                    dbc.Button(dbc.CardImg(src=app.get_asset_url('growth.png'), className="responsive"), href='https://thunder2020.pythonanywhere.com/growth'),
                    dbc.CardBody([
                        html.H4('Growth', style=sn),
                        html.P('The GROWTH page shows the new confirmed , deaths, recoveries and active cases of most of the countries.', style=sn),
                        dbc.Button('Growth', color='primary', href='https://thunder2020.pythonanywhere.com/growth', size='lg')
                    ])
                ], className="z-depth-3"),
                width=12, lg=4),
            dbc.Col(
                dbc.Card([
                    dbc.Button(dbc.CardImg(src=app.get_asset_url('Infocentre.png'), className="responsive"), href='https://thunder2020.pythonanywhere.com/infocenter'),
                    dbc.CardBody([
                        html.H4('Infocenter', style=sn),
                        html.P("The INFOCENTER gives information on Covid-19, it's symptoms, vaccination and prevention", style=sn),
                        dbc.Button("Infocenter", color='primary', href='https://thunder2020.pythonanywhere.com/infocentre', size='lg')
                    ])
                ], className="z-depth-3"),
                width=12, lg=4)]),
            # dbc.Col(
                # dbc.Card([, className="z-depth-3"
                    # dbc.CardImg(src=app.get_asset_url('counter_g.jpg')),
                    # dbc.CardBody([
                        # html.H4('Counter', style=sn),
                        # html.P('The COUNTER page shows the Worldwide Covid-19 cases, deaths and recoveries. You can also choose a country to show its statistics.', style=sn),
                        # dbc.Button('Counter', color='primary', href='http://127.0.0.1:8080/counter', size='lg')
                    # ])
                # ]),
                # width=12
            # )
html.Div([create_cop(app)])

])])



#@app.callback(Output('PEST', 'children'),
#              [Input('inc', 'n_intervals')])
#def fU_HAN_LUKE_CORRAN(n):
#    page = requests.get('https://news.google.com/search?q=coronavirus')
#    soup = bs(page.content, 'html.parser')
#    results = soup.find_all('a', class_='VDXfz')
#
#    dic = []
#
#    n = 0
#    print(len(results))
#    for i, res in enumerate(results):
#        print(i, n)
#        if n > 19:
#            break
#        try:
#            k = res["href"][1:]
#            link = "https://news.google.com" + k
#            page = requests.get(link, verify=False)
#            if str(page) != '<Response [200]>':
#                raise EOFError
#            soup = bs(page.content, 'html.parser')
#            title_html = str(soup.find_all('h1')[0])
#            title = title_html.split('>')[1].split('<')[0].strip()
#            dic.append((title, link))
#            n += 1
#        except:
#            pass
#    chill1 = []
#    for x in range(20):
#        chill1.append(
#                html.A(dic[x][0], href=dic[x][1], style={'color':'red'})
#        )
#        chill1.append(
#                html.A('|||', style={'color':'grey'})
#        )
#    return html.Marquee(chill1)

#@app.callback(Output("ROW12", "children"),
#              [Input("i-c", "n-intervals")])
#def hkhk(a):
#    country = extras.getip()
#    h = requests.get("http://api.covid19api.com/summary", verify=False).json()
#    n = pd.DataFrame.from_dict(h["Countries"])
#    c = n.loc[n["CountryCode"] == country]
#    a1 = dbc.Col(dbc.Alert([
#        html.H4("Total Confirmed Cases in {}".format(c["Country"].to_list()[0]), className="alert-heading"),
#        html.Hr(),
#        daq.LEDDisplay(value=int(c["TotalConfirmed"])),
#        ], className="alert-dark"))
#    a2 = dbc.Col(html.Center(html.H1("Corona Tracker", style=sn), style={"padding-top": "23px"}))
#    a3 = dbc.Col(dbc.Alert([
#        html.H4("Total Confirmed Deaths in {}".format(c["Country"].to_list()[0]), className="alert-heading"),
#        html.Hr(),
#        daq.LEDDisplay(value=int(c["TotalDeaths"])),
#        ], className="alert-dark"))
#
#
#    return [a1,a2,a3]
app.index_string = extras.ind_str
#"""<!DOCTYPE html>
#<html>
#    <head>
#        <meta name="description" content="This website gives the latest data and visualizations of the Novel Covid 19 Virus.">
#        <meta name="viewport" content="width=device-width, initial-scale=1.0">
#        <script async src="https://arc.io/widget.min.js#LHbAsxJ6"></script>
#        <script type='text/javascript' src='https://platform-api.sharethis.com/js/sharethis.js#property=60397de1f6067000116b078b&product=sop' async='async'></script>
#        <!-- Global site tag (gtag.js) - Google Analytics -->
#        <script async src="https://www.googletagmanager.com/gtag/js?id=G-BVFL2XTDQ8"></script>
#        <script>
#        window.dataLayer = window.dataLayer || [];
#        function gtag(){dataLayer.push(arguments);}
#        gtag('js', new Date());
#
#        gtag('config', 'G-BVFL2XTDQ8');
#        </script>
#        {%metas%}
#        <title>{%title%}</title>
#        {%favicon%}
#        {%css%}
#    </head>
#    <body>
#        {%app_entry%}
#        <footer>
#            {%config%}
#            {%scripts%}
#            {%renderer%}
#        </footer>
#    </body>
#</html>"""
app.title = 'Corona Tracker'
if __name__ == '__main__':
    app.run_server(debug=False)
