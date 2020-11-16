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


"""
===============================================================================
control panel
"""

intro_text = dcc.Markdown(
    """
The Timer component adds new props to dcc.Interval to make timer/stopwatch functionality available.

 1. __duration__  Sets the number of milliseconds the timer will run.  If -1 the duration has no limit (the default)
     and if 0 then the timer stops running.
 2. __timer:__ Number of milliseconds remaining on the timer.  (read-only) 
 3. __timer:__ Number of milliseconds elapse time (read-only)
 4. __reset:__ starts the timer  with the given prop settings.
 5. __rerun:__ automatically restarts the timer
 
All other props from dcc.Interval are unchanged. Start and Pause options are controlled by the disabled prop

#### When used in a Dash Callback:
  - Time is formatted in a human readable way using the datetime library's timedelta. 
   See different formatting by changing the duration prop.
    - str(dt.timedelta(milliseconds=int(timer_milliseconds)))   
    
    
  - Precision of the timer is controlled by the `interval` prop.  This also determines how often a callback will fire.  
    - For example: 
        - interval=1000 counts down by seconds,  
        - interval=60000 counts down by minutes  
    
#### When timer messages updated clientside
  - When timer messages is provided using the `messages` prop, the messages is updated clientside.
  - Time is formatted in a human readable way using pretty-ms
     - For example:  
        - 1337000000 → 15d 11h 23m 20s
        - '15 days 11 hours 1 minute 9 seconds'   (verbose option - which translates well to other languages in the browser)
      
            

"""
)


intro_card = dbc.Card(
    [dbc.CardHeader(html.H3("Timer Component and App Notes")), intro_text,],
    className="p-1 mt-4",
)
props_card = dbc.Card(
    [
        html.H4("Timer props:", className="m-2"),
        html.Button("Reset", id="reset", className="m-4"),
        dcc.RadioItems(
            id="timer_control",
            options=[{"label": i, "value": i} for i in (["Start", "Pause"])],
            value="Pause",
            className="m-2",
            inputClassName="m-2",
        ),
        dcc.RadioItems(
            id="mode",
            options=[{"label": i, "value": i} for i in (["Countdown", "Stopwatch"])],
            value="Countdown",
            className="m-2",
            inputClassName="m-2",
        ),
        dcc.Checklist(
            id="rerun",
            className="mb-2 ml-2",
            options=[{"label": "Repeat", "value": "Repeat"}],
            inputClassName="m-2",
        ),
        "interval",
        dcc.Input(id="interval", type="number", value=1000, className="m-2"),
        "max_intervals",
        dcc.Input(id="max_intervals", type="number", value=-1, className="m-2"),
        "duration",
        dcc.Input(
            id="duration", type="number", value=30000, debounce=True, className="m-2"
        ),
        html.H4("Timer read-only props", className="mt-4"),
        html.Div(id="n_intervals_text"),
        html.Div(id="timer_text"),
    ],
    className="mb-4 p-2",
)
"""
===============================================================================
use cases
"""
dash_callback_card = dbc.Card(
    [
        dbc.CardHeader(html.H3("Updated in Dash Callback")),
        dbc.CardBody(
            [
                html.H5("1.  Countdown timer"),
                "set props using control panel",
                html.Div(
                    id="badge_output",
                    className="m-4  bg-success border rounded text-white",
                ),
                html.H3(id="timer_end_text"),
                html.H5("2.  Stopwatch timer"),
                "set props using control panel",
                html.Div(
                    id="timer2", className="m-4  bg-success border rounded text-white"
                ),
            ]
        ),
    ],
    className="m-1",
)

clientside_card = dbc.Card(
    [
        dbc.CardHeader(html.H3("Updated clientside")),
        dbc.CardBody(
            [
                html.H5("1.  Countdown timer"),
                "set props using control panel",
                html.H1(
                    [
                        "This is a test",
                        dmc.Timer(
                            id="mytimer",
                            duration=5000,
                            timer_format={"display": True, "colonNotation": True},
                            messages={1000: "Checking for updates in: ",}
                        ),
                    ],
                    className="m-4  bg-success border rounded text-white",
                ),
                html.H5("2.  Count up timer"),
                "on a 10 second repeat timer",
                html.Div(
                    dmc.Timer(
                        id="timer2_timer",
                        duration=10000,
                       # duration=-1,
                        rerun=True,
                        mode="stopwatch",
                        messages={1000:"Loading data. This will take around 10 seconds. It has been"},
                        timer_format=({'display': True})
                    ),
                    className="m-4  bg-success border rounded text-white",
                ),
            ]
        ),
    ],
    className="m-1",
)


"""
===============================================================================
Timer with dict
"""

five_min_dict = {
    1000: "Task submitted! This will take around five minutes.",
    10000: "Task submitted! This will take around five minutes. It has been 10 seconds.",
    60000: "Task submitted! This will take around five minutes. It has been one minute.",
    120000: "Task submitted! This will take around five minutes. It has been two minutes.",
    180000: "Task submitted! This will take around five minutes. It has been three minutes.",
    240000: "Task submitted! This will take around five minutes. It has been four minutes.",
    300000: "Task submitted! It has been five minutes - it should be done momentarily!",
    330000: "Task submitted! This will take around five minutes. It has been five minutes and 30 seconds. It's taking a little longer than expected, hang tight!",
    360000: "Task submitted! This should have taken around five minutes. It has been six minutes. Something might've gone wrong. Reach out to eli@acme.corp.",
    420000: "Task submitted! This should have taken around five minutes. It is taking much longer than expected. Something might've gone wrong. Reach out to eli@acme.corp.",
}
five_min_card = dbc.Card(
    [
        dbc.CardHeader(html.H4("Timer messages updated with dict")),
        dbc.CardBody(
            [
                "On a 5 minute repeat timer.  Message updated in Dash callback",
                html.Div(
                    dmc.Timer(
                        id="five_min_timer",
                        duration=420000,
                    #    duration=-1,
                        rerun=True,
                        messages=five_min_dict,
                        mode="stopwatch",
                        timer_format={"display": False},
                    ),
                    className="m-4  bg-light border rounded",
                ),
                # dash callback div
                html.Div(id="five_min", className="m-4  bg-light border rounded"),
            ]
        ),
    ],
    className="m-3",
)


