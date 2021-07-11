#
# """
# Copy to Clipboard component demo
# """
#
# import dash
# import dash_more_components as dmc
# import dash_core_components as dcc
# import dash_html_components as html
# import dash_bootstrap_components as dbc
# import pandas as pd
#
# external_stylesheets = [dbc.themes.BOOTSTRAP]
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")
#
# # get code to display in dcc.Markdown
# with open("clipboard_demo.py") as f:
#     code = f.read()
# code = f"```{code}```"
#
# markdown_row = dbc.Row(
#     dbc.Col(
#         [
#             html.H3(
#                 dmc.Clipboard(target_id="md"),
#                 className="float-right p-1 text-secondary border border-secondary",
#                 title="copy",
#             ),
#             dcc.Markdown(
#                 code, id="md", className="overflow-auto border", style={"height": 300},
#             ),
#         ],
#     ),
#     className="my-4",
# )
#
# input_row = dbc.Row(
#     dbc.Col(
#         [
#             dcc.Input(id="input_id", value=""),
#             html.Div(
#                 dmc.Clipboard(target_id="input_id"),
#                 className="d-inline-block text-white  p-1  bg-secondary ",
#                 title="copy",
#             ),
#         ],
#     ),
#     className="my-4",
# )
#
# html_table_row = dbc.Row(
#     dbc.Col(
#         [
#             html.H5(
#                 dmc.Clipboard(target_id="html_table"),
#                 className="d-inline-block p-1 text-info  border border-info",
#             ),
#             html.Span("Copy Table", className="text-info"),
#             html.Table(
#                 id="html_table",
#                 children=[
#                     html.Thead(html.Tr([html.Th(col) for col in df.columns])),
#                     html.Tbody(
#                         [
#                             html.Tr([html.Td(df.iloc[i][col]) for col in df.columns])
#                             for i in range(min(len(df), 10))
#                         ]
#                     ),
#                 ],
#             ),
#         ],
#     ),
#     className="my-4 border",
# )
#
# paste_area = dbc.Row(
#     dbc.Col(dbc.Textarea(className="overflow-auto border", style={"height": 300})),
#     className="m-4",
# )
#
#
# app.layout = dbc.Container(
#     [
#         html.H2("Copy To Clipboard Demo"),
#         input_row,
#         markdown_row,
#         html_table_row,
#         html.H2("Test Paste Area:"),
#         paste_area,
#     ],
#     className="m-4",
# )
#
#
# if __name__ == "__main__":
#     app.run_server(debug=True)
#

#
# """
# ===============================================================================
# Quickstart app for the docs
# """
#
# """
# Copy to Clipboard component demo
# """
#
# import dash
# import dash_more_components as dmc
# import dash_core_components as dcc
# import dash_html_components as html
#
# external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
#
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
# app.layout = html.Div(
#     [
#         html.H3("Copy To Clipboard Demo"),
#         html.Div(
#             [
#                 dcc.Input(id="input_id", value=""),
#                 dmc.Clipboard(
#                     target_id="input_id",
#                     title="copy",
#                     className='button',
#                     style={
#                         "padding-right": 2,
#                         "padding-left": 2,
#                         "fontSize": 20,
#                      },
#                 ),
#             ], style={"margin-bottom": 10}
#         ),
#         dcc.Textarea(id="textarea_id", value=""),
#         dmc.Clipboard(
#             target_id="textarea_id",
#             title="copy",
#             style={
#                 "display": "inline-block",
#                 "fontSize": 30,
#                 "padding-right": 5,
#                 "padding-left": 5,
#                 "border-radius": 4,
#                 "backgroundColor": "gainsboro",
#                 "vertical-align": "top",
#             },
#         ),
#     ]
# )
#
# if __name__ == "__main__":
#     app.run_server(debug=True)


"""
=========================================================
From PR  & add DataTable

"""

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import dash_more_components as dmc

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

app.layout = html.Div(
    [
        html.H3("Copy To Clipboard Demo"),
        html.Div(
            [
                dcc.Input(id="input_id", value=""),
                dmc.Clipboard(
                    target_id="input_id",
                    title="copy",
                    className="button",
                    style={"padding": "0px 2px", "fontSize": 20,},
                ),
            ],
        ),
        html.Div(
            [
                dcc.Textarea(id="textarea_id", value="Text to copy", style={'width':800}),
                dmc.Clipboard(
                    target_id="textarea_id",
                    title="copy",
                    style={
                        "display": "inline-block",
                        "fontSize": 30,
                        "borderRadius": 4,
                        "backgroundColor": "gainsboro",
                        "verticalAlign": "top",
                    },
                ),
            ],
            style={"margin": "20px 0px"},
        ),
        html.Div(
            [
                dmc.Clipboard(
                    target_id="html_table",
                    title="copy table",
                    style={"fontSize": 25, "color": "blue",},
                ),
                html.Table(
                    id="html_table",
                    children=[
                        html.Thead(html.Tr([html.Th(col) for col in df.columns])),
                        html.Tbody(
                            [
                                html.Tr(
                                    [html.Td(df.iloc[i][col]) for col in df.columns]
                                )
                                for i in range(min(len(df), 10))
                            ]
                        ),
                    ],
                ),
            ],
            style={
                "border": "1px solid #D1D1D1",
                "padding": 10,
                "display": "inline-block",
            },
        ),
        html.Div(
            [
                html.I(dmc.Clipboard(
                    target_id="output",
                    title="copy table",
                    style={"fontSize": 25, "color": "blue",},
                ), id='copy'),
                dash_table.DataTable(
                    id="table",
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict("records"),
                    cell_selectable=True,
                ),
                html.Div(id="output"),
            ]
        )
    ]
)


@app.callback(
    Output("output", "children"),
    Input("copy", "n_clicks"),
    State("table", "start_cell"),
    State("table", "end_cell"),
    State("table", "derived_virtual_data"),
)
def copy_to_clipboard(n, start, end, data):
    if start is None:
        return dash.no_update
    dff = pd.DataFrame(data)
    copy_cells = dff.loc[
        start["row"] : end["row"], start["column_id"] : end["column_id"]
    ]
    copy_cells.to_clipboard(excel=False, index=False)


if __name__ == "__main__":
    app.run_server(debug=True)

