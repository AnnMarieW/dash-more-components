import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

app = dash.Dash(__name__, prevent_initial_callbacks=True)


def make_map(lat, lon, zoom):
    fig = go.Figure(
        go.Scattermapbox(
            lat=[lat],
            lon=[lon],
            mode="markers",
            marker=go.scattermapbox.Marker(size=14),
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
        html.Div("Enter the time between updates in milliseconds"),
        dcc.Input(id="interval_input", placeholder=1000, type="number"),
        html.Div("Enter map zoom", style={"margin-top": 10}),
        dcc.Input(
            id="zoom_input", placeholder=8, value=8, min=0, max=23, type="number"
        ),
        dcc.Interval(id="interval_component"),
        dmc.CurrentLocation(
            id="current_loc",
        ),
        html.Div(id="text_position"),
        html.Div(dcc.Graph(id="map")),
    ]
)


@app.callback(
    Output("current_loc", "update_now"),
    Input("interval_component", "n_intervals"),
)
def update_now(n):
    return True if n else False


@app.callback(
    Output("interval_component", "interval"),
    Input("interval_input", "value"),
)
def update_interval(time):
    return time if time else 1000


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

    if lat:
        position = html.Div(
            [
                html.H3(f"As of {date} your location was:"),
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
