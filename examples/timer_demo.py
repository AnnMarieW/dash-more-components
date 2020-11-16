import dash
from dash.exceptions import PreventUpdate
import dash_more_components as dmc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc
import datetime as dt

external_stylesheets = [dbc.themes.BOOTSTRAP]

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def formatted(milliseconds):
    return str(dt.timedelta(milliseconds=int(milliseconds)))


"""
===============================================================================
Markdown
"""

intro_text = dcc.Markdown(
    """
"""
)


"""
===============================================================================
Countdown card
"""

timer_countdown_card = dbc.Card(
    [
        dbc.CardHeader(html.H3("Timer - Countdown Mode")),
        dbc.CardBody(
            [
                #  "timer_format={'verbose':True}",
                html.Div(
                    [
                        html.Div(
                            "Data updates every 30 seconds.  Updating in...",
                            style={"display": "inline-block"},
                        ),
                        html.H5(
                            dmc.Timer(
                                mode="countdown",
                                duration=30000,
                                timer_format={"display": True, "verbose": True},
                                rerun=True,
                            ),
                            className="d-inline-block",
                        ),
                    ],
                    className="mx-3 mt-4",
                ),
                html.Div(
                    [
                        html.H4(
                            "Next event starts in in...",
                            style={"display": "inline-block", "color": "#34558b "},
                        ),
                        html.H5(
                            dmc.Timer(
                                mode="countdown",
                                duration=100000000,
                                timer_format={"display": True, "verbose": True},
                                rerun=True,
                            ),
                            style={"display": "inline-block", "color": "#34558b "},
                        ),
                    ],
                    className="mx-3 mt-4 p-3 border",
                ),
                #  "timer_format={'display': True}  (default)",
                html.Div(
                    [
                        html.H3(
                            "Hurry!  Special offer ends in...",
                            style={"display": "inline-block"},
                        ),
                        html.H3(
                            dbc.Badge(
                                dmc.Timer(
                                    mode="countdown",
                                    duration=10000000,
                                    timer_format={"display": True},
                                    rerun=True,
                                ),
                                className="d-inline-block",
                                color="danger",
                            )
                        ),
                    ],
                    className="mx-3 mt-4",
                ),
            ],
        ),
    ],
    className="m-1",
)


"""
===============================================================================
Stopwatch
"""

timer_stopwatch_card = dbc.Card(
    [
        dbc.CardHeader(html.H3("Timer - Stopwatch Mode")),
        dbc.CardBody(
            [
                # "timer_format={'verbose':True}",
                html.Div(
                    [
                        html.Div(
                            "Loading data. This will take around 30 seconds. It has been:",
                            style={"display": "inline-block"},
                        ),
                        html.H5(
                            dmc.Timer(
                                mode="stopwatch",
                                duration=30000,
                                timer_format={"display": True, "verbose": True},
                                rerun=True,
                            ),
                            className="d-inline-block",
                        ),
                    ],
                    className="mx-3 mt-4",
                ),
                # "timer_format={'colonNotation':True}",
                html.Div(
                    [
                        html.Div("Updating in...", style={"display": "inline-block"}),
                        html.H5(
                            dmc.Timer(
                                mode="stopwatch",
                                duration=10000000,
                                timer_format={"display": True, "colonNotation": True},
                                rerun=True,
                            ),
                            className="d-inline-block",
                        ),
                    ],
                    className="mx-3 mt-4 mb-4",
                ),
                html.H4(
                    dmc.Timer(
                        mode="stopwatch",
                        duration=421000,
                        rerun=True,
                        messages={
                            1000: "Task submitted! This will take around five minutes.",
                            10000: "Task submitted! This will take around five minutes. It has been 10 seconds.",
                            30000: "Task submitted! This will take around five minutes. It has been 30 seconds.",
                            60000: "Task submitted! This will take around five minutes. It has been one minute.",
                            120000: "Task submitted! This will take around five minutes. It has been two minutes.",
                            180000: "Task submitted! This will take around five minutes. It has been three minutes.",
                            240000: "Task submitted! This will take around five minutes. It has been four minutes.",
                            300000: "Task submitted! It has been five minutes - it should be done momentarily!",
                            330000: "Task submitted! This will take around five minutes. It has been five minutes and 30 seconds. It's taking a little longer than expected, hang tight!",
                            360000: "Task submitted! This should have taken around five minutes. It has been six minutes. Something might've gone wrong. Reach out to eli@acme.corp.",
                            420000: "Task submitted! This should have taken around five minutes. It is taking much longer than expected. Something might've gone wrong. Reach out to eli@acme.corp.",
                        },
                    ),
                    className="mx-3 mt-4 p-3 border",
                    style={"color": "#34558b"},
                ),
            ],
        ),
    ],
    className="m-1",
)

"""
===============================================================================
Space Shuttle
"""
shuttle = (
    "https://cdn.pixabay.com/photo/2012/11/28/10/33/rocket-launch-67641_960_720.jpg"
)

shuttle_card = html.Div(
    [
        dbc.Button("start", id="start", size="lg", color="info", className="m-4"),
        html.H1("Space Shuttle Endeavour T-50 seconds and counting"),
        html.H3(
            dmc.Timer(
                id="shuttle_countdown",
                mode="countdown",
                disabled=True,
                duration=51000,
                fire=[0],
                messages={
                    50000: "(T-50 seconds) Orbiter transfers from ground to internal power",
                    31000: "(T-31 seconds) Ground Launch Sequencer is go for auto sequence start",
                    16000: "(T-16 seconds) Activate launch pad sound suppression system",
                    10000: "(T-10 seconds) Activate main engine hydrogen burnoff system",
                    6000: "(T-6 seconds) Main engine start",
                    5000: "Five",
                    4000: "Four",
                    3000: "Three",
                    2000: "Two",
                    1000: "One",
                    0: "Solid Rocket Booster ignition and LIFTOFF!",
                },
            )
        ),
        dbc.Modal(
            dbc.ModalBody(html.Img(src=shuttle, style={"width": "100%"}),),
            id="modal",
            size="lg",
            is_open=False,
        ),
    ],
    className="mt-4 m-4 border p-4",
)


"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    [
        dbc.Row([dbc.Col(timer_countdown_card), dbc.Col(timer_stopwatch_card),]),
        dbc.Row(shuttle_card),
    ],
    className="m-4",
)


"""
===============================================================================
Callbacks
"""


@app.callback(
    Output("shuttle_countdown", "disabled"),
    Output("shuttle_countdown", "reset"),
    Input("start", "n_clicks"),
)
def start(btn_clicks):
    if btn_clicks and btn_clicks >= 0:
        return False, True
    else:
        return dash.no_update


@app.callback(
    Output("modal", "is_open"), Input("shuttle_countdown", "at_interval"),
)
def blastoff(at_interval):
    return at_interval == 0


if __name__ == "__main__":
    app.run_server(debug=True)