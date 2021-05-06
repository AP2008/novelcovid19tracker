import pandas as pd
import requests
import plotly.graph_objs as go
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from sidebar import *
import extras
import time
from dash.exceptions import PreventUpdate
#from dash_defer_js_import import Import

pt = True
nhj=""
external_stylesheets = [extras.theme]
url_countries = 'https://api.covid19api.com/countries'
page_countries = [
    {
        "Country": "Barbados",
        "Slug": "barbados",
        "ISO2": "BB"
    },
    {
        "Country": "Gibraltar",
        "Slug": "gibraltar",
        "ISO2": "GI"
    },
    {
        "Country": "Lithuania",
        "Slug": "lithuania",
        "ISO2": "LT"
    },
    {
        "Country": "Malaysia",
        "Slug": "malaysia",
        "ISO2": "MY"
    },
    {
        "Country": "Nauru",
        "Slug": "nauru",
        "ISO2": "NR"
    },
    {
        "Country": "Palestinian Territory",
        "Slug": "palestine",
        "ISO2": "PS"
    },
    {
        "Country": "Qatar",
        "Slug": "qatar",
        "ISO2": "QA"
    },
    {
        "Country": "Solomon Islands",
        "Slug": "solomon-islands",
        "ISO2": "SB"
    },
    {
        "Country": "Sri Lanka",
        "Slug": "sri-lanka",
        "ISO2": "LK"
    },
    {
        "Country": "Turks and Caicos Islands",
        "Slug": "turks-and-caicos-islands",
        "ISO2": "TC"
    },
    {
        "Country": "Vanuatu",
        "Slug": "vanuatu",
        "ISO2": "VU"
    },
    {
        "Country": "Wallis and Futuna Islands",
        "Slug": "wallis-and-futuna-islands",
        "ISO2": "WF"
    },
    {
        "Country": "Dominica",
        "Slug": "dominica",
        "ISO2": "DM"
    },
    {
        "Country": "Gambia",
        "Slug": "gambia",
        "ISO2": "GM"
    },
    {
        "Country": "Iran, Islamic Republic of",
        "Slug": "iran",
        "ISO2": "IR"
    },
    {
        "Country": "Namibia",
        "Slug": "namibia",
        "ISO2": "NA"
    },
    {
        "Country": "Tokelau",
        "Slug": "tokelau",
        "ISO2": "TK"
    },
    {
        "Country": "Guinea",
        "Slug": "guinea",
        "ISO2": "GN"
    },
    {
        "Country": "Morocco",
        "Slug": "morocco",
        "ISO2": "MA"
    },
    {
        "Country": "Tunisia",
        "Slug": "tunisia",
        "ISO2": "TN"
    },
    {
        "Country": "Azerbaijan",
        "Slug": "azerbaijan",
        "ISO2": "AZ"
    },
    {
        "Country": "Honduras",
        "Slug": "honduras",
        "ISO2": "HN"
    },
    {
        "Country": "Saint-Martin (French part)",
        "Slug": "saint-martin-french-part",
        "ISO2": "MF"
    },
    {
        "Country": "Chad",
        "Slug": "chad",
        "ISO2": "TD"
    },
    {
        "Country": "Christmas Island",
        "Slug": "christmas-island",
        "ISO2": "CX"
    },
    {
        "Country": "Costa Rica",
        "Slug": "costa-rica",
        "ISO2": "CR"
    },
    {
        "Country": "Bulgaria",
        "Slug": "bulgaria",
        "ISO2": "BG"
    },
    {
        "Country": "Denmark",
        "Slug": "denmark",
        "ISO2": "DK"
    },
    {
        "Country": "Malawi",
        "Slug": "malawi",
        "ISO2": "MW"
    },
    {
        "Country": "Nepal",
        "Slug": "nepal",
        "ISO2": "NP"
    },
    {
        "Country": "Switzerland",
        "Slug": "switzerland",
        "ISO2": "CH"
    },
    {
        "Country": "Canada",
        "Slug": "canada",
        "ISO2": "CA"
    },
    {
        "Country": "China",
        "Slug": "china",
        "ISO2": "CN"
    },
    {
        "Country": "Grenada",
        "Slug": "grenada",
        "ISO2": "GD"
    },
    {
        "Country": "Andorra",
        "Slug": "andorra",
        "ISO2": "AD"
    },
    {
        "Country": "Belgium",
        "Slug": "belgium",
        "ISO2": "BE"
    },
    {
        "Country": "Burkina Faso",
        "Slug": "burkina-faso",
        "ISO2": "BF"
    },
    {
        "Country": "Cayman Islands",
        "Slug": "cayman-islands",
        "ISO2": "KY"
    },
    {
        "Country": "Estonia",
        "Slug": "estonia",
        "ISO2": "EE"
    },
    {
        "Country": "Jersey",
        "Slug": "jersey",
        "ISO2": "JE"
    },
    {
        "Country": "Montserrat",
        "Slug": "montserrat",
        "ISO2": "MS"
    },
    {
        "Country": "Oman",
        "Slug": "oman",
        "ISO2": "OM"
    },
    {
        "Country": "Cameroon",
        "Slug": "cameroon",
        "ISO2": "CM"
    },
    {
        "Country": "Luxembourg",
        "Slug": "luxembourg",
        "ISO2": "LU"
    },
    {
        "Country": "Slovakia",
        "Slug": "slovakia",
        "ISO2": "SK"
    },
    {
        "Country": "Bosnia and Herzegovina",
        "Slug": "bosnia-and-herzegovina",
        "ISO2": "BA"
    },
    {
        "Country": "Moldova",
        "Slug": "moldova",
        "ISO2": "MD"
    },
    {
        "Country": "Brunei Darussalam",
        "Slug": "brunei",
        "ISO2": "BN"
    },
    {
        "Country": "Eritrea",
        "Slug": "eritrea",
        "ISO2": "ER"
    },
    {
        "Country": "Jordan",
        "Slug": "jordan",
        "ISO2": "JO"
    },
    {
        "Country": "Liberia",
        "Slug": "liberia",
        "ISO2": "LR"
    },
    {
        "Country": "Portugal",
        "Slug": "portugal",
        "ISO2": "PT"
    },
    {
        "Country": "Ukraine",
        "Slug": "ukraine",
        "ISO2": "UA"
    },
    {
        "Country": "Indonesia",
        "Slug": "indonesia",
        "ISO2": "ID"
    },
    {
        "Country": "Kenya",
        "Slug": "kenya",
        "ISO2": "KE"
    },
    {
        "Country": "Georgia",
        "Slug": "georgia",
        "ISO2": "GE"
    },
    {
        "Country": "Iceland",
        "Slug": "iceland",
        "ISO2": "IS"
    },
    {
        "Country": "Jamaica",
        "Slug": "jamaica",
        "ISO2": "JM"
    },
    {
        "Country": "Norfolk Island",
        "Slug": "norfolk-island",
        "ISO2": "NF"
    },
    {
        "Country": "French Southern Territories",
        "Slug": "french-southern-territories",
        "ISO2": "TF"
    },
    {
        "Country": "Guernsey",
        "Slug": "guernsey",
        "ISO2": "GG"
    },
    {
        "Country": "Paraguay",
        "Slug": "paraguay",
        "ISO2": "PY"
    },
    {
        "Country": "Tajikistan",
        "Slug": "tajikistan",
        "ISO2": "TJ"
    },
    {
        "Country": "US Minor Outlying Islands",
        "Slug": "us-minor-outlying-islands",
        "ISO2": "UM"
    },
    {
        "Country": "Uzbekistan",
        "Slug": "uzbekistan",
        "ISO2": "UZ"
    },
    {
        "Country": "American Samoa",
        "Slug": "american-samoa",
        "ISO2": "AS"
    },
    {
        "Country": "British Virgin Islands",
        "Slug": "british-virgin-islands",
        "ISO2": "VG"
    },
    {
        "Country": "Finland",
        "Slug": "finland",
        "ISO2": "FI"
    },
    {
        "Country": "Malta",
        "Slug": "malta",
        "ISO2": "MT"
    },
    {
        "Country": "Botswana",
        "Slug": "botswana",
        "ISO2": "BW"
    },
    {
        "Country": "Israel",
        "Slug": "israel",
        "ISO2": "IL"
    },
    {
        "Country": "Saint Lucia",
        "Slug": "saint-lucia",
        "ISO2": "LC"
    },
    {
        "Country": "Spain",
        "Slug": "spain",
        "ISO2": "ES"
    },
    {
        "Country": "Argentina",
        "Slug": "argentina",
        "ISO2": "AR"
    },
    {
        "Country": "Congo (Kinshasa)",
        "Slug": "congo-kinshasa",
        "ISO2": "CD"
    },
    {
        "Country": "Réunion",
        "Slug": "réunion",
        "ISO2": "RE"
    },
    {
        "Country": "Saint-Barthélemy",
        "Slug": "saint-barthélemy",
        "ISO2": "BL"
    },
    {
        "Country": "Zambia",
        "Slug": "zambia",
        "ISO2": "ZM"
    },
    {
        "Country": "Bahrain",
        "Slug": "bahrain",
        "ISO2": "BH"
    },
    {
        "Country": "Chile",
        "Slug": "chile",
        "ISO2": "CL"
    },
    {
        "Country": "Uruguay",
        "Slug": "uruguay",
        "ISO2": "UY"
    },
    {
        "Country": "Yemen",
        "Slug": "yemen",
        "ISO2": "YE"
    },
    {
        "Country": "Austria",
        "Slug": "austria",
        "ISO2": "AT"
    },
    {
        "Country": "Bangladesh",
        "Slug": "bangladesh",
        "ISO2": "BD"
    },
    {
        "Country": "Italy",
        "Slug": "italy",
        "ISO2": "IT"
    },
    {
        "Country": "Micronesia, Federated States of",
        "Slug": "micronesia",
        "ISO2": "FM"
    },
    {
        "Country": "Puerto Rico",
        "Slug": "puerto-rico",
        "ISO2": "PR"
    },
    {
        "Country": "Tuvalu",
        "Slug": "tuvalu",
        "ISO2": "TV"
    },
    {
        "Country": "ALA Aland Islands",
        "Slug": "ala-aland-islands",
        "ISO2": "AX"
    },
    {
        "Country": "Afghanistan",
        "Slug": "afghanistan",
        "ISO2": "AF"
    },
    {
        "Country": "Cambodia",
        "Slug": "cambodia",
        "ISO2": "KH"
    },
    {
        "Country": "Sao Tome and Principe",
        "Slug": "sao-tome-and-principe",
        "ISO2": "ST"
    },
    {
        "Country": "Korea (North)",
        "Slug": "korea-north",
        "ISO2": "KP"
    },
    {
        "Country": "New Zealand",
        "Slug": "new-zealand",
        "ISO2": "NZ"
    },
    {
        "Country": "Turkey",
        "Slug": "turkey",
        "ISO2": "TR"
    },
    {
        "Country": "Greenland",
        "Slug": "greenland",
        "ISO2": "GL"
    },
    {
        "Country": "Hungary",
        "Slug": "hungary",
        "ISO2": "HU"
    },
    {
        "Country": "Australia",
        "Slug": "australia",
        "ISO2": "AU"
    },
    {
        "Country": "India",
        "Slug": "india",
        "ISO2": "IN"
    },
    {
        "Country": "San Marino",
        "Slug": "san-marino",
        "ISO2": "SM"
    },
    {
        "Country": "United Kingdom",
        "Slug": "united-kingdom",
        "ISO2": "GB"
    },
    {
        "Country": "Comoros",
        "Slug": "comoros",
        "ISO2": "KM"
    },
    {
        "Country": "Mauritania",
        "Slug": "mauritania",
        "ISO2": "MR"
    },
    {
        "Country": "Benin",
        "Slug": "benin",
        "ISO2": "BJ"
    },
    {
        "Country": "Côte d'Ivoire",
        "Slug": "cote-divoire",
        "ISO2": "CI"
    },
    {
        "Country": "Guadeloupe",
        "Slug": "guadeloupe",
        "ISO2": "GP"
    },
    {
        "Country": "Heard and Mcdonald Islands",
        "Slug": "heard-and-mcdonald-islands",
        "ISO2": "HM"
    },
    {
        "Country": "Kiribati",
        "Slug": "kiribati",
        "ISO2": "KI"
    },
    {
        "Country": "Mali",
        "Slug": "mali",
        "ISO2": "ML"
    },
    {
        "Country": "Northern Mariana Islands",
        "Slug": "northern-mariana-islands",
        "ISO2": "MP"
    },
    {
        "Country": "Palau",
        "Slug": "palau",
        "ISO2": "PW"
    },
    {
        "Country": "Myanmar",
        "Slug": "myanmar",
        "ISO2": "MM"
    },
    {
        "Country": "Somalia",
        "Slug": "somalia",
        "ISO2": "SO"
    },
    {
        "Country": "Trinidad and Tobago",
        "Slug": "trinidad-and-tobago",
        "ISO2": "TT"
    },
    {
        "Country": "Turkmenistan",
        "Slug": "turkmenistan",
        "ISO2": "TM"
    },
    {
        "Country": "French Guiana",
        "Slug": "french-guiana",
        "ISO2": "GF"
    },
    {
        "Country": "Lao PDR",
        "Slug": "lao-pdr",
        "ISO2": "LA"
    },
    {
        "Country": "United Arab Emirates",
        "Slug": "united-arab-emirates",
        "ISO2": "AE"
    },
    {
        "Country": "Albania",
        "Slug": "albania",
        "ISO2": "AL"
    },
    {
        "Country": "Ireland",
        "Slug": "ireland",
        "ISO2": "IE"
    },
    {
        "Country": "Burundi",
        "Slug": "burundi",
        "ISO2": "BI"
    },
    {
        "Country": "Cape Verde",
        "Slug": "cape-verde",
        "ISO2": "CV"
    },
    {
        "Country": "Greece",
        "Slug": "greece",
        "ISO2": "GR"
    },
    {
        "Country": "Guam",
        "Slug": "guam",
        "ISO2": "GU"
    },
    {
        "Country": "Guatemala",
        "Slug": "guatemala",
        "ISO2": "GT"
    },
    {
        "Country": "Korea (South)",
        "Slug": "korea-south",
        "ISO2": "KR"
    },
    {
        "Country": "Niger",
        "Slug": "niger",
        "ISO2": "NE"
    },
    {
        "Country": "Panama",
        "Slug": "panama",
        "ISO2": "PA"
    },
    {
        "Country": "Saint Helena",
        "Slug": "saint-helena",
        "ISO2": "SH"
    },
    {
        "Country": "Viet Nam",
        "Slug": "vietnam",
        "ISO2": "VN"
    },
    {
        "Country": "Saint Kitts and Nevis",
        "Slug": "saint-kitts-and-nevis",
        "ISO2": "KN"
    },
    {
        "Country": "Seychelles",
        "Slug": "seychelles",
        "ISO2": "SC"
    },
    {
        "Country": "Timor-Leste",
        "Slug": "timor-leste",
        "ISO2": "TL"
    },
    {
        "Country": "Bouvet Island",
        "Slug": "bouvet-island",
        "ISO2": "BV"
    },
    {
        "Country": "El Salvador",
        "Slug": "el-salvador",
        "ISO2": "SV"
    },
    {
        "Country": "Russian Federation",
        "Slug": "russia",
        "ISO2": "RU"
    },
    {
        "Country": "Slovenia",
        "Slug": "slovenia",
        "ISO2": "SI"
    },
    {
        "Country": "French Polynesia",
        "Slug": "french-polynesia",
        "ISO2": "PF"
    },
    {
        "Country": "Hong Kong, SAR China",
        "Slug": "hong-kong-sar-china",
        "ISO2": "HK"
    },
    {
        "Country": "Madagascar",
        "Slug": "madagascar",
        "ISO2": "MG"
    },
    {
        "Country": "Nigeria",
        "Slug": "nigeria",
        "ISO2": "NG"
    },
    {
        "Country": "Samoa",
        "Slug": "samoa",
        "ISO2": "WS"
    },
    {
        "Country": "British Indian Ocean Territory",
        "Slug": "british-indian-ocean-territory",
        "ISO2": "IO"
    },
    {
        "Country": "Equatorial Guinea",
        "Slug": "equatorial-guinea",
        "ISO2": "GQ"
    },
    {
        "Country": "Holy See (Vatican City State)",
        "Slug": "holy-see-vatican-city-state",
        "ISO2": "VA"
    },
    {
        "Country": "Rwanda",
        "Slug": "rwanda",
        "ISO2": "RW"
    },
    {
        "Country": "Saint Vincent and Grenadines",
        "Slug": "saint-vincent-and-the-grenadines",
        "ISO2": "VC"
    },
    {
        "Country": "Virgin Islands, US",
        "Slug": "virgin-islands",
        "ISO2": "VI"
    },
    {
        "Country": "Congo (Brazzaville)",
        "Slug": "congo-brazzaville",
        "ISO2": "CG"
    },
    {
        "Country": "Guyana",
        "Slug": "guyana",
        "ISO2": "GY"
    },
    {
        "Country": "Haiti",
        "Slug": "haiti",
        "ISO2": "HT"
    },
    {
        "Country": "Marshall Islands",
        "Slug": "marshall-islands",
        "ISO2": "MH"
    },
    {
        "Country": "Singapore",
        "Slug": "singapore",
        "ISO2": "SG"
    },
    {
        "Country": "Bhutan",
        "Slug": "bhutan",
        "ISO2": "BT"
    },
    {
        "Country": "Ghana",
        "Slug": "ghana",
        "ISO2": "GH"
    },
    {
        "Country": "Mozambique",
        "Slug": "mozambique",
        "ISO2": "MZ"
    },
    {
        "Country": "Antigua and Barbuda",
        "Slug": "antigua-and-barbuda",
        "ISO2": "AG"
    },
    {
        "Country": "Cocos (Keeling) Islands",
        "Slug": "cocos-keeling-islands",
        "ISO2": "CC"
    },
    {
        "Country": "Cyprus",
        "Slug": "cyprus",
        "ISO2": "CY"
    },
    {
        "Country": "Latvia",
        "Slug": "latvia",
        "ISO2": "LV"
    },
    {
        "Country": "Lebanon",
        "Slug": "lebanon",
        "ISO2": "LB"
    },
    {
        "Country": "Cook Islands",
        "Slug": "cook-islands",
        "ISO2": "CK"
    },
    {
        "Country": "Isle of Man",
        "Slug": "isle-of-man",
        "ISO2": "IM"
    },
    {
        "Country": "Libya",
        "Slug": "libya",
        "ISO2": "LY"
    },
    {
        "Country": "Netherlands",
        "Slug": "netherlands",
        "ISO2": "NL"
    },
    {
        "Country": "New Caledonia",
        "Slug": "new-caledonia",
        "ISO2": "NC"
    },
    {
        "Country": "Niue",
        "Slug": "niue",
        "ISO2": "NU"
    },
    {
        "Country": "Thailand",
        "Slug": "thailand",
        "ISO2": "TH"
    },
    {
        "Country": "Egypt",
        "Slug": "egypt",
        "ISO2": "EG"
    },
    {
        "Country": "Faroe Islands",
        "Slug": "faroe-islands",
        "ISO2": "FO"
    },
    {
        "Country": "South Georgia and the South Sandwich Islands",
        "Slug": "south-georgia-and-the-south-sandwich-islands",
        "ISO2": "GS"
    },
    {
        "Country": "Algeria",
        "Slug": "algeria",
        "ISO2": "DZ"
    },
    {
        "Country": "Brazil",
        "Slug": "brazil",
        "ISO2": "BR"
    },
    {
        "Country": "Central African Republic",
        "Slug": "central-african-republic",
        "ISO2": "CF"
    },
    {
        "Country": "Czech Republic",
        "Slug": "czech-republic",
        "ISO2": "CZ"
    },
    {
        "Country": "Ecuador",
        "Slug": "ecuador",
        "ISO2": "EC"
    },
    {
        "Country": "Gabon",
        "Slug": "gabon",
        "ISO2": "GA"
    },
    {
        "Country": "Zimbabwe",
        "Slug": "zimbabwe",
        "ISO2": "ZW"
    },
    {
        "Country": "Peru",
        "Slug": "peru",
        "ISO2": "PE"
    },
    {
        "Country": "Saint Pierre and Miquelon",
        "Slug": "saint-pierre-and-miquelon",
        "ISO2": "PM"
    },
    {
        "Country": "Republic of Kosovo",
        "Slug": "kosovo",
        "ISO2": "XK"
    },
    {
        "Country": "Tonga",
        "Slug": "tonga",
        "ISO2": "TO"
    },
    {
        "Country": "South Sudan",
        "Slug": "south-sudan",
        "ISO2": "SS"
    },
    {
        "Country": "Colombia",
        "Slug": "colombia",
        "ISO2": "CO"
    },
    {
        "Country": "Germany",
        "Slug": "germany",
        "ISO2": "DE"
    },
    {
        "Country": "Lesotho",
        "Slug": "lesotho",
        "ISO2": "LS"
    },
    {
        "Country": "Falkland Islands (Malvinas)",
        "Slug": "falkland-islands-malvinas",
        "ISO2": "FK"
    },
    {
        "Country": "Saudi Arabia",
        "Slug": "saudi-arabia",
        "ISO2": "SA"
    },
    {
        "Country": "Aruba",
        "Slug": "aruba",
        "ISO2": "AW"
    },
    {
        "Country": "Swaziland",
        "Slug": "swaziland",
        "ISO2": "SZ"
    },
    {
        "Country": "United States of America",
        "Slug": "united-states",
        "ISO2": "US"
    },
    {
        "Country": "Antarctica",
        "Slug": "antarctica",
        "ISO2": "AQ"
    },
    {
        "Country": "Cuba",
        "Slug": "cuba",
        "ISO2": "CU"
    },
    {
        "Country": "Monaco",
        "Slug": "monaco",
        "ISO2": "MC"
    },
    {
        "Country": "Serbia",
        "Slug": "serbia",
        "ISO2": "RS"
    },
    {
        "Country": "Anguilla",
        "Slug": "anguilla",
        "ISO2": "AI"
    },
    {
        "Country": "Maldives",
        "Slug": "maldives",
        "ISO2": "MV"
    },
    {
        "Country": "Romania",
        "Slug": "romania",
        "ISO2": "RO"
    },
    {
        "Country": "Uganda",
        "Slug": "uganda",
        "ISO2": "UG"
    },
    {
        "Country": "Japan",
        "Slug": "japan",
        "ISO2": "JP"
    },
    {
        "Country": "Belarus",
        "Slug": "belarus",
        "ISO2": "BY"
    },
    {
        "Country": "France",
        "Slug": "france",
        "ISO2": "FR"
    },
    {
        "Country": "Western Sahara",
        "Slug": "western-sahara",
        "ISO2": "EH"
    },
    {
        "Country": "Iraq",
        "Slug": "iraq",
        "ISO2": "IQ"
    },
    {
        "Country": "Norway",
        "Slug": "norway",
        "ISO2": "NO"
    },
    {
        "Country": "Philippines",
        "Slug": "philippines",
        "ISO2": "PH"
    },
    {
        "Country": "Bahamas",
        "Slug": "bahamas",
        "ISO2": "BS"
    },
    {
        "Country": "Dominican Republic",
        "Slug": "dominican-republic",
        "ISO2": "DO"
    },
    {
        "Country": "Macao, SAR China",
        "Slug": "macao-sar-china",
        "ISO2": "MO"
    },
    {
        "Country": "Bermuda",
        "Slug": "bermuda",
        "ISO2": "BM"
    },
    {
        "Country": "Pakistan",
        "Slug": "pakistan",
        "ISO2": "PK"
    },
    {
        "Country": "Pitcairn",
        "Slug": "pitcairn",
        "ISO2": "PN"
    },
    {
        "Country": "Tanzania, United Republic of",
        "Slug": "tanzania",
        "ISO2": "TZ"
    },
    {
        "Country": "Bolivia",
        "Slug": "bolivia",
        "ISO2": "BO"
    },
    {
        "Country": "Kazakhstan",
        "Slug": "kazakhstan",
        "ISO2": "KZ"
    },
    {
        "Country": "Kyrgyzstan",
        "Slug": "kyrgyzstan",
        "ISO2": "KG"
    },
    {
        "Country": "Taiwan, Republic of China",
        "Slug": "taiwan",
        "ISO2": "TW"
    },
    {
        "Country": "Armenia",
        "Slug": "armenia",
        "ISO2": "AM"
    },
    {
        "Country": "Svalbard and Jan Mayen Islands",
        "Slug": "svalbard-and-jan-mayen-islands",
        "ISO2": "SJ"
    },
    {
        "Country": "Sweden",
        "Slug": "sweden",
        "ISO2": "SE"
    },
    {
        "Country": "Togo",
        "Slug": "togo",
        "ISO2": "TG"
    },
    {
        "Country": "Fiji",
        "Slug": "fiji",
        "ISO2": "FJ"
    },
    {
        "Country": "Martinique",
        "Slug": "martinique",
        "ISO2": "MQ"
    },
    {
        "Country": "Montenegro",
        "Slug": "montenegro",
        "ISO2": "ME"
    },
    {
        "Country": "Suriname",
        "Slug": "suriname",
        "ISO2": "SR"
    },
    {
        "Country": "Venezuela (Bolivarian Republic)",
        "Slug": "venezuela",
        "ISO2": "VE"
    },
    {
        "Country": "Angola",
        "Slug": "angola",
        "ISO2": "AO"
    },
    {
        "Country": "Macedonia, Republic of",
        "Slug": "macedonia",
        "ISO2": "MK"
    },
    {
        "Country": "Mauritius",
        "Slug": "mauritius",
        "ISO2": "MU"
    },
    {
        "Country": "Mayotte",
        "Slug": "mayotte",
        "ISO2": "YT"
    },
    {
        "Country": "Senegal",
        "Slug": "senegal",
        "ISO2": "SN"
    },
    {
        "Country": "South Africa",
        "Slug": "south-africa",
        "ISO2": "ZA"
    },
    {
        "Country": "Syrian Arab Republic (Syria)",
        "Slug": "syria",
        "ISO2": "SY"
    },
    {
        "Country": "Liechtenstein",
        "Slug": "liechtenstein",
        "ISO2": "LI"
    },
    {
        "Country": "Netherlands Antilles",
        "Slug": "netherlands-antilles",
        "ISO2": "AN"
    },
    {
        "Country": "Croatia",
        "Slug": "croatia",
        "ISO2": "HR"
    },
    {
        "Country": "Djibouti",
        "Slug": "djibouti",
        "ISO2": "DJ"
    },
    {
        "Country": "Mexico",
        "Slug": "mexico",
        "ISO2": "MX"
    },
    {
        "Country": "Belize",
        "Slug": "belize",
        "ISO2": "BZ"
    },
    {
        "Country": "Guinea-Bissau",
        "Slug": "guinea-bissau",
        "ISO2": "GW"
    },
    {
        "Country": "Mongolia",
        "Slug": "mongolia",
        "ISO2": "MN"
    },
    {
        "Country": "Poland",
        "Slug": "poland",
        "ISO2": "PL"
    },
    {
        "Country": "Ethiopia",
        "Slug": "ethiopia",
        "ISO2": "ET"
    },
    {
        "Country": "Kuwait",
        "Slug": "kuwait",
        "ISO2": "KW"
    },
    {
        "Country": "Nicaragua",
        "Slug": "nicaragua",
        "ISO2": "NI"
    },
    {
        "Country": "Papua New Guinea",
        "Slug": "papua-new-guinea",
        "ISO2": "PG"
    },
    {
        "Country": "Sierra Leone",
        "Slug": "sierra-leone",
        "ISO2": "SL"
    },
    {
        "Country": "Sudan",
        "Slug": "sudan",
        "ISO2": "SD"
    }
]

