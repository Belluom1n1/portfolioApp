# + ---- library imports ---- +
import dash
import dash_bootstrap_components as dbc
from dash import Dash

# + ---- components & assets ---- +
from components import navbar

# + ---- css // styles // declarations ---- +
FA621 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"
TYPOGRAPHY = "/assets/typography.css"

# import Navbar
nav = navbar.navbar()

# + ---- initialize app ---- +
app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.FLATLY, FA621, TYPOGRAPHY],
    suppress_callback_exceptions=True,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width= device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.5,",
            "charSet": "utf-8",
        }
    ],
)
server = app.server


# + ---- layout ---- +
""" Call components/pages and wrap them in a dbc.Container """
app.layout = dbc.Container(
    [nav, dash.page_container],
    fluid=True,
)


# + ---- run server ---- +
# Run server with debug developer mode
if __name__ == "__main__":
    app.run_server(debug=False)
