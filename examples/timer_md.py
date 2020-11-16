# import dash
# import dash_more_components as dmc
# import dash_html_components as html
#
# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div(
#     [
#         html.Div("Updating in...", style={"display": "inline-block"}),
#         html.Div(
#             dmc.Timer(
#                 # Any output the Timer component generates will be displayed here
#                 mode="stopwatch",  # 'countdown  | 'stopwatch'
#                 duration=10000,
#                 timer_format={"display": True, "verbose": True},
#                 rerun=True,
#             ),
#             style={"display": "inline-block"},
#         ),
#     ],
# )
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
#
# """
# ===============================================================================
# task progress
# """
#
# import dash
# import dash_more_components as dmc
# import dash_html_components as html
#
# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div(
#     [
#         html.H3("Track task Progress:", style={"margin": 5}),
#         html.H3(
#             dmc.Timer(
#                 mode="stopwatch",
#                 duration=421000,
#                 repeat=True,
#                 messages={
#                     1000: "Task submitted! This will take around five minutes.",
#                     10000: "Task submitted! This will take around five minutes. It has been 10 seconds.",
#                     60000: "Task submitted! This will take around five minutes. It has been one minute.",
#                     120000: "Task submitted! This will take around five minutes. It has been two minutes.",
#                     180000: "Task submitted! This will take around five minutes. It has been three minutes.",
#                     240000: "Task submitted! This will take around five minutes. It has been four minutes.",
#                     300000: "Task submitted! It has been five minutes - it should be done momentarily!",
#                     330000: "Task submitted! This will take around five minutes. It has been five minutes and 30 seconds. It's taking a little longer than expected, hang tight!",
#                     360000: "Task submitted! This should have taken around five minutes. It has been six minutes. Something might've gone wrong. Reach out to eli@acme.corp.",
#                     420000: "Task submitted! This should have taken around five minutes. It is taking much longer than expected. Something might've gone wrong. Reach out to eli@acme.corp.",
#                 },
#             )
#         ),
#     ],
# )
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
#
"""
===============================================================================
Space Shuttle
"""

import dash
from dash.dependencies import Input, Output
import dash_more_components as dmc
import dash_html_components as html
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

shuttle = (
    "https://cdn.pixabay.com/photo/2012/11/28/10/33/rocket-launch-67641_960_720.jpg"
)

app.layout = html.Div(
    [
        dbc.Button("start", id="start", size="lg", color="danger", className="m-4"),
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
)

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

#
# #========================================================
#
# import dash
# from dash.exceptions import PreventUpdate
# import dash_more_components as dmc
# import dash_core_components as dcc
# from dash.dependencies import Input, Output, State
# import dash_html_components as html
# import dash_bootstrap_components as dbc
# import datetime as dt
#
# external_stylesheets = [dbc.themes.BOOTSTRAP]
#
# # external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
#
# def formatted(milliseconds):
#     return str(dt.timedelta(milliseconds=int(milliseconds)))
#
#
# """
# ===============================================================================
# Markdown
# """
#
# intro_text = dcc.Markdown(
#     """
# """
# )
#
#
# timer1_card = dbc.Card(
#     [
#         # dbc.CardHeader(html.H3("Updated clientside")),
#         dbc.CardBody(
#             [
#                 html.H5("1.  Countdown timer"),
#                 html.Div(
#                     [
#                         html.Div("Updating in...", style={"display": "inline-block"}),
#                         html.Div(
#                             dmc.Timer(
#                                 # Any output the Timer component generates will be displayed here
#                                 id="timer1",
#                                 mode="stopwatch",  # 'countdown  | 'stopwatch'
#                                 duration=10000,
#                                 timer_format={"display": True, "verbose": True},
#                                 messages={
#                                     0: "zero",
#                                     10000: "ten",
#                                     2000: "udate 2 sec",
#                                     8000: "update 8sec",
#                                 },
#                                 fire=[2000, 8000],
#                                 rerun=True,
#                             ),
#                             className="d-inline-block",
#                         ),
#                     ],
#                     className="m-4",
#                 ),
#                 html.Div(id="timer1_callback_output"),
#             ],
#         ),
#     ],
#     className="m-1",
# )
#
#
# """
# ===============================================================================
# Layout
# """
# app.layout = dbc.Container(
#     [
#         dbc.Row(
#             [
#                 dbc.Col(timer1_card),
#                 #  dbc.Col(dash_callback_card, width=4),
#                 # dbc.Col(clientside_card, width=4),
#                 html.Div("test1"),
#                 html.Div("test2"),
#             ]
#         ),
#         # dbc.Row(
#         #     [
#         #         dbc.Col(
#         #             [five_min_card, time_input_card],
#         #             width={"size": 6, "order": 1, "offset": 4},
#         #         )
#         #     ]
#         # ),
#         # dbc.Row(intro_card),
#     ],
#     className="m-4",
# )
#
#
# """
# ===============================================================================
# Callbacks
# """
#
#
# @app.callback(
#     Output("timer1_callback_output", "children"), Input("timer1", "at_interval"),
# )
# def timer1(at_interval):
#     print(at_interval)
#     if at_interval:
#         return f"job started at  {dt.datetime.now().strftime('%I:%M:%S %p')}"
#     else:
#         raise PreventUpdate
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
