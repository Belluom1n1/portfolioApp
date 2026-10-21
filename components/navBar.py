"""Simple Navbar.

-> Styled with Dash Bootsrap Components.
-> Date: 08/08/2023.
"""

# + -- Imports -- +
from dash import html, Dash
import dash_bootstrap_components as dbc

from components import dmcAvatar as avatar

# + -- Avatar -- +
myBrand = avatar.avatar()


# + --- navBar --- +
def navBar():
    """Create a simple navbar for the web app."""
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="p-2 fa-brands fa-github fa-xl"),
                        " ",
                    ],
                    href="https://github.com/Belluom1n1",
                    external_link=True,
                    target="_blank",
                )
            ),
            dbc.NavItem(
                dbc.NavLink(
                    [
                        html.I(className="p-2 fa-brands fa-linkedin fa-xl"),
                        " ",
                    ],
                    href="https://linkedin.com/in/bbelluomini",
                    external_link=True,
                    target="_blank",
                )
            ),
            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem("Navigation", header=True),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Home", href="/"),
                    dbc.DropdownMenuItem("Projects", href="/Projects"),
                ],
                nav=True,
                in_navbar=True,
                label="Menu",
                align_end=True,
                class_name="me-2",
            ),
        ],
        brand=myBrand,
        brand_href="/",
        color="primary",
        dark=True,
        fluid=True,
        className="mb-0",
    )
