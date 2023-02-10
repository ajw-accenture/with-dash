from app.services.fiscal_year_sales_service import FiscalYearSalesService
from dash import html, dcc
import dash
import plotly.express as px

dash.register_page(__name__)

salesDf = FiscalYearSalesService.getFiscalYearSales()
salesFigure = px.bar(salesDf, x="Month", y="Sales")

layout = html.Div(children=[
    html.H1(children="FY Sales"),
    html.P(children="12-month sales graph."),
    dcc.Graph(id="fy-sales-graph", className="dcc-bar-graph", figure=salesFigure)
], id=f"page-{__name__}")
