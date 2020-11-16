import dash
from dash.exceptions import PreventUpdate
import dash_more_components as dmc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_bootstrap_components as dbc
import datetime as dt

external_stylesheets = [dbc.themes.BOOTSTRAP]

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

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



timer_countdown_card = dbc.Card(
    [
       # dbc.CardHeader(html.H3("Updated clientside")),
        dbc.CardBody(
            [
                html.H3("Timer - Countdown mode"),

                "timer_format={'verbose':True}",
                html.Div(
                    [
                        html.Div("Updating in...", style={"display": "inline-block"}),
                        html.H5(dmc.Timer(
                            mode='countdown',
                            duration = 10000,
                            timer_format={"display": True, "verbose": True},
                            rerun=True,
                        ),className = "d-inline-block"),
                    ],
                 className="mx-3 mt-1"
                ),

                html.Div(
                    [
                        html.Div("Updating in...", style={"display": "inline-block"}),
                        html.H5(dmc.Timer(
                            mode='countdown',
                            duration = 100000000,
                            timer_format={"display": True, "verbose": True},
                            rerun=True,
                        ),className = "d-inline-block"),
                    ],
                 className="mx-3 mt-1 mb-4"
                ),

                "timer_format={'colonNotation':True}",
                html.Div(
                    [
                        html.Div("Updating in...", style={"display": "inline-block"}),
                        html.H5(dmc.Timer(

                            mode='countdown',
                            duration=10000000,
                            timer_format={"display": True, "colonNotation": True},
                            rerun=True,
                        ), className="d-inline-block"),
                    ],
                    className="mx-3 mt-1 mb-4"
                ),

                "timer_format={'display': True}  (default)",
                html.Div(
                    [
                        html.Div("Updating in...", style={"display": "inline-block"}),
                        html.H5(dmc.Timer(

                            mode='countdown',
                            duration=10000000,
                            timer_format={"display": True},
                            rerun=True,
                        ), className="d-inline-block"),
                    ],
                    className="mx-3 mt-1"
                ),
            ],
        ),
    ],
    className="m-1",
)


timer_stopwatch_card = dbc.Card(
    [
       # dbc.CardHeader(html.H3("Updated clientside")),
        dbc.CardBody(
            [
                html.H3("Timer - Stopwatch Mode"),

                "timer_format={'verbose':True}",
                html.Div(
                    [
                        html.Div("Updating in...", style={"display": "inline-block"}),
                        html.H5(dmc.Timer(
                            mode='stopwatch',
                            duration = 10000,
                            timer_format={"display": True, "verbose": True},
                            rerun=True,
                        ),className = "d-inline-block"),
                    ],
                 className="mx-3 mt-1"
                ),

                html.Div(
                    [
                        html.Div("Updating in...", style={"display": "inline-block"}),
                        html.H5(dmc.Timer(
                            mode='stopwatch',
                            duration = 100000000,
                            timer_format={"display": True, "verbose": True},
                            rerun=True,
                        ),className = "d-inline-block"),
                    ],
                 className="mx-3 mt-1 mb-4"
                ),

                "timer_format={'colonNotation':True}",
                html.Div(
                    [
                        html.Div("Updating in...", style={"display": "inline-block"}),
                        html.H5(dmc.Timer(
                            mode='stopwatch',
                            duration=10000000,
                            timer_format={"display": True, "colonNotation": True},
                            rerun=True,
                        ), className="d-inline-block"),
                    ],
                    className="mx-3 mt-1 mb-4"
                ),

                "timer_format={'display': True}  (default)",
                html.Div(
                    [
                        html.Div("Updating in...", style={"display": "inline-block"}),
                        html.H5(dmc.Timer(
                            # Any output the Timer component generates will be displayed here
                            mode='stopwatch',  # 'countdown  | 'stopwatch'
                            duration=10000000,
                            timer_format={"display": True},
                            rerun=True,
                        ), className="d-inline-block"),
                    ],
                    className="mx-3 mt-1"
                ),
            ],
        ),
    ],
    className="m-1",
)




"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(timer_countdown_card),
                dbc.Col(timer_stopwatch_card),
              #  dbc.Col(dash_callback_card, width=4),
               # dbc.Col(clientside_card, width=4),

            ]
        ),
        # dbc.Row(
        #     [
        #         dbc.Col(
        #             [five_min_card, time_input_card],
        #             width={"size": 6, "order": 1, "offset": 4},
        #         )
        #     ]
        # ),
        # dbc.Row(intro_card),
    ],
    className="m-4",
)


"""
===============================================================================
Callbacks
"""




if __name__ == "__main__":
    app.run_server(debug=True)
