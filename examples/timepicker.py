import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H3("Examples from timepicker.py"),
        html.P(
            [
                "Default Timepicker with initial time set:",
                dmc.Timepicker(id="example1", value="12:00:00"),
                html.Div(id="output1"),
            ]
        ),
        html.P(
            [
                "Default Timepicker with a format of hh:mm a",
                dmc.Timepicker(id="example2", format="hh:mm a"),
                html.Div(id="output2"),
                "Note the format of the time string returned from a callback",
            ]
        ),
        html.P(
            [
                "Timepicker 24hr clock display",
                dmc.Timepicker(id="example3", value="13:50:30", format="HH:mm:ss"),
            ]
        ),
        html.P(
            [
                "Timepicker disabled",
                dmc.Timepicker(id="example4", value="13:50:30", disabled=True),
            ]
        ),
        html.P(
            [
                "Timepicker with max time allowed (set to 2pm)",
                dmc.Timepicker(id="example5", maxTime="14:00:00"),
            ]
        ),
        html.P(
            [
                "Timepicker with seconds",
                dmc.Timepicker(id="example6", value="13:50:30", maxDetail="second"),
            ]
        ),
    ],
    className="m-5",
)


@app.callback(
    Output("output1", "children"),
    Output("output2", "children"),
    Input("example1", "value"),
    Input("example2", "value"),
)
def update_output(time1, time2):
    msg_a = "Please select a time"
    msg_b = "You have selected: "

    clock1 = msg_b + time1 if time1 else msg_a
    clock2 = msg_b + time2 if time2 else msg_a
    return clock1, clock2


if __name__ == "__main__":
    app.run_server(debug=True)
