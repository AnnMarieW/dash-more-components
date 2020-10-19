"""
 TODO -

"""


import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
import datetime as dt

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


countdown_timer = dmc.CountdownTimer(
    id="countdown", pause=True, starting_duration=0, remaining_duration=0
)

countdown_timer2 = dmc.CountdownTimer(
    id="countdown2", pause=True, starting_duration=0, remaining_duration=0
)
"""
========================================================================================================================
input card
"""
countdown_input_card = html.Div(
    dbc.Card(
        [
            html.H4("Countdown Timer input"),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("Seconds", addon_type="prepend"),
                    dbc.Input(
                        id="seconds",
                        placeholder=f"time in seconds",
                        type="number",
                        debounce=True,
                        value=0,
                        min=0,
                        max=60,
                    ),
                ],
                className="m-1",
                size="sm",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("Minutes", addon_type="prepend"),
                    dbc.Input(
                        id="minutes",
                        type="number",
                        debounce=True,
                        value=0,
                        min=0,
                        max=60,
                    ),
                ],
                className="m-1",
                size="sm",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("Hours", addon_type="prepend"),
                    dbc.Input(
                        id="hours",
                        type="number",
                        debounce=True,
                        value=0,
                        min=0,
                        max=24,
                        step=1,
                    ),
                ],
                className="m-1",
                size="sm",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("Days", addon_type="prepend"),
                    dbc.Input(id="days", type="number", debounce=True, value=0, min=0),
                ],
                className="m-1",
                size="sm",
            ),
            dbc.InputGroup(
                [
                    dbc.InputGroupAddon("", addon_type="prepend"),
                    dbc.RadioItems(
                        id="pause",
                        options=[
                            {"label": "Start", "value": "False"},
                            {"label": "Pause", "value": "True"},
                        ],
                        value="True",
                    ),
                ],
                className="m-3",
                size="sm",
            ),
        ],
        body=True,
        className="m-4",
    )
)


calendar_input_card = html.Div(
    dbc.Card(
        [
            dcc.DatePickerSingle(
                id="date_picker",
                date=dt.datetime.today().strftime("%Y-%m-%d"),
            ),
            html.Span(
                dbc.Badge(id="countdown_to_date", color="primary", className="m-2")
            ),
        ]
    )
)

time_input_card = html.Div(
    dbc.Card(
        [
            html.H4("Countdown to a time of day"),
            dbc.Row(
                [
                    dbc.Col(
                        dmc.Timepicker(
                            id="time_picker",
                            value="12:00:00",
                            maxDetail="second",
                        ),
                    ),
                    dbc.Col(
                        dbc.Button(
                            "Start countdown timer",
                            id="start_btn",
                            n_clicks=0,
                            color="primary",
                            size="sm",
                        ),
                    ),
                ]
            ),
            html.Span(
                dbc.Badge(id="countdown_to_time", color="success", className="m-2")
            ),
        ],
        body=True,
        className="m-3",
    )
)

"""
========================================================================================================================
results cards
"""


bootstrap_progress_card = html.Div(
    [
        dbc.Card(
            [
                html.H4("Bootsrap Progress Bar"),
                html.Div(dbc.Progress(id="progress")),
            ],
            body=True,
            className="m-3",
        )
    ]
)

daq_progress_card = html.Div(
    [
        dbc.Card(
            [
                html.H4("Dash Daq Progress Bar"),
                html.Div(
                    daq.GraduatedBar(
                        id="daq_bar",
                        vertical=True,
                        showCurrentValue=True,
                        max=100,
                        value=10,
                    )
                ),
            ],
            body=True,
            className="m-3",
        )
    ]
)

text_output_card = html.Div(
    [
        dbc.Card(
            [
                html.H4("Time Remaining (formatted)"),
                html.Span(
                    dbc.Badge(id="badge_output", color="success", className="m-2")
                ),
                html.H3(id="timer_end_text"),
            ],
            body=True,
            className="m-3",
        )
    ]
)


