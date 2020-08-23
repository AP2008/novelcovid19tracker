from modules import *
from sidebar import *
from cop import create_cop

external_stylesheets = [dbc.themes.SOLAR, 'https://codepen.io/chriddyp/pen/bWLwgP.css']
sn = {'color':'white'}


app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets, requests_pathname_prefix='/home/')
CORONA_LOGO = 'https://cdn.cnn.com/cnnnext/dam/assets/200204130938-cdc-coronavirus-illustration-exlarge-169.jpg'
#app.scripts.append_script({'external_url': 'https://novelcovid19tracker.herokuapp.com/assets/gtag.js'})
app.layout = html.Div(children=[
    html.Div([
        html.Div([
            dbc.Row(
                dbc.Col(
                    html.H1('COVID - 19 Tracker', style=sn),
                    width={'size': 6, 'offset': 4}
                )
            ),
            html.Div([
                dbc.Navbar([
                    html.A(
                        dbc.Row([
                            dbc.Col(html.Img(src=CORONA_LOGO, height="30px")),
                            dbc.Col(dbc.ButtonGroup([
                                        dbc.Button("Home", href="https://novelcovid19tracker.herokuapp.com/home/", color='success'),
                                        dbc.Button("Timeline", href="https://novelcovid19tracker.herokuapp.com/timeline/", color='success'),
                                        dbc.Button("Map", href="https://novelcovid19tracker.herokuapp.com/map/", color='success'),
                                        dbc.Button("DataTable", href="https://novelcovid19tracker.herokuapp.com/table/", color='success'),
                                        dbc.Button("Counter", href="https://novelcovid19tracker.herokuapp.com/counter/", color='success'),
                                        dbc.Button("Growth", href="https://novelcovid19tracker.herokuapp.com/growth/", color='success')
                                    ], size='lg', className='mr-1'), align='right')
                        ])
                )
                ], color="dark", dark=True)
            ]),
            html.Div([
                html.Div([
                    dbc.Card([
                        dbc.Button(dbc.CardImg(src=app.get_asset_url('bar_g.jpg')), href='https://novelcovid19tracker.herokuapp.com/timeline'),
                        dbc.CardBody([
                            html.H4('Timeline', style=sn),
                            html.P('The TIMELINE page shows the Covid-19 data of most of the countries as a time-series.', style=sn),
                            dbc.Button('Timeline', color='primary', href='https://novelcovid19tracker.herokuapp.com/timeline', size='lg')
                        ])
                    ]),
                ], className='four columns'),
                html.Div([
                    dbc.Card([
                        dbc.Button(dbc.CardImg(src=app.get_asset_url('counter_g.jpg')), href='https://novelcovid19tracker.herokuapp.com/counter'),
                        dbc.CardBody([
                            html.H4('Counter', style=sn),
                            html.P('The COUNTER page shows the Worldwide Covid-19 cases, deaths and recoveries. You can also choose a country to show its statistics.', style=sn),
                            dbc.Button('Counter', color='primary', href='https://novelcovid19tracker.herokuapp.com/counter', size='lg')
                        ])
                    ])
                ], className='four columns'),
                # html.Div([
                    # dbc.Card([
                        # dbc.Button(dbc.CardImg(src=app.get_asset_url('map_g.jpg')), href='https://novelcovid19tracker.herokuapp.com/map'),
                        # dbc.CardBody([
                            # html.H4('Choropleth map', style=sn),
                            # html.P('The MAP page shows a Choropleth map of the confirmed cases in India state-wise and the confirmed cases of most of the countries.', style=sn),
                            # dbc.Button('Choropleth Map', color='primary', href='https://novelcovid19tracker.herokuapp.com/map', size='lg')
                        # ])
                    # ]),
                # ], className='four columns'),
                html.Div([
                    dbc.Card([
                        dbc.Button(dbc.CardImg(src=app.get_asset_url('table_g.jpg')), href='https://novelcovid19tracker.herokuapp.com/table'),
                        dbc.CardBody([
                            html.H4('Data Table', style=sn),
                            html.P('The TABLE page shows the COVID-19 data of India district-wise and state-wise. It also shows the World COVID-19 data continent-wise.', style=sn),
                            dbc.Button('Table', color='primary', href='https://novelcovid19tracker.herokuapp.com/table', size='lg')
                        ])
                    ]),
                ], className='four columns')
            ], className='row'),
            # html.Div([
                # html.Div([
                    # dbc.Card([
                        # dbc.Button(dbc.CardImg(src=app.get_asset_url('counter_g.jpg')), href='https:/novelcovid19tracker.herokuapp.com/counter'),
                        # dbc.CardBody([
                            # html.H4('Counter', style=sn),
                            # html.P('The COUNTER page shows the Worldwide Covid-19 cases, deaths and recoveries. You can also choose a country to show its statistics.', style=sn),
                            # dbc.Button('Counter', color='primary', href='https:/novelcovid19tracker.herokuapp.com/counter', size='lg')
                        # ])
                    # ])
                # ], className='four columns')
            # ], className='row'),
            html.Div([
                dbc.Card([
                    dbc.Button(dbc.CardImg(src=app.get_asset_url('map_g.jpg')), href='https://novelcovid19tracker.herokuapp.com/map'),
                    dbc.CardBody([
                        html.H4('Choropleth map', style=sn),
                        html.P('The MAP page shows a Choropleth map of the confirmed cases in India state-wise and the confirmed cases of most of the countries.', style=sn),
                        dbc.Button('Choropleth Map', color='primary', href='https://novelcovid19tracker.herokuapp.com/map', size='lg')
                    ])
                ], className='six columns'),
                dbc.Card([
                    dbc.Button(dbc.CardImg(src=app.get_asset_url('growth.png')), href='https://novelcovid19tracker.herokuapp.com/growth'),
                    dbc.CardBody([
                        html.H4('Growth', style=sn),
                        html.P('The GROWTH page shows the new confirmed , deaths, recoveries and active cases of most of the countries.', style=sn),
                        dbc.Button('Growth', color='primary', href='https://novelcovid19tracker.herokuapp.com/growth', size='lg')
                    ])
                ], className='six columns')
            ], className='row')
            # dbc.Col(
                # dbc.Card([
                    # dbc.CardImg(src=app.get_asset_url('counter_g.jpg')),
                    # dbc.CardBody([
                        # html.H4('Counter', style=sn),
                        # html.P('The COUNTER page shows the Worldwide Covid-19 cases, deaths and recoveries. You can also choose a country to show its statistics.', style=sn),
                        # dbc.Button('Counter', color='primary', href='http://127.0.0.1:8080/counter', size='lg')
                    # ])
                # ]),
                # width=4
            # )
        ])
    ]),
html.Div([create_cop(app)])

])



#@app.callback(Output('PEST', 'children'),
#              [Input('interval-component', 'n_intervals')])
#def fU_HAN_LUKE_CORRAN(n):
#    page = requests.get('https://news.google.com/search?q=coronavirus')
#    soup = bs(page.content, 'html.parser')
#   results = soup.find_all('a', class_='VDXfz')
#
#    dic = []
#
 #   n = 0
 #   print(len(results))
 #   for i, res in enumerate(results):
 #       print(i, n)
 #       if n > 19:
#            break
#        try:
#            res = str(res)
#            http_ = res.split('http')[1]
#            link = 'http' + http_.split(';')[0]
#            page = requests.get(link)
#            if str(page) != '<Response [200]>':
#                raise EOFError
#            soup = bs(page.content, 'html.parser')
#            title_html = str(soup.find_all('h1')[0])
#            title = title_html.split('>')[1].split('<')[0]
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
app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-168248200-1"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('js', new Date());

          gtag('config', 'UA-168248200-1');
        </script>
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
