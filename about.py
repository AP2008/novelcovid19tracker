from web_scrape import *
from modules import *
from sidebar import *

external_stylesheets = [dbc.themes.SOLAR, 'https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

sn = {'color':'white'}

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets)

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
    dbc.Card([
        dbc.CardImg(src=app.get_asset_url('profile.jpg'), top=True,
                    style={'width':'100px', 'height':'100px'}),
        dbc.CardBody([
            html.H4('Aratrik Pal', style=sn)
        ])
    ])
])


if __name__ == '__main__':
    app.run_server(debug=False)

