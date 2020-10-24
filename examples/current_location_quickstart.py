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
    Input("current_loc", "isodate_UTC"),
    Input("current_loc", "isodate_local"),
    Input("current_loc", "position"),
)
def display_output(date, isodate, isolocal, pos):
    print("local date string from component - nice format ready to use in UI:", date)
    print("iso format of local time", isolocal)
    print("iso format of UTC time. But it is not time zone aware:", isodate)

    print(" ")
    print("Demo of creating a datetime object from the date strings:")
    utc_date = dt.datetime.fromisoformat(isodate).replace(tzinfo=dt.timezone.utc)
    print("UTC datetime object - time zone aware:", utc_date)

    # convert to local time:
    local_date = utc_date.astimezone(tz=None)
    print("UTC datetime object converted to local datetime object:", local_date)
    print(" ")

    if pos:
        return html.P(
            f"As of {date} your location was: lat {pos['latitude']},lon {pos['longitude']}, accuracy {pos['accuracy']} meters",
        )
    else:
        return "No position data available"


if __name__ == "__main__":
    app.run_server(debug=True)
