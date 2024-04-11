import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H6("Altere o valor abaixo para ver o callback em ação!"),
    html.Div("Entrada:",
             dcc.Input(id="my-input", value="Valor inicial", type="text")),
    html.Br(),
    html.Div(id='my-output'),
])

@app.callback(
        [Output(component_id="my_output", component_property="children")], 
        [Input(component_id="my_input", component_property="value")],
)
def update_output_div(value):
    return "Saída: {}".format(value)

if __name__ == '__main__':
    app.run_server(debug=True)