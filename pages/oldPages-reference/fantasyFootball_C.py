import dash
from dash import html, dcc
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


# + ---- register page ---- +
dash.register_page(__name__, name="FF", top_nav=False, path="/FF")

# + ---- layout ---- +
layout = dbc.Container(
    [
        html.Div(
            [
                dbc.Row([], class_name="bg-light"),
                dbc.Row(
                    [
                        dbc.Col(html.Div(), class_name="bg-light"),
                        dbc.Col(html.Div(), class_name="bg-light"),
                        dbc.Col(
                            [
                                html.Br(),
                                dmc.Paper(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        html.H2("Fantasy Football", id="h2"),
                                                        html.Hr(className="my-2"),
                                                    ]
                                                )
                                            ],
                                            justify="start",
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        dcc.Markdown("_Coming Soon_ . . .", id="body-text"),
                                                        dbc.Button(
                                                            "Back",
                                                            color="primary",
                                                            class_name="me-1",
                                                            href="/Projects",
                                                            active=True,
                                                            id="ff-back-btn",
                                                        ),
                                                    ]
                                                )
                                            ]
                                        ),
                                    ],
                                    shadow="xl",
                                    p="lg",
                                    radius="md",
                                ),
                            ],
                            width=10,
                        ),
                        dbc.Col(html.Div(), class_name="bg-light"),
                        dbc.Col(html.Div(), class_name="bg-light"),
                    ]
                ),
            ]
        )
    ],
    fluid=True,
    style={"background-color": "#ecf0f1"},
)
