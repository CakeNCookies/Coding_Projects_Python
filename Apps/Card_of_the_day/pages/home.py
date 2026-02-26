import dash
from dash import html, dcc, html, Input, Output, ctx, callback
from datetime import date, datetime

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Which Card Did You Get Today?'),
    html.H3('Select a day'),
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=date(1995, 1, 1),
        max_date_allowed=date(2100, 12, 31),
        initial_visible_month=datetime.today(),
        date=datetime.today()
    ),
    html.Div(id='output-container-date-picker-single'),

    html.Br(),



    # html.Div([
    #     dcc.Button('Major Arcana', id='btn-marc'),
    #     dcc.Button('Cups', id='btn-cups'),
    #     dcc.Button('Pentacles', id='btn-pent'),
    #     dcc.Button('Wands', id='btn-wand'),
    #     dcc.Button('Swords', id='btn-swor'),
    # ]),


    

    # dcc.Dropdown(
    #     id = 'dropdown-to-show_or_hide-element',
    #     options=[
    #         {'label': 'Show element', 'value': 'on'},
    #         {'label': 'Hide element', 'value': 'off'}
    #     ],
    #     value = 'on'
    # ),

    # html.Div([
    # html.Img(id="00MA", src="assets/00MA.png", n_clicks=0, style={'cursor': 'pointer'}),
    # html.Img(id="01MA", src="assets/01MA.png", n_clicks=0, style={'cursor': 'pointer'}),
    # html.Div(id="output-text")
    # ], style= {'display': 'inline-block', 'float':'left'}),


    html.Div([
    # html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs-example-graph", value='tab-ma', children=[
        dcc.Tab(label='Major Arcana', value='tab-ma'),
        dcc.Tab(label='Cups', value='tab-cu'),
        dcc.Tab(label='Pentacles', value='tab-pe'),
        dcc.Tab(label='Wands', value='tab-wa'),
        dcc.Tab(label='Swords', value='tab-sw'),
    ]),
    html.Div(id='tabs-content-example-graph')
])
])






# @callback(
#     Output("output-text", "children"), 
#     Input("00MA", "n_clicks"))
# def display_click_count(n_clicks):
#     return f"Image clicked {n_clicks} times"


# @callback(
#    [Output(component_id='00MA', component_property='style'),
#    Output(component_id='01MA', component_property='style')],
#    [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')])

# def show_hide_element(visibility_state):
#     if visibility_state == 'on':
#         return [{'display': 'inline-block'}, {'display': 'inline-block'}]
#     if visibility_state == 'off':
#         return [{'display': 'none'}, {'display': 'none'}]
    



@callback(
        Output('tabs-content-example-graph', 'children'),
        Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-ma':
        return html.Div([
            html.Img(id="00MA", src="assets/00MA.png", n_clicks=0, style={'cursor': 'pointer'}),
            html.Img(id="01MA", src="assets/01MA.png", n_clicks=0, style={'cursor': 'pointer'}),
            html.Img(id="02MA", src="assets/02MA.png", n_clicks=0, style={'cursor': 'pointer'}),
        ], style={'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'wrap'})
    elif tab == 'tab-cu':
        return html.Div([
            html.Img(id="01CU", src="assets/01CU.png", n_clicks=0, style={'cursor': 'pointer'}),
        ], style={'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'wrap'})
    elif tab == 'tab-pe':
        return html.Div([
            html.Img(id="01PE", src="assets/01PE.png", n_clicks=0, style={'cursor': 'pointer'}),
        ], style={'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'wrap'})
    elif tab == 'tab-wa':
        return html.Div([
            html.Img(id="01WA", src="assets/01WA.png", n_clicks=0, style={'cursor': 'pointer'}),
        ], style={'display': 'flex', 'flexDirection': 'row','flexWrap': 'wrap'})
    elif tab == 'tab-sw':
        return html.Div([
            html.Img(id="01SW", src="assets/01SW.png", n_clicks=0, style={'cursor': 'pointer'}),
        ], style={'display': 'flex', 'flexDirection': 'row','flexWrap': 'wrap'})