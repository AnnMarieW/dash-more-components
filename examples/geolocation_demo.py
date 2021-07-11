import dash_more_components as dmc
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_table
import plotly.graph_objects as go
from geopy.geocoders import Nominatim
import pandas as pd
import datetime as dt
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(
    __name__, prevent_initial_callbacks=True, external_stylesheets=external_stylesheets
)

df = pd.DataFrame(
    {
        "lat": 0,
        "lon": 0,
        "alt": 0,
        "accuracy": 0,
        "altAccuracy": 0,
        "heading": 0,
        "speed": 0,
    },
    index=[0],
)

"""
==============================================================================
Markdown
"""
markdown_card = dbc.Card(
    [
        dbc.CardHeader(
            "Notes on Geoocation component and App settings",
            className="font-weight-bold",
        ),
        dcc.Markdown(
            """

1. The __Update Position__ button does a one-time update to the position.

2. __Include Address__ is an option to make a call to geopy to get address.  Sometimes it's slow, so if Watch Position 
is selected, or timeout is very small,  it's better to not have it included.
 
3. __Watch Position__ will automatically update if the position has changed or more accurate data is available. 
 Some browsers (like Firefox) update every 5 seconds.  While using, timeout should not be set to less than 5000
  otherwise it may constantly be in a timeout condition.

4. __Enable High Accuracy__ will use GPS if available, and will also attempt to get the best data possible.  Note - this 
uses more power and resources .  Also, timeout should be set to a high number or a max age should be provided as GPS 
sometimes takes longer to update.

5. __Max Age__ will provide a cached location after specified number of milliseconds if no new position data is 
available before the timeout.   If set to zero, it will not use a cached data.

6. __Timeout__ is the number of milliseconds allowed for the position to update without generating an error message

7. __Recenter__ and zoom to button will recenter the map and set the zoom to specified level.  The map uses uirevision 
to hold the user settings for pan, zoom etc, so those won't change when the position data is updated.  Note that in 
order for this to update, a new zoom number must be entered, because if it's the same, Dash will not update the map 


8.  The __dates and times__ are when the position data was obtained.  The date reflects the
 current system time from the computer running the browser.  The accuracy is dependant on this being set correctly
 in the user's computer and browser. 

        """
        ),
    ]
)


"""
===============================================================================
Map and address
"""


def get_address(lat, lon, show_address):
    address = ""
    if show_address:
        geolocator = Nominatim(user_agent="my_location")
        try:
            location = geolocator.reverse(",".join([str(lat), str(lon)]))
            address = location.address
        except:
            address = "address unavailable"
    return address


