# Contact Page for portfolio web app
#    Page Registry: "contact", path = "/contact", order = 2

import dash
from dash import html, dcc, Dash, Input, Output

# Page Registry
dash.register_page(__name__, path="/contact", title="Contact", order=2)