n = pd.DataFrame.from_dict(page_countries)
countries = n['Country'].values.tolist()
slugs = n['Slug'].values.tolist()
ddc = []
for i, country in enumerate(countries):
    ddc.append({'label': country, 'value': slugs[i]})

def get_df(country: str, case_type: str) -> pd.DataFrame:
    url = 'https://api.covid19api.com/total/dayone/country/' + country + '/status/' + case_type
    page = requests.get(url, verify=False)
    df = pd.DataFrame.from_dict(page.json())
    dates = df['Date'].values.tolist()
    ddc = []
    for i, country in enumerate(countries):
        ddc.append({'label': country, 'value': slugs[i]})

    datesF = []
    for i in dates:
        s = i.split('-')
        a = int(s[0])
        b = int(s[1])
        c = int(s[2][:2])
        datesF.append((a, b, c))

    df = df.reset_index()
    df = df[['Cases', 'Date']]

    return df

def get_range(cases: list) -> list:
    diff = []
    start = 0
    for case in cases:
        diff.append(case - start)
        start = case

    return diff


app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/growth/')
CONTENT_STYLE = {
}
app.layout = html.Div([
    navbar("Growth"),
    html.Div([
        html.Div([
            dcc.Interval(
                id="ic",
                interval=20000,
                n_intervals=0
            )],
            id="temp"
        ),
        dcc.Dropdown(
            id = 'drop',
            options = ddc,
            style=dict(width='100%'),
        ),
        html.Div([
            dcc.Dropdown(id="ind_drop")],
            id='net'),
        html.Div([
            dcc.Dropdown(id="drop2"),
            dcc.Dropdown(id="drop3"),
            dcc.Dropdown(id="drop4")],
            id='net2'),
        html.Div([
            dcc.Graph(
                id='graph'
            ),
            dcc.Interval(
                id='interval_component',
                interval=10000,
                n_intervals=0
            )
        ], className="box")
    ])
])



