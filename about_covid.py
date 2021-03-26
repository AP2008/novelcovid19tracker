from modules import *
from sidebar import *
import extras

external_stylesheets = [extras.theme]

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

CONTENT_STYLE = {
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'color': '#FFFFFF'
}

def make_jumbo(title, text, button_name, hre):
    return dbc.Jumbotron(
        [
            html.H1(title, className="display-3"),
            html.P(text),
            dbc.Button(button_name, color="primary", href=hre, size="lg")
        ])

what_is_covid = make_jumbo(
    "What is COVID-19 ?",
    """
Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.
Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness
and recover without requiring special treatment.  Older people, and those with underlying medical
problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more
likely to develop serious illness.
    """,
    "Learn more",
    "https://www.who.int/emergencies/diseases/novel-coronavirus-2019")

covid_symptoms = make_jumbo(
    "Symptoms",
    [
    "Most common symptoms: fever, dry cough, tiredness.",
    html.Br(),
    "Less common symptoms: aches and pains, sore throat, diarrhoea, conjunctivitis, headache,\
                          loss of taste or smell, a rash on skin, or discolouration of fingers or toes.",
    html.Br(),
    "Serious symptoms    : difficulty breathing or shortness of breath, chest pain or pressure, \
                          loss of speech or movement.",
    html.Br(),
    "On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, \
    however it can take up to 14 days."],
    "Learn more",
    "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19#:~:text=symptoms")

covid_prevention = make_jumbo(
    "Prevention",
    [
        "To prevent infection and to slow transmission of COVID-19, do the following:",
        html.Ul([
            html.Li("Wash your hands regularly with soap and water, or clean them with alcohol-based hand rub."),
            html.Li("Maintain at least 1 metre distance between you and people coughing or sneezing."),
            html.Li("Avoid touching your face."),
            html.Li("Cover your mouth and nose when coughing or sneezing."),
            html.Li("Stay home if you feel unwell."),
            html.Li("Refrain from smoking and other activities that weaken the lungs."),
            html.Li("Practice physical distancing by avoiding unnecessary travel and staying away from large groups of people.")
        ])
    ],
    "Learn more",
    "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public"
)

covid_vaccine = make_jumbo(
    "Vaccination",
    """
There are currently more than 50 COVID-19 vaccine candidates in trials.
When a safe and effective vaccine is found, COVAX (led by WHO, GAVI and CEPI) will facilitate the
equitable access and distribution of these vaccines to protect people in all countries.
People most at risk will be prioritized.
    """,
    "Learn more",
    "https://www.raps.org/news-and-articles/news-articles/2020/3/covid-19-vaccine-tracker"
)

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/infocentre/'
                )

app.layout = html.Div([
    html.Div([navbar("Infocenter")]),
    dbc.Row([
        dbc.Col(html.Div(what_is_covid), width=12, lg=6),
        dbc.Col(html.Div(covid_symptoms), width=12, lg=6),
        dbc.Col(html.Div(covid_prevention), width=12, lg=6),
        dbc.Col(html.Div(covid_vaccine), width=12, lg=6)
    ])
],
style=CONTENT_STYLE,
className="row")

app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script async src="https://arc.io/widget.min.js#LHbAsxJ6"></script>
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