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


"""
===============================================================================
Quickstart app for the docs
"""

"""
Copy to Clipboard component demo
"""

import dash
import dash_more_components as dmc
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container(
    dbc.Row(
        dbc.Col(
            [
                html.H3("Copy To Clipboard Demo"),
                dcc.Input(id="input_id", value=""),
                html.Div(
                    dmc.Clipboard(target_id="input_id"),
                    className="d-inline-block text-white  p-1  bg-secondary",
                    title="copy",
                ),
            ],className='m-4'
        ),
    ),fluid=True
)


if __name__ == "__main__":
    app.run_server(debug=True)
