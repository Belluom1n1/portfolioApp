# Run this app with 'python app.py' and
#  visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import State, callback, Dash, Input, Output, clientside_callback
import dash_mantine_components as dmc
from dash_iconify import DashIconify

# + -- THEME -- +
theme = {
    # Add color definitions here.
    "colors": {
        "blue": [
            "#E9EDFC",
            "#C5D0F9",
            "#A1B2F6",
            "#7D94F3",
            "#5A76F0",
            "#3A59ED",
            "#2B43B9",
            "#1C2E85",
            "#0D1A51",
            "#010617",
        ],
    },
    "shadows": {
        "md": "1px 1px 3px rgba(0,0,0,.25)",
        "xl": "5px 5px 3px rgba(0,0,0,.25)",
    },
    "headings": {
        "fontFamily": "Roboto, sans-serif",
        "sizes": {
            "h1": {"fontSize": 34},
            "h2": {"fontSize": 28},
            "h3": {"fontSize": 22},
        },
    },
}

# + -- THEME TOGGLE -- +
theme_toggle = dmc.Switch(
    offLabel=DashIconify(icon="radix-icons:sun", width=15, color="var(--mantine-color-yellow-8)"),
    onLabel=DashIconify(
        icon="radix-icons:moon",
        width=15,
        color="var(--mantine-color-yellow-6)",
    ),
    id="color-scheme-toggle",
    persistence=True,
    color="grey",
)

# + -- LOGO -- +
logo = "https://github.com/user-attachments/assets/c1ff143b-4365-4fd1-880f-3e97aab5c302"

app = Dash()

# + -- LAYOUT -- +
layout = dmc.AppShell(
    [
        dmc.AppShellHeader(
            dmc.Group(
                [
                    dmc.Group(
                        [
                            dmc.Burger(
                                id="burger",
                                size="sm",
                                hiddenFrom="sm",
                                opened=False,
                            ),
                            dmc.Image(src=logo, h=40, flex=0),
                            dmc.Title("Brians Demo App", c="blue"),
                        ]
                    ),
                    theme_toggle,
                ],
                justify="space-between",
                style={"flex": 1},
                h="100%",
                px="md",
            ),
        ),
        dmc.AppShellNavbar(
            id="navbar",
            children=[
                "Navbar",
                *[dmc.Skeleton(height=28, mt="sm", animate=False) for _ in range(15)],
            ],
            p="md",
        ),
        dmc.AppShellMain("Main"),
    ],
    header={
        "height": {"base": 60, "md": 70, "lg": 80},
    },
    navbar={
        "width": {"base": 200, "md": 300, "lg": 400},
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    padding="md",
    id="appshell",
)

app.layout = dmc.MantineProvider(layout)


# + -- Callbacks -- +
@callback(
    Output("appshell", "navbar"),
    Input("burger", "opened"),
    State("appshell", "navbar"),
)
def toggle_navbar(opened, navbar):
    """Toggle the navbar's collapsed state based on the burger menu's opened state."""
    navbar["collapsed"] = {"mobile": not opened}
    return navbar


clientside_callback(
    """
    (switchOn) => {
       document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'dark' : 'light');
       return window.dash_clientside.no_update
    }
    """,
    Output("color-scheme-toggle", "id"),
    Input("color-scheme-toggle", "checked"),
)

if __name__ == "__main__":
    app.run(debug=True)
