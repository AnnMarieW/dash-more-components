import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

app = dash.Dash(__name__, prevent_initial_callbacks=True)


def make_map(lat, lon):
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
            zoom=8,
        ),
        uirevision="hold",
    )
    return fig


app.layout = html.Div(
    [
        html.Div("Enter the time between updates in milliseconds"),
        dcc.Input(id="interval_input", placeholder=1000, type="number"),
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
    Input("current_loc", "local_date"),
    Input("current_loc", "position"),
    prevent_initial_call=True,
)
def display_output(date, pos):

    if pos:
        position = html.Div(
            [
                html.H3(f"As of {date} your location was:"),
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
