from dash import html
import dash
from app.utils.data import generate_dash_table_row, generate_dash_table_header_row
from os.path import basename, splitext

dash.register_page(__name__)
page_path = "/bootstrap-components"


def generate_basic_html_table():
    return html.Div(children=[
        html.H2(children=html.A("Basic Table", href=f"{page_path}#basic_table"), id="basic_table"),
        html.Div(html.Table(  # className of "table" needed in order to apply bootstrap styles.
            className="table bootstrap-component-table",
            children=[
                # Colgroup - Controls column widths, or widths of groups of columns
                html.Colgroup(children=[
                    html.Col(span="1", className="col-group-0"),
                    html.Col(span="2", className="col-group-1"),
                    html.Col(span="5", className="col-group-2")
                ]),
                # Header
                html.Thead(children=generate_dash_table_header_row(
                    "Organization",
                    "Product Abbreviation",
                    "Product Category",

                    "Price 1",
                    "Volume A",
                    "Volume B",
                    "Volume C",
                    "Volume D",
                    "Volume E",
                    "Volume F",
                    "Volume G"
                )),
                # Body
                html.Tbody(
                    children=[generate_dash_table_row(
                        "org",
                        "abbreviation",
                        "word",

                        "millions of dollars",
                        "tens",
                        "thousands",
                        "millions",
                        "millions",
                        "thousands",
                        "hundreds",
                        "thousands"
                    ) for i in range(15)]
                )
            ]
        ), className="table-container")
    ], id="basic-table")


def generate_sortable_html_table():
    return html.Div(children=[
        html.H2(children=html.A("Sortable Table", href=f"{page_path}#sortable_table"), id="sortable_table"),
        html.Div(html.Table(  # className of "table" needed in order to apply bootstrap styles.
            className="table sortable bootstrap-component-table",
            children=[
                # Header
                html.Thead(children=generate_dash_table_header_row(
                    "Organization",
                    "Product Abbreviation",
                    "Product Category",

                    "Unit Price",
                    "Inventory",
                    sortable=True
                )),
                # Body
                html.Tbody(
                    children=[generate_dash_table_row(
                        "org",
                        "abbreviation",
                        "word",

                        "thousands of dollars",
                        "thousands",
                    ) for i in range(20)]
                )
            ]
        ), className="table-container")
    ])


layout = html.Div(children=[
    html.Div(children=generate_basic_html_table()),
    html.Div(children=generate_sortable_html_table())
], id="bootstrap-components")
