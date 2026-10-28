# Projects Page for portfolio web app
#    Page Registry: "projects", path = "/projects", order = 1

# + -------------------------- +
# +       Projects Page        +
# + -------------------------- +
# + ---- import libraries ---- +
import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

# + ---- page registration ---- +
dash.register_page(__name__, name="Projects", top_nav=True, path="/Projects", custom_key="Projects")


# + ---- jumbotron & cards ---- +
# Fantasy Football Jumbotron
fantasyJumbo = html.Div(
    dbc.Container(
        [
            html.H3("Fantasy Football", id="card-title"),
            html.P("Tools for Draft Day and in-season analysis.", className="lead"),
            html.Hr(className="my-2"),
            html.P(
                "Player Statistics, Rushing & Passing Statistics, Data Visualizations, VOR Draft Model. "
                "Written in Python and Jupyter Notebooks. "
            ),
            html.P(
                dbc.Button("Learn More", color="primary", id="ff-button", href="/FF", active=True), className="lead"
            ),
        ],
        fluid=True,
        className="p-5 border rounded-3 bg-light",
    ),
    className="p-3 me-4",
)

# RVM Jumbotron
rvmJumbo = html.Div(
    dbc.Container(
        [
            html.H3("RVM", id="card-title"),
            html.P("Reverse Vending Machine.", className="lead"),
            html.Hr(className="my-2"),
            html.P(
                "A reverse vending machine accepts Aluminum and Plastic recyclables and returns a voucher "
                "that can be redeemed for the CSV price of the users resident State. "
                "The goal of this project is to increase recycling rates in our community."
            ),
            html.P(
                dbc.Button("Learn More", color="primary", id="rvm-button", href="/RVM", active=True), className="lead"
            ),
        ],
        fluid=True,
        className="p-5 border rounded-3 bg-light",
    ),
    className="p-3 me-4",
)

# Smart Parking Card
dacCard = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H3("HiFi DAC", id="card-title"),
                        html.Hr(className="my-3", style={"width": "90%"}),
                        html.P(
                            "Digital-to-Analog Converter with RaspberryPi and HiFiBerry GPIO Hat. "
                            "Motivated by the warm tone of vintage power amplifiers and a large vinyl collection. "
                            "The DAC allows you to stream your digital music library over bluetooth or home network, "
                            "and through a 1972 Marantz 2238B Stereo Receiver.",
                            id="card-body-text",
                            className="w-80 mh-100 float-start",
                        ),
                    ]
                )
            ],
            style={"width": "auto"},
            class_name="rounded-3 bg-light mb-auto",
        )
    ],
    fluid=True,
    class_name="p-3 me-5 ",
)

smartCard = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        dmc.Group(
                            [
                                html.H3("Smart Parking System", id="card-title"),
                                dbc.Badge("NSF Grant DUE 1953752", id="source-text", color="success"),
                            ],
                            position="apart",
                        ),
                        html.Hr(className="my-3", style={"width": "90%"}),
                        html.P(
                            "A smart parking system was built using RaspberryPi, camera and Python "
                            "CNN (Convolutional Neural Network) algorithm to detect vehicles & pedestrians "
                            "entering a parking garage. The program returns the number of available parking "
                            "spaces in a student parking garage.  We were able to increase accuracy of the model by 25 percent from last year.",
                            id="card-body-text",
                            className="w-80 mh-100 float-start",
                        ),
                    ]
                )
            ],
            style={"width": "auto"},
            class_name="rounded-3 bg-light h-100 mb-auto",
        )
    ],
    fluid=True,
    class_name="p-3 me-5",
)


# + ---- layout ---- +
layout = dbc.Container(
    [
        html.Div(
            [
                dbc.Row([], className="bg-light"),  # empty row to separate paper element
                dbc.Row(
                    [
                        dbc.Col(html.Div(), className="bg-light"),  # Gutter
                        dbc.Col(html.Div(), className="bg-light"),  # Gutter
                        dbc.Col(
                            [
                                html.Br(),
                                dmc.Paper(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        html.H2("Projects", id="h2"),
                                                        html.H4("Past and Present", id="h4-sub"),
                                                        html.Hr(style={"width": "90%"}),
                                                    ]
                                                )
                                            ],
                                            justify="center",
                                        ),
                                        html.Br(),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        fantasyJumbo,
                                                    ]
                                                )
                                            ]
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col([smartCard], class_name="p-3 me-4 mh-100 "),
                                                dbc.Col([dacCard], class_name="p-3 me-4 mh-100"),
                                            ]
                                        ),
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        rvmJumbo,
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
                            width=8,
                        ),
                        dbc.Col(html.Div(), className="bg-light"),
                        dbc.Col(html.Div(), className="bg-light"),
                    ]
                ),
                dbc.Row([], className="bg-light"),
            ]
        ),
    ],
    fluid=True,
    style={"background-color": "#ecf0f1"},
)

# + ---- callbacks ---- +
