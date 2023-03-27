import locale
from chance import chance
from dash import html

org_suffix = ["Inc.", "LLC", "Corp.", "Ltd.", "Systems", "", "", ""]

def __generate_dash_table_header_cell(text="", sortable=False):
    th_className = ""
    children = []

    if sortable:
        th_className = f"{th_className} with-sort-control"
        children.append(html.Div(children=[
            html.I(className="bi bi-filter")
        ], className="sort-control"))

    children.append(html.Div(text))
    return html.Th(children=children, className=th_className)

def generate_dash_table_header_row(*args, sortable=False):
    return html.Tr(children=[ __generate_dash_table_header_cell(text=header, sortable=sortable) for header in args ])

def generate_dash_table_row(*args):
    row = []
    for arg in args:
        cell = ""
        # Python 3.10 or higher required for this pattern matching
        match arg:
            case "org":
                first = str.title(chance.word())
                middle = chance.pickone(["", " " + str.title(chance.word())])
                last = chance.pickone(org_suffix)
                cell = f"{first}{middle} {last}"
            case "tens":
                cell = locale.format("%.2f", int(chance.string(pool="123456789", minimum=1, maximum=2)), grouping=True)
            case "hundreds":
                cell = locale.format("%.2f", int(chance.string(pool="123456789", minimum=3, maximum=3)), grouping=True)
            case "thousands":
                cell = locale.format("%.2f", int(chance.string(pool="123456789", minimum=4, maximum=6)), grouping=True)
            case "thousands of dollars":
                cell = locale.currency(int(chance.string(pool="123456789", minimum=4, maximum=6)), grouping=True)
            case "millions":
                cell = locale.format("%.2f", int(chance.string(pool="123456789", minimum=7, maximum=9)), grouping=True)
            case "millions of dollars":
                cell = locale.currency(int(chance.string(pool="123456789", minimum=7, maximum=9)), grouping=True)
            case "billions":
                cell = locale.format("%.2f", int(chance.string(pool="123456789", minimum=10, maximum=12)), grouping=True)
            case "full name":
                cell = chance.name()
            case "sentence":
                cell = chance.sentence()
            case "abbreviation":
                cell = chance.string(pool="ABCDEFGHIJKLMNOPQRSTUVWXYZ", minimum=2, maximum=4)
            case "word":
                cell = str.title(chance.word())
            case _:
                cell = chance.string(minimum=5, maximum=18)
        row.append(cell)
    return html.Tr(children=[html.Td(children=cell) for cell in row])