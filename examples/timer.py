import dash
import dash_more_components as dmc
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc
import datetime as dt

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dmc.Timer(id="mytimer", interval=1000),
        dbc.RadioItems(
            id="timer_control",
            options=[{"label": i, "value": i} for i in (["Start", "Pause"])],
            value="Pause",
        ),
        html.Button('Reset', id="reset"),
        html.H3(dbc.Badge(id="badge_output", color="success", className="m-2")),
        html.H3(id="timer_end_text"),
        html.H3(id= 'counter'),
    ],
    className="m-4",
)

@app.callback(
    Output("mytimer", "reset"),
    Input("reset", 'n_clicks')
)
def update_reset(n):
    return True if n and n > 0 else False


@app.callback(
    Output("badge_output", "children"),
    Output("timer_end_text", "children"),
    Output('counter',"children"),
    Output("mytimer", "disabled"),
  #  Output('mytimer', 'max_intervals'),
    Input("timer_control", "value"),
    Input("mytimer", "remaining_duration"),
    State("mytimer", "n_intervals"),
)
def update_display(timer_control, remaining_time, n):
    pause = True if timer_control == "Pause" else False

    badge_text = (
        f"Checking for updates in {str(dt.timedelta(seconds=remaining_time/1000))}"
        if remaining_time
        else ""
    )
    timer_end_text = "Results are in!" if remaining_time == 0 else ""
    interval_text = f"timer {n} intervals"



    return badge_text,timer_end_text, interval_text, pause


if __name__ == "__main__":
    app.run_server(debug=True)
