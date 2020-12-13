import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc
import datetime as dt

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

time_input_card = html.Div(
    dbc.Card(
        [
            html.H4("Check for results at: "),
            dbc.Row(
                dbc.Col(
                    [
                        dmc.Timepicker(
                            id="time_picker", value="12:00:00", maxDetail="second",
                        ),
                        dbc.Button(
                            "Start countdown timer",
                            id="start_btn",
                            n_clicks=0,
                            color="primary",
                            size="sm",
                        ),
                    ],
                ),
            ),
        ],
        body=True,
        className="m-3",
    )
)

app.layout = dbc.Container(
    [
        time_input_card,
        html.Div("Results ready in:", className="m-2"),
        dbc.Badge(
            children=dmc.Timer(
                id="countdown",
                disabled=True,
                mode="countdown",
                timer_format="verbose",
                fire_times=[0],
            ),
            color="success",
            className="m-2",
            style={"minWidth": 250},
        ),
    ],
    fluid=True,
)


@app.callback(
    Output("countdown", "duration"),
    Output("countdown", "disabled"),
    Input("start_btn", "n_clicks"),
    State("time_picker", "value"),
)
def update_date_countdown( click, time_selected):
    ctx = dash.callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "start_btn":
        time_obj = dt.datetime.strptime(time_selected, "%H:%M:%S")
        time_now = dt.datetime.now()
        time_dif = time_obj - time_now
        starting_duration = time_dif.seconds * 1000
        return starting_duration, False
    else:
        return dash.no_update, dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
