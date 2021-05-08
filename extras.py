from modules import *
theme = dbc.themes.SUPERHERO
root = "https://novcov19.ml"

def getip():
    country = requests.get("http://ip-api.com/json/{}?fields=countryCode".format(request.headers.get('X-Forwarded-For'))).json()["countryCode"]
    return country

ind_str = """
<!DOCTYPE html>
<html>
    <head>
        <meta name="description" content="This website gives the latest data and visualizations of the Novel Covid 19 Virus.">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script async src="https://arc.io/widget.min.js#LHbAsxJ6"></script>
        <script type='text/javascript' src='https://platform-api.sharethis.com/js/sharethis.js#property=60597de1f6067000116b078b&product=sop' async='async'></script>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-BVFL2XTDQ8"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-BVFL2XTDQ8');
        </script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
    </head>
    <body>
        <base target="_parent"></base>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""