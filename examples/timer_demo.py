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
        dbc.CardHeader(html.H3('Timer - mode="countdown"')),
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
        dbc.CardHeader(html.H3('Timer - mode="stopwatch"')),
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
            [
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
                        5000: "",
                        0: "Solid Rocket Booster ignition and LIFTOFF!",
                    },
                ),
                dmc.Timer(
                    id="clock",
                    duration=51000,
                    timer_format={"display": True, "colonNotation": True},
                    disabled=True,
                ),
            ]
        ),
        dbc.Modal(
            dbc.ModalBody(html.Img(src=shuttle, style={"width": "100%"}),),
            id="modal",
            is_open=False,
        ),
    ],
    className="mt-4 m-4 border p-4",
)

"""
===============================================================================
Live Stage Progress
"""

stages_card = dbc.Card(
    [
        dbc.CardHeader(
            html.H3("Update at  `fire_times` ")
        ),
        dbc.CardBody(
            [
                dmc.Timer(
                    id="stages_timer",
                    fire=[2000, 6000, 12000, 18000],
                    duration=20000,
                    rerun=True,
                    mode="stopwatch",
                ),
                dbc.ButtonGroup(
                    [
                        dbc.Button(
                            "stage " + str(i),
                            id="stage" + str(i),
                            color="white",
                            className="m-5 rounded-circle border",
                        )
                        for i in range(1, 5)
                    ],
                    size="lg",
                ),
            ],
        ),
    ],
    className="mt-4 m-4 border p-4",
)


"""
===============================================================================
Update at a time of day
"""

time_of_day_card = dbc.Card(
    [
        dbc.CardHeader(
            html.H3("Timer - Job update with time of day")
        ),
        dbc.CardBody(
            [
                html.Div(
                    [
                        dbc.Button("start", id="start_job", size="lg", color="info", className="m-4"),
                        html.H3(id='job_started'),
                        html.H4(id='next_update',
                            style={"display": "inline-block", "color": "#34558b "},
                        ),
                        html.H5(['Next update in:',
                          #  style={"display": "inline-block", "color": "#34558b "}),
                            dmc.Timer(
                                id="time_of_day_timer",
                                disabled=True,
                                fire=[0],
                                mode="countdown",
                                duration=900000,
                                timer_format={"display": True, "verbose": True},
                                rerun=True,
                            ),
                           ], style={"display": "inline-block", "color": "#34558b "},
                        ),
                    ],
                    className="mx-3 mt-4 p-3 border",
                ),
            ],
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
        dbc.Row(stages_card),
        dbc.Row(shuttle_card),
        dbc.Row(time_of_day_card),
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
    Output("clock", "disabled"),
    Input("start", "n_clicks"),
)
def start(btn_clicks):
    if btn_clicks and btn_clicks >= 0:
        return False, True, False
    else:
        return dash.no_update


@app.callback(
    Output("modal", "is_open"), Input("shuttle_countdown", "at_fire_interval"),
)
def blastoff(at_fire_interval):
    return at_fire_interval == 0


@app.callback(
    [Output("stage" + str(i), "color") for i in range(1, 5)],
    [Output("stage" + str(i), "children") for i in range(1, 5)],
    Input("stages_timer", "at_fire_interval"),
)
def update_stages(at_fire_interval):
    colors = {2000: "white", 6000: "white", 12000: "white", 18000: "white"}
    stage_colors = {2000: "primary", 6000: "success", 12000: "warning", 18000: "info"}
    stage_names = {
        2000: "Stage 1",
        6000: "Stage 2",
        12000: "Stage 3",
        18000: "   Stage 4",
    }

    if at_fire_interval:
        colors[at_fire_interval] = stage_colors[at_fire_interval]
        stage_names[at_fire_interval] = "On " + stage_names[at_fire_interval]
    return list(colors.values()) + list(stage_names.values())


@app.callback(
    Output("job_started", "children"),
    Output("time_of_day_timer",'disabled'),
    Input("start_job", "n_clicks"),
)
def time_of_day_job_starter(start_btn_clicks):
    if start_btn_clicks is None:
        raise PreventUpdate
    if start_btn_clicks > 1:
        raise PreventUpdate
    # if start_btn_clicks == 0:
    #     msg = 'Start Job'
    #     pause = True
    if start_btn_clicks ==1:
        start_time = dt.datetime.now().time().strftime('%I:%M %p')
        msg= 'Job started at ' + start_time + '  Updates every 15 minutes'
        pause = False

    return msg, pause

@app.callback(
    Output("next_update", "children"),
    Input("time_of_day_timer", "at_fire_interval"),
    prevent_initial_call=True

)
def update_time_of_day_job(at_fire_interval):
    next_update = dt.datetime.now() + dt.timedelta(seconds=900)
    return f'Next update at {next_update}'


if __name__ == "__main__":
    app.run_server(debug=True)
