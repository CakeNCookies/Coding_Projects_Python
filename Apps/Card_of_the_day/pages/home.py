import dash
from dash import html, dcc, html, Input, Output, ctx, callback
from datetime import date, datetime
import os
import pandas as pd

dash.register_page(__name__, path='/')

last_clicked = {
    '00MA': -1, '01MA': -1, '02MA': -1, '03MA': -1, '04MA': -1, '05MA': -1, '06MA': -1, '07MA': -1, '08MA': -1, '09MA': -1, '10MA': -1, '11MA': -1, '12MA': -1, '13MA': -1, '14MA': -1, '15MA': -1, '16MA': -1, '17MA': -1, '18MA': -1, '19MA': -1, '20MA': -1, '21MA': -1,
    '01CU': -1, '02CU': -1, '03CU': -1, '04CU': -1, '05CU': -1, '06CU': -1, '07CU': -1, '08CU': -1, '09CU': -1, '10CU': -1, '11CU': -1, '12CU': -1, '13CU': -1, '14CU': -1,
    '01PE': -1, '02PE': -1, '03PE': -1, '04PE': -1, '05PE': -1, '06PE': -1, '07PE': -1, '08PE': -1, '09PE': -1, '10PE': -1, '11PE': -1, '12PE': -1, '13PE': -1, '14PE': -1,
    '01WA': -1, '02WA': -1, '03WA': -1, '04WA': -1, '05WA': -1, '06WA': -1, '07WA': -1, '08WA': -1, '09WA': -1, '10WA': -1, '11WA': -1, '12WA': -1, '13WA': -1, '14WA': -1,
    '01SW': -1, '02SW': -1, '03SW': -1, '04SW': -1, '05SW': -1, '06SW': -1, '07SW': -1, '08SW': -1, '09SW': -1, '10SW': -1, '11SW': -1, '12SW': -1, '13SW': -1, '14SW': -1
}

if os.path.exists('data.csv'):
    pd.read_csv("data.csv")
else:
    df = pd.DataFrame({'date': [], 'card':[]})
    df.to_csv("data.csv", index=False)    

def updatecsv(data, date, card):
    # day = datetime.today().strftime('%Y-%m-%d')
    day = date.strftime('%Y-%m-%d')
    if day not in data.date.unique():
        data = pd.concat([data, pd.DataFrame({'date':[day], 'card':[card]})], axis=0)
    else:
        data.loc[data['date'] == day, 'card'] = card
        print(card)
    data.to_csv("data.csv", index=False)
    return data.sort_values(by=['date'])













layout = html.Div([
    html.H1('Which Card Did You Get Today?'),

    html.Div([
    html.H3('Select a day'),
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=date(1995, 1, 1),
        max_date_allowed=date(2100, 12, 31),
        initial_visible_month=datetime.today(),
        date=datetime.today()
    ),
    html.Div(id='output-container-date-picker-single'),
    ], style={'max-width': '500'}),


    html.Br(),


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



@callback(
    Output('output-container-date-picker-single', 'children'),
    Input('my-date-picker-single', 'date'))
def update_output(date_value):
    string_prefix = 'You have selected: '
    if date_value is not None:
        date_object = date_value
        date_string = datetime.fromisoformat(date_object).strftime('%Y-%m-%d')
        return string_prefix + date_string



@callback(
        Output('tabs-content-example-graph', 'children'),
        Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-ma':
        return html.Div([
            html.Img(id="00MA", src="assets/00MA.png", n_clicks_timestamp=0, style={'cursor': 'pointer'}),
            html.Img(id="01MA", src="assets/01MA.png", n_clicks_timestamp=0, style={'cursor': 'pointer'}),
            html.Img(id="02MA", src="assets/02MA.png", n_clicks_timestamp=0, style={'cursor': 'pointer'}),
        ], style={'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'wrap'})
    elif tab == 'tab-cu':
        return html.Div([
            html.Img(id="01CU", src="assets/01CU.png", n_clicks_timestamp=0, style={'cursor': 'pointer'}),
        ], style={'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'wrap'})
    elif tab == 'tab-pe':
        return html.Div([
            html.Img(id="01PE", src="assets/01PE.png", n_clicks_timestamp=0, style={'cursor': 'pointer'}),
        ], style={'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'wrap'})
    elif tab == 'tab-wa':
        return html.Div([
            html.Img(id="01WA", src="assets/01WA.png", n_clicks_timestamp=0, style={'cursor': 'pointer'}),
        ], style={'display': 'flex', 'flexDirection': 'row','flexWrap': 'wrap'})
    elif tab == 'tab-sw':
        return html.Div([
            html.Img(id="01SW", src="assets/01SW.png", n_clicks_timestamp=0, style={'cursor': 'pointer'}),
        ], style={'display': 'flex', 'flexDirection': 'row','flexWrap': 'wrap'})
    




    