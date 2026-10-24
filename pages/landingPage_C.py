# + ----------------- +
# +   Landing Page    +
# + ----------------- +
# + ---- library imports ---- +
import dash
from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

# + ---- timeline ---- +
from components import dmcTimeLine as timeline

timeline = timeline.timeline()

# + ---- page registration ---- +
dash.register_page(__name__, name="Home", top_nav=True, path="/")


# + ---- icons // buttons --- +
"""
Refer to these comments for accordion title styling.

    myRes = html.I(className= 'p-3 fa-regular fa-file-lines fa-xl')
    myGit = html.I(className= 'p-3 fa-brands fa-github fa-xl')
    myLinked = html.I(className= 'p-3 fa-brands fa-linkedin fa-xl')
"""

# + ---- layout ---- +
layout = dbc.Container(
    [
        html.Div(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Br(),
                            dmc.Paper(
                                [
                                    # + ---- Home Page, Title ---- +
                                    dmc.Grid(
                                        children=[
                                            dmc.Col(
                                                html.Div(
                                                    [
                                                        html.H2(" NAME ", id="h2", className="mb-1"),
                                                        dcc.Markdown(
                                                            "#### _Student of Mechanical Engineering_",
                                                            id="h5-sub",
                                                            style={"font-weight": 200},
                                                        ),
                                                        html.Hr(className="mt-2 mb-3"),
                                                    ]
                                                ),
                                                span=8,
                                            )
                                        ],
                                        grow=True,
                                        gutter="sm",
                                    ),
                                    # + ---- Contact Info // Work Timeline  ---- +
                                    dmc.Grid(
                                        children=[
                                            dmc.Col(
                                                html.Div(
                                                    [
                                                        html.H4("Phone:", style={"font-weight": 300}, id="h4"),
                                                        html.Hr(style={"width": "88%"}),
                                                        dcc.Markdown(
                                                            "_916-955-6175_", id="body-text", style={"font-size": 18}
                                                        ),
                                                        html.H4("Location:", id="h4", style={"font-weight": 300}),
                                                        html.Hr(style={"width": "88%"}),
                                                        dcc.Markdown(
                                                            "_Sacramento, CA. 95608_",
                                                            id="body-text",
                                                            style={"font-size": 18},
                                                        ),
                                                        html.H4("Email:", style={"font-weight": 300}, id="h4"),
                                                        html.Hr(style={"width": "88%"}),
                                                        dcc.Markdown(
                                                            """
                                                * < EMAIL ADDRESS >

                                                * < EMAIL ADDRESS >
                                                         """,
                                                            id="body-text",
                                                        ),
                                                        dcc.Markdown(
                                                            "#### Education:", id="h4", style={"font-weight": 300}
                                                        ),
                                                        html.Hr(style={"width": "88%"}),
                                                        dcc.Markdown(
                                                            """
                                                    - **California State University, Sacramento** | Sacramento, CA. \n
                                                         _Master of Science in Mechanical Engineering (MSME)_ \n
                                                         _Expected Graduation in Spring 2025_

                                                    - **California State University, Sacramento** | Sacramento, CA. \n
                                                         _Bachelor's of Science in Mechanical Engineering (BSME)_ \n
                                                         _Graduated in Fall 2023_
                                                         """,
                                                            id="body-text",
                                                        ),
                                                        html.H4("Links:", id="h4", style={"font-weight": 300}),
                                                        html.Hr(style={"width": "88%"}),
                                                        html.Div(
                                                            dbc.Accordion(
                                                                [
                                                                    # + ---- Resume Item ---- +
                                                                    dbc.AccordionItem(
                                                                        [
                                                                            dmc.Group(
                                                                                [
                                                                                    dmc.Button(
                                                                                        "Resume",
                                                                                        id="open-modal",
                                                                                        className="me-1",
                                                                                        n_clicks=0,
                                                                                    ),
                                                                                    html.P(
                                                                                        'Click the "Resume" button to view, download, or save a copy of my resume.',
                                                                                        className="px-1",
                                                                                    ),
                                                                                    dmc.Modal(
                                                                                        children=[
                                                                                            dmc.Container(
                                                                                                [
                                                                                                    html.Iframe(
                                                                                                        id="embedded-pdf",
                                                                                                        src="/assets/Resume.pdf",
                                                                                                        width="480",
                                                                                                        height="730",
                                                                                                        style={
                                                                                                            "width": "100%",
                                                                                                            "align": "center",
                                                                                                        },
                                                                                                    ),
                                                                                                ],
                                                                                                fluid=True,
                                                                                                style={
                                                                                                    "padding": 1,
                                                                                                    "width": "100%",
                                                                                                    "height": "100%",
                                                                                                },
                                                                                            ),
                                                                                            dmc.Group(
                                                                                                [
                                                                                                    dmc.Button(
                                                                                                        "Close",
                                                                                                        color="red",
                                                                                                        variant="outline",
                                                                                                        id="close-modal",
                                                                                                        n_clicks=0,
                                                                                                    )
                                                                                                ],
                                                                                                position="right",
                                                                                            ),
                                                                                        ],
                                                                                        size="xl",
                                                                                        id="modal-center",
                                                                                        centered=True,
                                                                                        title="Resume",
                                                                                        overflow="inside",
                                                                                        shadow="sm",
                                                                                        opened=False,
                                                                                    ),
                                                                                ],
                                                                            )
                                                                        ],
                                                                        title="Resume",
                                                                        id="body-text",
                                                                    ),
                                                                    # + ---- GitHub Item ---- +
                                                                    dbc.AccordionItem(
                                                                        [
                                                                            html.A(
                                                                                html.I(
                                                                                    className="p-1 ms-1 fa-brands fa-github fa-xl",
                                                                                    style={"color": "#9d34b0"},
                                                                                ),
                                                                                href="https://github.com/Belluom1n1",
                                                                                target="_blank",
                                                                            ),
                                                                            "   You can visit my public GitHub page through the link embedded in the icon.",
                                                                            html.P(
                                                                                "Note: Repositories may not be regularly maintained.",
                                                                                className="text-warning fst-italic mx-",
                                                                            ),
                                                                        ],
                                                                        title="GitHub",
                                                                        id="body-text",
                                                                    ),
                                                                    # + ---- LinkedIn Item ---- +
                                                                    dbc.AccordionItem(
                                                                        [
                                                                            html.A(
                                                                                html.I(
                                                                                    className="p-1 ms-1 fa-brands fa-linkedin fa-xl",
                                                                                    style={"color": "#6184f4"},
                                                                                ),
                                                                                href=" LinkedIn ",
                                                                                target="_blank",
                                                                            ),
                                                                            "   You can view my LinkedIn profile by using the link embedded in this icon.",
                                                                        ],
                                                                        title="LinkedIn",
                                                                        id="body-text",
                                                                    ),
                                                                ],
                                                                start_collapsed=True,
                                                                style={"width": "88%"},
                                                            )
                                                        ),
                                                        html.Br(),
                                                    ]
                                                ),
                                                span=6,
                                            ),
                                            # + ----  Work Timeline ---- +
                                            dmc.Col(
                                                html.Div(
                                                    [
                                                        dcc.Markdown(
                                                            "#### Work Experience", id="h4", style={"font-weight": 300}
                                                        ),
                                                        html.Hr(style={"width": "90%"}),
                                                        timeline,
                                                    ],
                                                    style={"align": "start"},
                                                ),
                                                span="auto",
                                            ),
                                        ],
                                        gutter="md",
                                    ),
                                    html.Br(),
                                ],
                                shadow="xl",
                                p="lg",
                                radius="md",
                            ),
                            html.Br(),
                        ],
                        width={"size": 8, "padding": 2},
                    ),
                ],
                justify="center",
            )
        )
    ],
    fluid=True,
    style={"background-color": "#ecf0f1"},
)


# + ---- callbacks ---- +
@callback(
    Output("modal-center", "opened"),
    [Input("open-modal", "n_clicks"), Input("close-modal", "n_clicks")],
    [State("modal-center", "opened")],
)
def toggle_modal(n1, n2, opened):
    """Toggle the modal's opened state when either button is clicked."""
    if n1 or n2:
        return not opened
    return opened
