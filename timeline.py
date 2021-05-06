from modules import *
from web_scrape import *
from sidebar import *
import extras

external_stylesheets = [extras.theme]

colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}

url = 'https://api.covid19api.com/total/dayone/country/india/status/confirmed'
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
countries = pd.DataFrame.from_dict(page_countries)['Country'].values.tolist()
slugs = pd.DataFrame.from_dict(page_countries)['Slug'].values.tolist()
page = requests.get(url, verify=False)
dates = pd.DataFrame.from_dict(page.json())['Date'].values.tolist()
ddc = []
for i, country in enumerate(countries):
    ddc.append({'label': country, 'value': slugs[i]})

datesF = []
for i in dates:
    s = i.split('-')
    a = int(s[0])
    b = int(s[1])
    c = int(s[2][:2])
    datesF.append((a,b,c))

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                requests_pathname_prefix='/timeline/'
     )
CONTENT_STYLE = {
    "margin-left": "1rem",
    "margin-right": "1rem",
#    "padding": "2rem 1rem",
}

app.layout = html.Div([
        navbar("Timeline"),
html.Div([
    html.Div(id = 'Fe_He', children=[
        dcc.DatePickerRange(
            id='dat_',
            min_date_allowed=dt(datesF[0][0], datesF[0][1], datesF[0][2]),
            max_date_allowed=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]),
            initial_visible_month=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]),
            start_date=dt(datesF[0][0], datesF[0][1], datesF[0][2]).date(),
            end_date=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]).date(),
            display_format='MMM|Do|YY'
        )
    ]),
    html.Div([
        dcc.Dropdown(
            id = 'drop',
            options = ddc,
            style=dict(width='100%'),
            value='india'
        )
    ]),
    html.Div([
        html.H4(f'Timeline', id='nono_', style={'color':'white'}),
        dcc.Graph(id='update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=5000,
            n_intervals=0
        )
    ], className='box')],
style=CONTENT_STYLE)
  ]#,
)

@app.callback(Output('Fe_He', 'children'),
                [Input('drop', 'value')])
def fnucs(val_d):
    URL = 'https://api.covid19api.com/total/dayone/country/' + val_d + '/status/confirmed'
    page = requests.get(URL, verify=False)
    dates = pd.DataFrame.from_dict(page.json())['Date'].values.tolist()
    datesF = []
    for i in dates:
        s = i.split('-')
        a = int(s[0])
        b = int(s[1])
        c = int(s[2][:2])
        datesF.append((a,b,c))
    return dcc.DatePickerRange(
        id='dat_',
        min_date_allowed=dt(datesF[0][0], datesF[0][1], datesF[0][2]),
        max_date_allowed=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]),
        initial_visible_month=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]),
        start_date=dt(datesF[0][0], datesF[0][1], datesF[0][2]).date(),
        end_date=dt(datesF[-1][0], datesF[-1][1], datesF[-1][2]).date(),
        display_format='MMM|Do|YY'
    )


@app.callback(Output('update-graph', 'figure'),
              [Input('drop', 'value'),
               Input('interval-component', 'n_intervals'),
               Input('dat_', 'start_date'),
               Input('dat_', 'end_date')
                ])
def plot_bar(val, n, start, end):
    '''
    Plots the collected data
    '''
    start = start.split('-')
    end = end.split('-')
    start_index = datesF.index((int(start[0]), int(start[1]), int(start[2])))
    end_index = datesF.index((int(end[0]), int(end[1]), int(end[2]))) + 1
    print(start_index, end_index)
    URL = 'https://api.covid19api.com/total/dayone/country/' + val + '/status/confirmed'
    page = requests.get(URL, verify=False)
    dfc = pd.DataFrame.from_dict(page.json())
    URL = 'https://api.covid19api.com/total/dayone/country/' + val + '/status/recovered'
    page = requests.get(URL, verify=False)
    dfr = pd.DataFrame.from_dict(page.json())
    URL = 'https://api.covid19api.com/total/dayone/country/' + val + '/status/deaths'
    page = requests.get(URL, verify=False)
    dfd = pd.DataFrame.from_dict(page.json())
    fig = ms(rows = 2, cols=2,
        specs=[[{}, {}],
               [{"colspan": 2}, None]],
    )
    print(len(dfc['Date']))
    fig.add_trace(go.Bar(x=dfc['Date'][start_index:end_index], y=dfd['Cases'][start_index:end_index], name='Deaths'),1,1)
    fig.add_trace(go.Scatter(x=dfc['Date'][start_index:end_index], y=dfd['Cases'][start_index:end_index], name='Deaths'),1,1)
    fig.add_trace(go.Bar(x=dfc['Date'][start_index:end_index], y=dfr['Cases'][start_index:end_index], name='Recoveries'),1,2)
    fig.add_trace(go.Scatter(x=dfc['Date'][start_index:end_index], y=dfr['Cases'][start_index:end_index], name='Recoveries'),1,2)
    fig.add_trace(go.Bar(x=dfc['Date'][start_index:end_index], y=dfc['Cases'][start_index:end_index], name='Confirmed Cases'),2,1)
    fig.add_trace(go.Scatter(x=dfc['Date'][start_index:end_index], y=dfc['Cases'][start_index:end_index], name='Confirmed Cases'),2,1)
    fig.update_layout(showlegend=False,
                      legend=dict(
                          font=dict(
                              color="white"
                          )
                      ),
#                      width=1000, height=500,
                      margin=dict(
                      l=0,
                      r=0,
#                      b=15,
                      t=0,
                      pad=0
                            ),
                      # plot_bgcolor='#111111',
                      paper_bgcolor='#2B3E50')
                      # title={
                          # 'text': f"COVID 19 DATA OF {val} IN 2020",
                          # 'y':0.9,
                          # 'x':0.5,
                          # 'xanchor': 'center',
                          # 'yanchor': 'bottom', 'font':{'color':'white'}})
    fig.update_xaxes(tickangle=90, tickfont=dict(family='Rockwell', color='white'))
    fig.update_yaxes(tickfont=dict(family='Rockwell', color='white'))
    return fig
app.index_string = extras.ind_str
app.title = 'Corona Tracker'
if __name__ == '__main__':
    app.run_server(debug=False)
