import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Button("Update Position", id="update_btn"),
        dmc.CurrentLocation(id="current_loc"),
        html.Div(id="text_position"),
    ]
)


@app.callback(Output("current_loc", "update_now"),Input("update_btn", "n_clicks"))
def update_now(click):
    return True if click and click > 0 else False


@app.callback(
    Output("text_position", "children"),
    Input("current_loc", "date"),
    Input("current_loc", "latitude"),
    Input("current_loc", "longitude"),
    Input("current_loc", "accuracy"),
)
def display_output(date, lat, lon, acc):
    if lat:
        return html.P(f"As of {date} your location was: lat {lat}, lon {lon}, with an accuracy of {acc} meters")
    else:
        return "No position data available"


if __name__ == "__main__":
    app.run_server(debug=True)
