"""Dash Bootstrap Component: Avatar.

-> Avatar Element for web-app.
-> Will display a shamm thumbnail picture of myself.
-> Date: 08/08/2023.
"""

import dash
from dash import html

import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

# + --- photo source --- +
myPhoto = " <ADD PATH> "


# + --- layout --- +
def avatar():
    """Profile Avatar for web-app."""
    return dbc.Container(
        [html.Div([dmc.Avatar(src="/assets/moodle_profile.jpg", size="lg", radius="xl", alt="my headshot")])],
        fluid=True,
    )
