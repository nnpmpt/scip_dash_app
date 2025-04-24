import dash
from dash import html

#### create app ####
app = dash.Dash(__name__)
app.title = 'Test'

#### define layout ####
app.layout = html.Div("Hello World")

#### run the app ####
if __name__ == '__main__':
    app.run_server(debug=True, port=80457)
