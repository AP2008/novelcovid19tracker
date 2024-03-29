import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash_defer_js_import import Import
import extras

main = f"{extras.root}/"

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
    navlinks = [
                        # DONE
                        dbc.NavLink("Home", href=f"{main}",   active=(ap == "Home")),
                        # DONE
                        dbc.NavLink("Timeline", href=f"{main}timeline/",   active=(ap == "Timeline")),
                        # DONE
                        dbc.NavLink("DataTable", href=f"{main}table/",   active=(ap == "DataTable")),
                        # DONE
                        dbc.NavLink("Map", href=f"{main}map/",   active=(ap == "Map")),
                        # DONE
                        dbc.NavLink("Counter", href=f"{main}counter/",   active=(ap == "Counter")),
                        # DONE
                        dbc.NavLink("Growth", href=f"{main}growth/",   active=(ap == "Growth")),
                        # DONE
                        dbc.NavLink("Vaccine", href=f"{main}vaccine/",   active=(ap == "Vaccine")),
                        # DONE
                        dbc.NavLink("Infocenter", href=f"{main}infocentre/",   active=(ap == "Infocenter")),
                        # DONE
                        dbc.NavLink("About", href=f"{main}aboutme/",   active=(ap == "About"))
    ]
    Lis = []
    for n in ["Home", "Timeline", "DataTable", "Map", "Counter", "Growth", "Vaccine", "Infocenter", "About"]:
        if ap == n:
            Lis.append(html.Li(html.A(n, href=f"{main}{n.lower() if n != 'Home' else ''}", className="act-link")))
        else:
            Lis.append(html.Li(html.A(n, href=f"{main}{n.lower()}")))
    Lis.append(
        html.A(
            html.Img(
                src="https://cdn.ko-fi.com/cdn/kofi3.png?v=2",
                style="border:0px;height:36px;",
                height=36,
                alt='Buy Me a Coffee at ko-fi.com'
            ),
            href="https://ko-fi.com/R6R84J2II",
            target="_blank"
        )
    )
    navbar = html.Div([
        html.Div([
            html.H2("NavBar", className="display-4", style={'color':'black'}),
            html.Hr(),
            dbc.Nav(
                navlinks,
                vertical=True,
                pills=True,
            ),
            ],
            style=SIDEBAR_STYLE,
            className="nav"
        ),
        html.Div([
            html.Nav(
                html.Div([
                    html.A(
                        "Covid-19",
                        href="#!",
                        className="brand-logo"),
                    html.A(
                        html.I("menu", className="material-icons"),
                        href="#",
                        className="sidenav-trigger",
                        **{
                            'data-target':"mobile-demo"
                            }),
                    html.Ul(Lis, className="right hide-on-med-and-down")
                        ], className="nav-wrapper")),
                    html.Ul(
                        Lis, className="sidenav", id="mobile-demo"),
                    Import(src="https://thunder2020.pythonanywhere.com/assets/nen.js")
        #html.Div([
#            dbc.NavbarSimple(
#                navlinks,
#                color="dark",
#                brand="Corona Tracker",
#                dark=True
#            )
        ], className="topnav", style={'align': 'left'})
    ])
    return navbar

