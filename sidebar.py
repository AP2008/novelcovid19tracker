import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

navbar = html.Div([
    html.H2("NavBar", className="display-4", style={'color':'black'}),
    html.Hr(),
    dbc.Nav(
        [
            # DONE
            dbc.NavLink("Home", href="https://novelcovid19tracker.herokuapp.com/home/", id="page-1-link"),
            # DONE
            dbc.NavLink("Timeline", href="https://novelcovid19tracker.herokuapp.com/timeline/", id="page-2-link"),
            # DONE
            dbc.NavLink("DataTable", href="https://novelcovid19tracker.herokuapp.com/table/", id="page-3-link"),
            # DONE
            dbc.NavLink("Map", href="https://novelcovid19tracker.herokuapp.com/map/", id="page-4-link"),
            # DONE
            dbc.NavLink("Counter", href="https://novelcovid19tracker.herokuapp.com/counter/", id="page-6-link"),
            # DONE
            dbc.NavLink("Growth", href="https://novelcovid19tracker.herokuapp.com/growth/", id="page-7-link"),
#             # 0%
            # dbc.NavLink("InfoCenter", href="https://covid19tracknow.herokuapp.com/info/", id="page-8-link"),
            # # 0%
            # dbc.NavLink("Newsletter", href="https://covid19tracknow.herokuapp.com/letter/", id="page-9-link"),
            # # 0%
            # dbc.NavLink("About", href="https://covid19tracknow.herokuapp.com/about/", id="page-10-link")
        ],
        vertical=True,
        pills=True,
    ),
    ],
    style=SIDEBAR_STYLE
)
app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])
app.layout = html.Div([navbar])

if __name__=='__main__':
    app.run_server(debug=False)