@app.callback([Output("drop", "value"), Output("temp", "children")],
        [Input("ic", "n_intervals")])
def updip(r):
    global pt
    s = extras.getip()
    print(pt)
    pt = s
    print("PT: ", pt)
    h = n['ISO2'].values.tolist().index(s)
    c = slugs[h]
    return c, []

@app.callback([Output("net", "children"), Output("net2", "style")],
        [Input("drop", "value")])
def net_c(val):
    if val == "india":
        return [
            dcc.Dropdown(
                id="ind_drop",
                options=[
                    {'label': 'Districts', 'value': 'district'},
                    {'label': 'State', 'value': 'state'}],
                value="state")], {'display': 'block'}
    else:
        return [], {'display': 'none'}

@app.callback(Output("net2", "children"),
        [Input("ind_drop", "value")])
def net2_c(val):
    k = pd.read_csv("https://api.covid19india.org/csv/latest/district_wise.csv")
    states = list(set(k["State"]))
    states.sort()
    s = list(k.loc[k["State"] == "Andhra Pradesh"]["District"])
    s.sort()
    if val == "state":
        return [
            dcc.Dropdown(
                id="drop4",
                options=[{'label': x, 'value': x} for x in states] + [{'label': 'All', 'value': 'all'}],
                value="all", style={"display": "block"}),
            dcc.Dropdown(
                id="drop2",
                options=[{'label': x, 'value': x} for x in states],
                value="Andhra Pradesh", style={"display": "none"}),
            dcc.Dropdown(
                id="drop3",
                options=[{'label': x, 'value': x} for x in s],
                value=s[0], style={"display": "none"}
            )
        ]
    elif val=="district":
        return [
            dcc.Dropdown(
                id="drop4",
                options=[{'label': x, 'value': x} for x in states],
                value="Andhra Pradesh", style={"display": "none"}),
            dcc.Dropdown(
                id="drop2",
                options=[{'label': x, 'value': x} for x in states],
                value="Andhra Pradesh", style={"display": "block"}),
            dcc.Dropdown(
                id="drop3",
                options=[{'label': x, 'value': x} for x in s],
                value=s[0], style={"display": "block"}
            )
        ]

