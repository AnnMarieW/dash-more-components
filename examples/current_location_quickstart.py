import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import datetime as dt

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button("Update Position", id="update_btn"),
        dmc.CurrentLocation(id="current_loc"),
        html.Div(id="text_position"),
    ]
)


@app.callback(Output("current_loc", "update_now"), Input("update_btn", "n_clicks"))
def update_now(click):
    return True if click and click > 0 else False


@app.callback(
    Output("text_position", "children"),
    Input("current_loc", "local_date"),
    Input("current_loc", "timestamp"),
    Input("current_loc", "position"),
)
def display_output(date, timestamp, pos):

    # example:  how to create datetime object from timestamp
    if timestamp:
        datetime_local = dt.datetime.fromtimestamp(timestamp)
        datetime_utc = dt.datetime.utcfromtimestamp(timestamp)
        print('local:', datetime_local, 'utc: ', datetime_utc)

    if pos:
        return html.P(
            f"As of {date} your location was: lat {pos['latitude']},lon {pos['longitude']}, accuracy {pos['accuracy']} meters",
        )
    else:
        return "No position data available"


if __name__ == "__main__":
    app.run_server(debug=True)