"""
===============================================================================
Timepicker
"""

clock_card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    dmc.Timepicker(
                        id="time_picker", value="12:00:00", maxDetail="second"
                    ),
                ),
                dbc.Col(
                    dbc.Button(
                        "Start timer timer",
                        id="start_btn",
                        n_clicks=0,
                        color="primary",
                        size="sm",
                    ),
                ),
            ]
        ),
    ],
    body=True,
    className="m-3",
)


time_input_card = dbc.Card(
    [
        dbc.CardHeader(html.H4("Update duration with timepicker")),
        dbc.CardBody(
            [
                "Timer messages updated clientside",
                clock_card,
                html.Div(  # time updated clientside
                    dmc.Timer(
                        id="time_picker_timer",
                        duration=1000,
                     #   duration=-1,
                        disabled=True,
                        messages={1000:"Checking for updates in: "},
                        timer_format={'display': True}
                    ),
                    className="m-4  bg-success border rounded text-white",
                ),
                html.Div(
                    id="time_input",  # time updated in dash callbak
                    className="m-4  bg-light border rounded",
                ),
            ]
        ),
    ],
    className="m-3",
)


"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(props_card, width=4),
                dbc.Col(dash_callback_card, width=4),
                dbc.Col(clientside_card, width=4),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [five_min_card, time_input_card],
                    width={"size": 6, "order": 1, "offset": 4},
                )
            ]
        ),
        dbc.Row(intro_card),
    ],
    className="m-4",
)


"""
===============================================================================
Callbacks
"""


def formatted(milliseconds):
    return str(dt.timedelta(milliseconds=int(milliseconds)))


# ======== timer properties  ===========
@app.callback(
    Output("mytimer", "reset"),
    Output("mytimer", "disabled"),
    Output("mytimer", "rerun"),
    Output("mytimer", "interval"),
    Output("mytimer", "max_intervals"),
    Output("mytimer", "duration"),
    Output("mytimer", "mode"),
    Input("reset", "n_clicks"),
    Input("timer_control", "value"),
    Input("rerun", "value"),
    Input("interval", "value"),
    Input("max_intervals", "value"),
    Input("duration", "value"),
    Input("mode", "value"),
)
def update_reset(clicks, timer_control, rerun, interval, max_interval, timer, mode):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]

    pause = True if timer_control == "Pause" else False

    rerun = True if rerun else False

    mode = "countdown" if mode == "Countdown" else "stopwatch"

    reset = False
    if input_id == "reset":
        reset = True if clicks and clicks > 0 else False

    print(reset, pause, rerun, interval, max_interval, timer, mode)
    return reset, pause, rerun, interval, max_interval, timer,  mode


# ======== read only prop output =====================
@app.callback(
    Output("timer_text", "children"),
    Output("n_intervals_text", "children"),
    Input("mytimer", "n_intervals"),
    Input("mytimer", "timer"),
)
def update_output(n, timer):
    return (f"n_intervals:  {n}", f"timer: {timer}")


# =======  timer timer  =====
@app.callback(
    Output("badge_output", "children"),
    Output("timer_end_text", "children"),
    Input("mytimer", "timer"),
)
def display_timer(remaining_time):
    if remaining_time is not None:
        badge_text = f"Checking for updates in {formatted(remaining_time)}"
        timer_end_text = "Results are in!" if remaining_time == 0 else ""
    else:
        raise PreventUpdate
    return badge_text, timer_end_text


# =======  timer timer  =====
@app.callback(
    Output("timer2", "children"),
    Input("mytimer", "timer"),
    State("mytimer", "duration"),
)
def display_timer(elapse_time, duration):
    duration = 0 if duration is None else duration
    return (
        f"Loading data. This will take around {int(duration / 1000) } seconds. It has been {int(elapse_time/1000)} seconds.",
    )


# ============ 5 min timer with dict ===
@app.callback(
    Output("five_min", "children"),
    Input("five_min_timer", "timer"),
    State("five_min_timer", "duration"),
)
def five_min(timer, duration):
    if timer and (timer in five_min_dict):
        return five_min_dict[timer]
    else:
        return dash.no_update


# =======  Timer picker ============


@app.callback(
    Output("time_picker_timer", "duration"),
    Output("time_picker_timer", "disabled"),
    Input("start_btn", "n_clicks"),
    State("time_picker", "value"),
)
def update_date_timer(click, time_selected):
    if click <= 0:
        raise PreventUpdate
    time_obj = dt.datetime.strptime(time_selected, "%H:%M:%S")
    time_now = dt.datetime.now()
    time_dif = time_obj - time_now
    duration = time_dif.seconds * 1000
    return duration, False


if __name__ == "__main__":
    app.run_server(debug=True)