time_left_cards = dbc.Card(
    [
        html.H4("Time Remaining:"),
        dbc.CardGroup(
            [
                dbc.Card(
                    [
                        dbc.CardHeader(html.H5("Days")),
                        dbc.CardBody(id="days_left"),
                    ]
                ),
                dbc.Card(
                    [
                        dbc.CardHeader(html.H5("Hours")),
                        dbc.CardBody(id="hours_left"),
                    ]
                ),
                dbc.Card(
                    [
                        dbc.CardHeader(html.H5("Minutes")),
                        dbc.CardBody(id="minutes_left"),
                    ]
                ),
                dbc.Card(
                    [
                        dbc.CardHeader(html.H5("Seconds")),
                        dbc.CardBody(id="seconds_left"),
                    ]
                ),
            ],
            className="text-nowrap",
        ),
    ],
    className="m-3",
    body=True,
)
"""
========================================================================================================================
Layout
"""
app.layout = dbc.Container(
    [
        countdown_timer,
        countdown_timer2,
        dbc.Row(
            [
                dbc.Col(countdown_input_card, width=3),
                dbc.Col(
                    html.Div(
                        [
                            text_output_card,
                            bootstrap_progress_card,
                            daq_progress_card,
                            time_left_cards,
                        ]
                    ),
                    width=6,
                ),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [time_input_card],
                    width={"size": 6, "offset": 3},
                ),
            ]
        ),
    ],
    fluid=True,
)
"""
========================================================================================================================
callbacks
"""


@app.callback(
    Output("countdown", "starting_duration"),
    Output("countdown", "pause"),
    Input("days", "value"),
    Input("hours", "value"),
    Input("minutes", "value"),
    Input("seconds", "value"),
    Input("pause", "value"),
)
def set_timer(days, hours, minutes, seconds, pause):
    pause = True if pause == "True" else False
    return days * 86400 + hours * 3600 + minutes * 60 + seconds, pause


@app.callback(
    Output("badge_output", "children"),
    Output("timer_end_text", "children"),
    Input("countdown", "n_seconds"),
    State("countdown", "remaining_duration"),
)
def display_badge(n, remaining_time):
    badge_text = f"Checking for updates in {str(dt.timedelta(seconds=remaining_time))}"
    timer_end_text = "You Win!!" if (n) and (remaining_time == 0) else ""
    return badge_text, timer_end_text


@app.callback(
    Output("days_left", "children"),
    Output("hours_left", "children"),
    Output("minutes_left", "children"),
    Output("seconds_left", "children"),
    Input("countdown", "n_seconds"),
    State("countdown", "remaining_duration"),
)
def display_time_remaining(n, remaining_time):
    days_text=''
    hours, minutes, seconds = 0, 0, 0
    if n:
        time_text = str(dt.timedelta(seconds=remaining_time))
        if "day" in time_text:
            days_text, _, time_text = time_text.partition(", ")
        time_object = dt.datetime.strptime(time_text, "%H:%M:%S")

        hours = time_object.hour
        minutes = time_object.minute
        seconds = time_object.second

    return days_text, hours, minutes, seconds


@app.callback(
    Output("progress", "value"),
    Output("progress", "children"),
    Output("daq_bar", "value"),
    Input("countdown", "starting_duration"),
    Input("countdown", "remaining_duration"),
)
def update_progress(start, remaining):
    progress = 0
    if start and start > 0:
        progress = int(remaining / start * 100)
    # only add text after 5% progress to ensure text isn't squashed too much
    return progress, f"{progress} %" if progress >= 5 else "", progress


@app.callback(
    Output("countdown_to_time", "children"),
    Output("countdown2", "starting_duration"),
    Output("countdown2", "pause"),
    Input("countdown2", "remaining_duration"),
    Input("start_btn", "n_clicks"),
    State("time_picker", "value"),
)
def update_date_countdown(remaining, click, time_selected):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]

    text = f"Countdown to {time_selected}: {str(dt.timedelta(seconds=remaining))}"

    if input_id == "start_btn":
        print(time_selected)

        time_obj = dt.datetime.strptime(time_selected, "%H:%M:%S")
        time_now = dt.datetime.now()
        time_dif = time_obj - time_now
        starting_duration = time_dif.seconds
        return text, starting_duration, False

    return text, dash.no_update, dash.no_update



if __name__ == "__main__":
    app.run_server(debug=True)
