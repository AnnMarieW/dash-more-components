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


def make_map(lat, lon):
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
            zoom=8,
        ),
        uirevision="hold",
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
    Input("current_loc", "local_date"),
    Input("current_loc", "position"),
    Input("current_loc", "position_error"),
    prevent_initial_call=True,
)
def display_output(date, pos, err):
    print("pos", pos)
    print("error", err)

    if pos:
        position = html.Div(
            [
                html.H3(f"As of {date} your location was:"),
                html.P(
                    get_address(pos["latitude"], pos["longitude"]),
                    style={"marginLeft": 20},
                ),
                html.P(
                    f"lat {pos['latitude']},   lon {pos['longitude']}, accuracy {pos['accuracy']} meters",
                    style={"marginLeft": 20},
                ),
            ]
        )
        return position, make_map(pos["latitude"], pos["longitude"])
    else:
        return "No position data available", dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)
