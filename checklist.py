import dash
from dash import dcc, html, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(id='checklist', children=[
        dcc.Checklist(
            id='my-checklist',
            options=[
                {'label': 'Item 1', 'value': 'item1'},
                {'label': 'Item 2', 'value': 'item2'},
                {'label': 'Item 3', 'value': 'item3'}
            ],
            value=[],
            inline=True
        ),
        html.Div(id='checklist-labels', children=[
            html.Label('Item 1', id='label-item1', style={'backgroundColor': 'lightblue', 'padding': '5px', 'margin': '5px'}),
            html.Label('Item 2', id='label-item2', style={'backgroundColor': 'lightblue', 'padding': '5px', 'margin': '5px'}),
            html.Label('Item 3', id='label-item3', style={'backgroundColor': 'lightblue', 'padding': '5px', 'margin': '5px'}),
        ])
    ])
])

@app.callback(
    Output('label-item1', 'style'),
    Output('label-item2', 'style'),
    Output('label-item3', 'style'),
    Input('my-checklist', 'value')
)
def update_label_styles(selected_items):
    styles = {
        'backgroundColor': 'lightblue',  # Couleur par défaut
        'padding': '5px',
        'margin': '5px'
    }
    
    # Met à jour les styles en fonction des éléments sélectionnés
    label_styles = {}
    for item in ['item1', 'item2', 'item3']:
        if item in selected_items:
            label_styles[f'label-{item}'] = {**styles, 'backgroundColor': '#005a9e', 'color': 'white'}  # Couleur sélectionnée
        else:
            label_styles[f'label-{item}'] = styles

    return label_styles['label-item1'], label_styles['label-item2'], label_styles['label-item3']

if __name__ == '__main__':
    app.run_server(debug=True)
