import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc


from datetime import date, timedelta, datetime, time


external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


countdown_timer = dmc.CountdownTimer(
    id="countdown", pause=False, starting_duration=0, remaining_duration=0
)


time_input_card = html.Div(
    dbc.Card(
        [
            "max detail: one of 'hour', 'minute', 'second', Default: 'minute'",
            dcc.Input(id="input_maxDetail", debounce=True),
            "format Supported values are: H, HH, h, hh, m, mm, s, ss, a. example h:m:s a",
            dcc.Input(id="input_format", debounce=True),
            dmc.Timepicker(
                id="time_picker",
                value=datetime.now().time(),
                #  format= "h:m:s a",
                format="h:m:s a",
                #  maxTime="23:30:30",
                # 	minTime="12:10:10",
                disabled=False,
                # disableClock=True,
            ),
            html.Span(dbc.Badge(id="time_selected", color="primary", className="m-2")),
        ]
    )
)


app.layout = dbc.Container(
    [
        countdown_timer,
        dbc.Row(
            dbc.Col(time_input_card, width=3),
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("time_selected", "children"),
    Output("time_picker", "format"),
    Output("time_picker", "maxDetail"),
    #  Output('time_picker', 'disabled'),
    Input("time_picker", "value"),
    Input("input_maxDetail", "value"),
    Input("input_format", "value"),
)
def update_date_countdown(time_selected, max, format):
    max = "minute" if max is None else max
    print("time", time_selected, type(time_selected))
    print(format)

    time_obj = time.fromisoformat(time_selected)
    time_string = time_obj.strftime("%I:%M:%S %p")

    return f"selected date: {time_string}", format, max


if __name__ == "__main__":
    app.run_server(debug=True)
