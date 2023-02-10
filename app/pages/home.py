from dash import html, dcc
import dash

dash.register_page(__name__, path="/")


layout = html.Div(
    html.Ul([
        html.Li(html.A("Home", href="/")),
        html.Li(html.A("Fiscal Year Sales", href="/fiscal-year-sales"))
    ]), id=f"page-{__name__}"
)