from modules import *
theme = dbc.themes.SUPERHERO

def getip():
    country = requests.get("http://ip-api.com/json/{}?fields=countryCode".format(request.headers.get('X-Forwarded-For'))).json()["countryCode"]
    return country