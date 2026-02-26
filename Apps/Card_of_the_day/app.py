import dash
from dash import Dash, html, dcc
import os
from threading import Timer
import webbrowser

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1('Card of The Day'),
    html.Div([
        html.Div(
            #dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

def open_browser():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:8050/')


if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True, port=8050)