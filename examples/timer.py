import dash
import dash_more_components as dmc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html

import datetime as dt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dmc.Timer(id="mytimer", countdown_duration=500000),
        html.H2('Timer Controls'),

        dcc.RadioItems(
            id="timer_control",
            options=[{"label": i, "value": i} for i in (["Start", "Pause"])],
            value="Pause",
        ),
        html.Button('Reset', id="reset"),

        html.Br(),
        html.H2('Timer Props'),
        "interval",
        dcc.Input(id="interval", type="number", value=1000, style={'display':'block'}),
        "max_intervals",
        dcc.Input(id='max_intervals', type='number', value=-1, style={'display':'block'}),
        "countdown_duration",
        dcc.Input(id='countdown_duration',type='number', value=60000, debounce=True, style={'display':'block'}),

        html.Br(),
        html.H2('Timer Output'),
        html.Div(id="n_intervals_text"),
        html.Div(id= 'counter_text'),
    ],
    className="m-4",
)





#======== timer properties  ===========
@app.callback(
    Output("mytimer", "reset"),
    Output("mytimer", 'disabled'),
    Output("mytimer", 'interval'),
    Output("mytimer", 'max_intervals'),
    Output("mytimer", "countdown_duration"),

    Input("reset", 'n_clicks'),
    Input("timer_control", "value"),
    Input('interval', "value"),
    Input('max_intervals', "value"),
    Input('countdown_duration', "value"),
)
def update_reset(clicks, timer_control, interval, max_interval, countdown):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]['prop_id'].split('.')[0]

    pause = True if timer_control == "Pause" else False
    print(countdown)
    reset= False
    if input_id == 'reset':
        reset = True if clicks and clicks > 0 else False

    return reset, pause, interval, max_interval, countdown



#======== output =====================
@app.callback(
    Output('counter_text',"children"),
    Output('n_intervals_text',"children"),
    Input("mytimer", "n_intervals"),
    Input("mytimer", "remaining_duration")
)
def update_output(n, remaining_time):
    n_int_text = f"n_intervals:  {n}"

    print('remaining', remaining_time)
    countdown_text = (
        f"Countdown remaining_duration {str(dt.timedelta(seconds=int(remaining_time / 1000)))}"
    )
    return countdown_text, n_int_text




if __name__ == "__main__":
    app.run_server(debug=True)
