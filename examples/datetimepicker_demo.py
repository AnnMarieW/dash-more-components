import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_bootstrap_components as dbc
import datetime as dt

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.H3("Examples from datetimepicker_demo.py"),
        html.Div(
            [
                "Default datetimepicker no initial time set and placeholders other than the default '--':",
                dmc.Datetimepicker(
                    id="example1",
                    yearPlaceholder='yyyy',
                    monthPlaceholder='mm',
                    dayPlaceholder='dd',
                    hourPlaceholder='hh',
                    minutePlaceholder='mm',
                    secondPlaceholder='ss',

                ),
                html.Div(id="output1"),
            ]
        ),
         html.Div(
             [
                 "Default datetimepicker with initial time set:",
                 dmc.Datetimepicker(
                     id="example2",
                 format = 'y-MM-dd HH:mm:ss',
              #   value ='2010-01-01T01:01',
                 value=str(dt.datetime.now()),
                # maxDetail='hour',
                ),
                 html.Div(id="output2"),
             ], className='mt-4'
         ),
        html.Div(
             [
                 "datetimepicker with max and min date set:",
                 dmc.Datetimepicker(
                     id="example3",
                 format = 'y-MM-dd HH:mm:ss',
                 maxDate=str(dt.date(2020, 12, 21)),
                 minDate=str(dt.date(2020, 10, 21)),

                 value=str(dt.datetime.now()),
                # maxDetail='hour',
                ),
                 html.Div(id="output3"),
             ], className='mt-4'
         ),
    ],
    className="m-5",
)


@app.callback(
    Output("output1", "children"),
    Output("output2", "children"),
    Output("output3", "children"),
    Input("example1", "value"),
    Input("example2", "value"),
    Input("example3", "value"),
)
def update_output(time1,time2, time3):
    msg_a = "Please select a date  and time"
    msg_b = "You have selected: "
    print(time1)
    print(type(time1))

    clock1 = msg_b + time1 if time1 else msg_a
    clock2 = msg_b + time2 if time2 else msg_a
    clock3 = msg_b + time3 if time3 else msg_a
    return clock1, clock2, clock3


if __name__ == "__main__":
    app.run_server(debug=True)
