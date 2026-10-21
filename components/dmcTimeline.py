"""Dash Mantine Components: Timeline.

-> Timeline Component to outline projects.
-> Styled with dash_mantine_components.
-> Date: 08/08/2023.
"""

# Imports
import dash
from dash import dcc, html, Dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


# + --- layout --- +
def timeline():
    """Timeline for web-app using dash mantine components."""
    return dmc.Timeline(
        active=8,
        bulletSize=15,
        color="primary",
        lineWidth=2,
        radius="xl",
        className="p-1 me-1",
        children=[
            dmc.TimelineItem(
                title="HLP Leadership Program",
                lineVariant="dashed",
                children=[
                    dmc.Text(
                        [
                            "Working with a C.E. Student to build a ",
                            dmc.Anchor("Smart Parking ", href="/pages/Projects", size="sm"),
                            "System using a RaspberryPi and Python machine learning classification algorithms to",
                            "update an Android mobile application and displaying available parking spaces in a parking garage.",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Text(["NSF Grant: DUE 1953752"], color="dimmed", size="xs"),
                    dmc.Text(["05/2023 - 08/2023"], color="dimmed", size="sm"),
                ],
            ),
            dmc.TimelineItem(
                title="Peer Instructed Learning Facilitator",
                lineVariant="solid",
                children=[
                    dmc.Text(
                        [
                            "Facilitated a class of 15 undergraduate Mechanical and Civil Engineering students",
                            " to build confidence in problem solving and engineering concepts.",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Text(["08/2022 - 12/2022"], color="dimmed", size="sm"),
                ],
            ),
            dmc.TimelineItem(
                title="Costco Meat Cutter",
                lineVariant="solid",
                children=[
                    dmc.Text(
                        [
                            "09/2017 - 10/2023",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                ],
            ),
            dmc.TimelineItem(
                title="Service Consultant",
                lineVariant="solid",
                children=[
                    dmc.Text(
                        [
                            "Responsible for training Service Advisors to write and complete accurate repair orders, control ",
                            "shop workflow, and customer service.  Worked as the shop dispatcher, assisted with Warranty claims.",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Text(["03/2015 - 10/2017"], color="dimmed", size="sm"),
                ],
            ),
            dmc.TimelineItem(
                title="Service Advisor",
                lineVariant="solid",
                children=[
                    dmc.Text(
                        [
                            "Service Advisor at San Francisco Honda. ",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Text(["02/2014 - 03/2015"], color="dimmed", size="sm"),
                ],
            ),
            dmc.TimelineItem(
                title="Assistant Service Manager",
                lineVariant="solid",
                children=[
                    dmc.Text(
                        [
                            "Assistant Service Manager at Toyota of Lake City.",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Text(["09/2011 - 03/2014"], color="dimmed", size="sm"),
                ],
            ),
            dmc.TimelineItem(
                title="Service Advisor",
                lineVariant="solid",
                children=[
                    dmc.Text(
                        ["Service Advisor at Elk Grove Honda, Elk Grove, CA."],
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Text(["06/2009 - 08/2011"], color="dimmed", size="sm"),
                ],
            ),
            dmc.TimelineItem(
                title="Certified Used Car Recon Assistant Manager",
                lineVariant="solid",
                children=[
                    dmc.Text(
                        [
                            "Assistant to the Used Car Manager at Mel Rapton Honda.",
                            "responsible for safety inspections, reconditioning, and certification.",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Text(["01/2007 - 06/2009"], color="dimmed", size="sm"),
                ],
            ),
            dmc.TimelineItem(
                title="Service Technician",
                lineVariant="solid",
                children=[
                    dmc.Text(
                        [
                            "Service Technician at Mel Rapton Honda",
                        ],
                        color="dimmed",
                        size="sm",
                    ),
                    dmc.Text(["01/2007 - 06/2009"], color="dimmed", size="sm"),
                ],
            ),
        ],
    )
