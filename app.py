from dash import Dash, html
import dash
import dash_bootstrap_components as dbc
import locale

locale.setlocale(locale.LC_ALL, "en_US")

app = Dash(
    __name__,
    use_pages=True,
    pages_folder="app/pages",
    external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP]
    )


app.layout = html.Div(children=[
    html.Div(html.H1("A Colorful Dash Site", id="app-title"), id="app-title-container"),
    html.Div(dash.page_container, id="app-container")
], id="layout-container")

if __name__ == '__main__':
    app.run_server(debug=True)
