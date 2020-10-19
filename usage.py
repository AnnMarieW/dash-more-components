import dash_more_components
import dash
from dash.dependencies import Input, Output
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_more_components.DashMoreComponents(
        id='input',
        value='my-value',
        label='my-label'
    ),
    html.Div(id='output')
])


@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
