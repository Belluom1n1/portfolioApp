# + --- imports --- +
from dash import Dash, State, callback, Input, Output, html, clientside_callback
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# + --- import theme --- +
SpaceLab = dbc.themes.SPACELAB
Icons = dbc.icons.FONT_AWESOME
load_figure_template(["spacelab", "spacelab_dark"])


# + --- color mode switcher --- +
color_mode_switch = html.Span(
    [
        dbc.Label(className="fa fa-moon", html_for="switch"),
        dbc.Switch(id="switch", value=False, className="d-inline-block ms-1", persistence=True),
        dbc.Label(className="fa fa-sun", html_for="switch"),
    ]
)

# + --- update theme for graph & table components --- +
# Add theme to component properties in the following format:
#   **{'data'-bs-theme', 'dark'}
#   then, finish adding callback

# + --- declare app --- +
app = Dash(__name__, external_stylesheets=[SpaceLab, Icons])

# + --- layout --- +
app.layout = dbc.Container(
    [
        # component,
        # color_mode_switch,
        # componet
    ]
)


# + --- callbacks --- +
clientside_callback(
    """
    (switchOn) => {
        document.documentElement.setAttribute("data-bs-theme", switchOn ? "light" : "dark");
        return window.dash_clientside.no_update;
    }
    """,
    Output("switch", "id"),
    Input("switch", "value"),
)

if "__name__" == "__main__":
    app.run_server(debug=True)
