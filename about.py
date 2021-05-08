from web_scrape import *
from modules import *
from sidebar import *
import extras

external_stylesheets = [extras.theme]

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

sn = {'color':'white'}

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/about/')

CONTENT_STYLE = {
    "margin-left": "1rem",
    "margin-right": "1rem",
    'color': '#FFFFFF'
}

app.layout = html.Div([
    html.Base(target="_parent"),
    html.Div([
        navbar("About")
    ]),
    html.Div([
        html.Center([
            html.Img(src=app.get_asset_url('profile.jpg'), style={'width':'180px', 'height':'180px', 'border-radius': '50%'}),
            dbc.CardBody([
                html.H4('Aratrik Pal', style=sn)
            ])
        ]),
        html.Div([
            html.Ol([
                html.Li("Hi, I am Aratrik Pal."),
                html.Li("I am 13 years old."),
                html.Li("I live in India"),
                html.Li("I like programming and maths"),
                html.Li("I created this website"),
                html.Li(["You can contact me at: ", html.A("aratrik.pal@gmail.com", href="mailto:aratrik.pal@gmail.com")]),
                html.Li(["My Github User ID is : ", html.A("AP2008", href="https://github.com/AP2008")]),
                html.Li(["The Source for the data of this website are : ", html.A("Covid 19 India", href="https://www.covid19india.org/"), ", ",
                                                                           html.A("Owid Covid Data", href="https://github.com/owid/covid-19-data/"), ", ",
                                                                           html.A("Covid 19 Api", href="https://covid19api.com/"), ", ",
                                                                           html.A("WHO", href="https://who.int/emergencies/diseases/novel-coronavirus-2019")])
            ])
        ])
    ])
], style=CONTENT_STYLE)

app.index_string = extras.ind_str
app.title="Corona Tracker"

if __name__ == '__main__':
    app.run_server(debug=False)

