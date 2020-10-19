import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from geopy.geocoders import Nominatim

app = dash.Dash(__name__, prevent_initial_callbacks=True)


def get_address(lat, lon):
    geolocator = Nominatim(user_agent="my_location")
    try:
        location = geolocator.reverse(",".join([str(lat), str(lon)]))
        return location.address
    except:
        return "address unavailable"


def make_map(lat, lon, zoom):
    fig = go.Figure(
        go.Scattermapbox(
            lat=[lat],
            lon=[lon],
            mode="markers",
            marker=go.scattermapbox.Marker(size=14),
            text=[get_address(lat, lon)],
        )
    )

    fig.update_layout(
        hovermode="closest",
        mapbox=dict(
            style="open-street-map",
            bearing=0,
            center=go.layout.mapbox.Center(lat=lat, lon=lon),
            pitch=0,
            zoom=zoom,
        ),
    )
    return fig


app.layout = html.Div(
    [
        html.Button("Update Position", id="update_btn"),
        dcc.Checklist(
            id="options_checklist",
            options=[
                {"label": "Watch Position", "value": "watch"},
                {"label": "Enable High Accuracy", "value": "high_accuracy"},
            ],
        ),
        html.Div("Enter map zoom", style={"margin-top": 10}),
        dcc.Input(
            id="zoom_input", placeholder=8, value=8, min=0, max=23, type="number"
        ),
        dmc.CurrentLocation(
            id="current_loc",
        ),
        html.Div(id="text_position"),
        html.Div(dcc.Graph(id="map")),
    ]
)


@app.callback(
    Output("current_loc", "watch_position"),
    Output("current_loc", "high_accuracy"),
    Input("options_checklist", "value"),
)
def update_options(checked):
    if checked:
        watch = True if "watch" in checked else False
        high_accuracy = True if "high_accuracy" in checked else False
        return watch, high_accuracy
    else:
        return False, False


@app.callback(
    Output("current_loc", "update_now"),
    Input("update_btn", "n_clicks"),
)
def update_now(click):
    return True if click and click > 0 else False


@app.callback(
    Output("text_position", "children"),
    Output("map", "figure"),
    Input("zoom_input", "value"),
    Input("current_loc", "date"),
    Input("current_loc", "latitude"),
    Input("current_loc", "longitude"),
    Input("current_loc", "accuracy"),
    Input("current_loc", "position"),
    prevent_initial_call=True
)
def display_output(zoom, date, lat, lon, acc, pos):
    print(pos)  # need to figure out why this is {}

    if lat:
        position = html.Div(
            [
                html.H3(f"As of {date} your location was:"),
                html.P(get_address(lat, lon), style={"marginLeft": 20}),
                html.P(
                    f"lat {lat},   lon {lon}, accuracy {acc} meters",
                    style={"marginLeft": 20},
                ),
            ]
        )
        return position, make_map(lat, lon, zoom)
    else:
        return "No position data available", dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
