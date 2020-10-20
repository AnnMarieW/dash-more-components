import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc
import datetime as dt

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H3("Examples from datetimepicker.py"),
        html.P(
            [
                "Default datetimepicker with initial time set:",
                dmc.Datetimepicker(id="example1", value=dt.datetime.now()),
                html.Div(id="output1"),
            ]
        ),
    ],
    className="m-5",
)

#
# @app.callback(
#     Output("output1", "children"),
#     Output("output2", "children"),
#     Input("example1", "value"),
#     Input("example2", "value"),
# )
# def update_output(time1, time2):
#     msg_a = "Please select a time"
#     msg_b = "You have selected: "
#
#     clock1 = msg_b + time1 if time1 else msg_a
#     clock2 = msg_b + time2 if time2 else msg_a
#     return clock1, clock2


if __name__ == "__main__":
    app.run_server(debug=True)
