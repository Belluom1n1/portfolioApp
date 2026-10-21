from dash import html, Dash
import dash

dash.register_page(__name__, path="/404", name="404", top_nav=False)

layout = html.H1("404: Not found", className="text-center mt-5")
