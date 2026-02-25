import dash
from dash import html, dcc, html, Input, Output, ctx, callback

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Which Card Did You Get Today?'),
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
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label='Major Arcana', value='tab-1-example-graph'),
        dcc.Tab(label='Cups', value='tab-2-example-graph'),
        dcc.Tab(label='Pentacles', value='tab-3-example-graph'),
        dcc.Tab(label='Wands', value='tab-4-example-graph'),
        dcc.Tab(label='Swords', value='tab-5-example-graph'),
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
    if tab == 'tab-1-example-graph':
        return html.Div([
            html.Img(id="00MA", src="assets/00MA.png", n_clicks=0, style={'cursor': 'pointer'}),
            html.Img(id="01MA", src="assets/01MA.png", n_clicks=0, style={'cursor': 'pointer'}),
            # dcc.Graph(
            #     figure={
            #         'data': [{
            #             'x': [1, 2, 3],
            #             'y': [3, 1, 2],
            #             'type': 'bar'
            #         }]
            #     }
            # )
        ])
    elif tab == 'tab-2-example-graph':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs-dcc',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])