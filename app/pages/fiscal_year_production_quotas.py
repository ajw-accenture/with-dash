from app.services.fiscal_year_quota_service import FiscalYearQuotaService
from dash import html, dcc
import dash
import plotly.express as px

dash.register_page(__name__)

quotasDf = FiscalYearQuotaService.getQuarterlyFiscalYearProductionQuotas()
quotasFigure = px.line(quotasDf, x="Quarters", y="Quotas", markers=True)

layout = html.Div(children=[
    html.H1(children="FY Production Quotas"),
    html.P(children="Quarterly production quotas."),
    dcc.Graph(id="fy-production-quotas-graph", className="dcc-line-graph", figure=quotasFigure, responsive=True)
], id=f"page-{__name__}")