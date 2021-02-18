import dash_html_components as html
import dash_bootstrap_components as dbc

def create_cop(app):
    copo = html.Footer(dbc.Row([html.Img(src=app.get_asset_url('ind.jpg')),
                                html.P("\u00A9 "+" IndDigiTech 2020. All Rights Reserved", style={'color':'white'})]))
    return copo