@app.callback([Output("drop3", "options"), Output("drop3", "value")],
            [Input("drop2", "value")])
def drop2_c(val):
    if val:
        k = pd.read_csv("https://api.covid19india.org/csv/latest/district_wise.csv")
        s = list(k.loc[k["State"] == val]["District"])
        s.sort()
        return [{'label': x, 'value': x} for x in s], s[-1]
    else:
        raise PreventUpdate


def plot_data(dates, confirmed_diff, deaths_diff, recovered_diff, active_diff):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=dates, y=confirmed_diff, name='New Cases', line=dict(color='orange'))
    )
    fig.add_trace(
        go.Scatter(x=dates, y=deaths_diff, name='New Deaths', line=dict(color='red'))
    )
    fig.add_trace(
        go.Scatter(x=dates, y=recovered_diff, name='New Recoveries', line=dict(color='green'))
    )
    fig.add_trace(
        go.Scatter(x=dates, y=active_diff, name='New Active', line=dict(color='yellow'))
    )
    fig.update_layout(showlegend=False,
                      legend=dict(
                          font=dict(
                              color="white"
                          )
                      ),
                      margin=dict(
                          l=5,
                          r=0,
                          b=5,
                          t=0,
                          pad=0
                      ),
                      plot_bgcolor='#2B3E50',
                      paper_bgcolor='#2B3E50')
    fig.update_xaxes(tickangle=90, tickfont=dict(family='Rockwell', color='white'), rangeslider_visible=True)
    fig.update_yaxes(tickfont=dict(family='Rockwell', color='white'))
    return fig

