import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

main = "http://thunder2020.pythonanywhere.com/"

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

def navbar(ap):
    navbar = html.Div([
        html.H2("NavBar", className="display-4", style={'color':'black'}),
        html.Hr(),
        dbc.Nav(
            [
                # DONE
                dbc.NavLink("Home", href=f"{main}", id="page-1-link", style={'color': 'black'}, active=(ap == "Home")),
                # DONE
                dbc.NavLink("Timeline", href=f"{main}timeline/", id="page-2-link", style={'color': 'black'}, active=(ap == "Timeline")),
                # DONE
                dbc.NavLink("DataTable", href=f"{main}table/", id="page-3-link", style={'color': 'black'}, active=(ap == "DataTable")),
                # DONE
                dbc.NavLink("Map", href=f"{main}map/", id="page-4-link", style={'color': 'black'}, active=(ap == "Map")),
                # DONE
                dbc.NavLink("Counter", href=f"{main}counter/", id="page-6-link", style={'color': 'black'}, active=(ap == "Counter")),
                # DONE
                dbc.NavLink("Growth", href=f"{main}growth/", id="page-7-link", style={'color': 'black'}, active=(ap == "Growth")),
                # DONE
                dbc.NavLink("Infocenter", href=f"{main}infocentre/", id="page-8-link", style={'color': 'black'}, active=(ap == "Infocenter")),
                # # 0%
                # dbc.NavLink("Newsletter", href="https://covid19tracknow.herokuapp.com/letter/", id="page-9-link"),
                # Done
                dbc.NavLink("About", href=f"{main}aboutme/", id="page-10-link", style={'color': 'black'}, active=(ap == "About"))
            ],
            vertical=True,
            pills=True,
        ),
        ],
        style=SIDEBAR_STYLE
    )
    return navbar

