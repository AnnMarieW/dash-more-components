import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc

import datetime as dt

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dmc.CountdownTimer(id="countdown", pause=True, starting_duration=10),
        dbc.RadioItems(
            id="pause",
            options=[
                {"label": "Start", "value": "False"},
                {"label": "Pause", "value": "True"},
            ],
            value="True",
        ),
        html.Span(dbc.Badge(id="badge_output", color="success", className="m-2")),
        html.H3(id="timer_end_text"),
    ],
    className="m-4",
)


@app.callback(
    Output("badge_output", "children"),
    Output("timer_end_text", "children"),
    Output("countdown", "pause"),
    Input("pause", "value"),
    Input("countdown", "n_seconds"),
    State("countdown", "remaining_duration"),
)
def display_badge(pause, n, remaining_time):
    pause = True if pause == "True" else False

    badge_text = (
        f"Checking for updates in {str(dt.timedelta(seconds=remaining_time))}"
        if remaining_time
        else ""
    )
    timer_end_text = "You Win!!" if (n) and (remaining_time == 0) else ""
    return badge_text, timer_end_text, pause


if __name__ == "__main__":
    app.run_server(debug=True)
