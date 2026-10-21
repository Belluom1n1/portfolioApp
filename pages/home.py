# Home Page for portfolio web app
#    Page Registry: "home", path = "/", order = 0

import dash
from dash import html, dcc, Dash, Input, Output


# Page Registry
dash.register_page(__name__, path="/", title="Home", order=0)

layout = html.Div(
    children=[
        html.H1(children="Home Page!"),
        html.Div(children="""This is the home page content. Yay."""),
    ]
)