def make_map(
    position, show_address, zoom=12,
):
    lat = position["lat"]
    lon = position["lon"]
    fig = go.Figure(
        go.Scattermapbox(
            lat=[lat],
            lon=[lon],
            mode="markers",
            marker=go.scattermapbox.Marker(size=14),
            text=[get_address(lat, lon, show_address)],
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
        uirevision=zoom,
    )
    return fig


"""
===============================================================================
Input card
"""
input_card = html.Div(
    dbc.Card(
        [
            dbc.CardHeader("Geolocation controls", className="font-weight-bold"),
            dbc.CardBody(
                [
                    dbc.Button(
                        "Update Position",
                        id="update_btn",
                        className="m-2",
                        color="secondary",
                    ),
                    dbc.Checklist(
                        id="options_checklist",
                        options=[
                            {"label": "Include Address", "value": "address"},
                            {"label": "Watch Position", "value": "watch"},
                            {"label": "Enable High Accuracy", "value": "high_accuracy"},
                            {"label": "Show errors as alert", "value": "alert"},
                        ],
                        className="mt-4",
                    ),
                    dbc.InputGroup(
                        [
                            dbc.InputGroupAddon("Max age", addon_type="prepend"),
                            dbc.Input(
                                id="max_age",
                                placeholder=f"milliseconds",
                                type="number",
                                debounce=True,
                                value=0,
                                min=0,
                            ),
                        ],
                        className="m-2",
                        size="sm",
                    ),
                    dbc.InputGroup(
                        [
                            dbc.InputGroupAddon("Timeout", addon_type="prepend"),
                            dbc.Input(
                                id="timeout_input",
                                type="number",
                                debounce=True,
                                value=10000,
                                min=0,
                            ),
                        ],
                        className="m-2",
                        size="sm",
                    ),
                    dbc.InputGroup(
                        [
                            dbc.InputGroupAddon(
                                dbc.Button("Recenter and zoom to:", id="center"),
                                addon_type="prepend",
                            ),
                            dcc.Input(
                                id="zoom",
                                type="number",
                                debounce=True,
                                value=8,
                                min=0,
                                max=22,
                                step=1,
                            ),
                        ],
                        className="m-2",
                        size="sm",
                    ),
                ],
                className="m-2",
            ),
        ],
    )
)


def make_position_card(pos, date, show_address):
    return html.Div(
        [
            html.H4(f"As of {date} your location:"),
            html.P(
                f"within {pos['accuracy']} meters of  lat,lon: ( {pos['lat']:.2f},  {pos['lon']:.2f})",
                style={"marginLeft": 20},
            ),
            html.P(
                get_address(pos["lat"], pos["lon"], show_address),
                style={"marginLeft": 20},
            ),
        ]
    )


"""
===============================================================================
Layout
"""
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(input_card, width=3),
                dbc.Col(
                    [html.Div(id="text_position"), html.Div(dcc.Graph(id="map")),],
                    width=9,
                ),
            ],
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(id="iso_date"),
                        html.Div(
                            dash_table.DataTable(
                                id="position_data",
                                columns=[{"name": i, "id": i} for i in df.columns],
                                data=df.to_dict("records"),
                            ),
                            className="mb-4",
                        ),
                        html.Div(id="error_data", className="m-4"),
                        html.Div(markdown_card, className="m-4"),
                    ],
                    width={"offset": 3},
                )
            ]
        ),
        dmc.Geolocation(id="geolocation",),
    ],
    className="m-4",
    style={"minWidth": 500},
    fluid=True,
)
"""
===============================================================================
Callbacks
"""


@app.callback(
    Output("geolocation", "watch_position"),
    Output("geolocation", "high_accuracy"),
    Output("geolocation", "maximum_age"),
    Output("geolocation", "timeout"),
    Output("geolocation", "show_alert"),
    Input("options_checklist", "value"),
    Input("max_age", "value"),
    Input("timeout_input", "value"),
)
def update_options(checked, max_age, timeout):

    if checked:
        watch = True if "watch" in checked else False
        high_accuracy = True if "high_accuracy" in checked else False
        alert = True if "alert" in checked else False
    else:
        watch, high_accuracy, alert = False, False, False
    return watch, high_accuracy, max_age, timeout, alert


@app.callback(
    Output("geolocation", "update_now"), Input("update_btn", "n_clicks"),
)
def update_now(click):
    return True if click and click > 0 else False


@app.callback(
    Output("text_position", "children"),
    Output("map", "figure"),
    Output("position_data", "data"),
    Output("iso_date", "children"),
    Output("error_data", "children"),
    Input("options_checklist", "value"),
    Input("center", "n_clicks"),
    Input("zoom", "value"),
    Input("geolocation", "local_date"),
    Input("geolocation", "timestamp"),
    Input("geolocation", "position"),
    Input("geolocation", "position_error"),
    prevent_initial_call=True,
)
def display_output(checklist, center, zoom, date, timestamp, pos, err):

    # update text message
    show_address = True if checklist and "address" in checklist else False
    position = (
        make_position_card(pos, date, show_address)
        if pos
        else "No position data available"
    )

    # update map

    map = make_map(pos, show_address, zoom) if pos else dash.no_update

    # update position data and error messages
    df = pd.DataFrame(pos, index=[0])
    data = df.to_dict("records")
    err_output = (f"Error {err['code']} : ( {err['message']})") if err else None

    # display iso dates
    timestamp = timestamp if timestamp else 0
    datetime_local = dt.datetime.fromtimestamp(int(timestamp / 1000))
    datetime_utc = dt.datetime.utcfromtimestamp(int(timestamp / 1000))
    iso_date = f"UTC datetime: {datetime_utc}      Local datetime: {datetime_local}"

    return position, map, data, iso_date, err_output


if __name__ == "__main__":
    app.run_server(debug=True)