@app.callback(Output('graph', 'figure'),
            [Input("drop3", "value"), Input("drop", "value"), Input("drop4", "value"), Input("drop2", "value")])
def drop3_c(val, val2, val3, val4):
    ctx = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    print("{}: {}", ctx, [val, val2, val3, val4])
    if ctx == "drop3":
        k = pd.read_csv("https://api.covid19india.org/csv/latest/districts.csv")
        row = k.loc[k["State"] == val4]
        rows = row.loc[row["District"] == val]
        cdf = rows["Confirmed"]
        confirmed_diff = get_range(list(cdf))
        #print(confirmed_diff)
        ddf = list(rows["Deceased"])
        deaths_diff = get_range(list(ddf))
        rdf = list(rows["Recovered"])
        recovered_diff = get_range(list(rdf))
        adf = list(rows["Confirmed"] - (rows["Recovered"] + rows["Deceased"]))
        active_diff = get_range(adf)
        fig = plot_data(list(rows["Date"]), confirmed_diff, deaths_diff, recovered_diff, active_diff)
    elif ctx == "drop":
        fig = glob_plot(val2)
    elif ctx == "drop4":
        if val3 == "all":
            fig = glob_plot("india")
        else:
            k = pd.read_csv("https://api.covid19india.org/csv/latest/states.csv")
            rows = k.loc[k["State"] == val3]
            cdf = rows["Confirmed"]
            confirmed_diff = get_range(list(cdf))
            ddf = list(rows["Deceased"])
            deaths_diff = get_range(list(ddf))
            rdf = list(rows["Recovered"])
            recovered_diff = get_range(list(rdf))
            adf = list(rows["Confirmed"] - (rows["Recovered"] + rows["Deceased"]))
            active_diff = get_range(adf)
            fig = plot_data(list(rows["Date"]), confirmed_diff, deaths_diff, recovered_diff, active_diff)

    return fig

def glob_plot(value):
    global nhj
    nhj = value
    dfc = get_df(value, 'confirmed')
    dates = dfc['Date']
    confirmed_diff = get_range(dfc['Cases'])
    dfd = get_df(value, 'deaths')
    deaths_diff = get_range(dfd['Cases'])
    dfr = get_df(value, 'recovered')
    recovered_diff = get_range(dfr['Cases'])
    dfa = pd.DataFrame(dfc['Cases'] - (dfd['Cases'] + dfr['Cases']))
    active_diff = get_range(dfa[dfa.columns[0]])
    fig = plot_data(dates, confirmed_diff, deaths_diff, recovered_diff, active_diff)
    return fig


app.index_string = extras.ind_str
app.title = 'Corona Tracker'

if __name__ == '__main__':
    app.run_server(debug=False)
