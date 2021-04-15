import pandas as pd
import plotly.express as px  # (version 4.7.0)
import dash_table as dt
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate

# Data Exploration with Pandas
#---------------------------------------------------------------------------
df = pd.read_csv('vgsales.csv')
df = pd.read_csv('0408.csv')
print (df.columns)

# print (df.Genre.nunique())
# print (df.Genre.unique())
# print(sorted(df.Year.unique()))

# Data Visualisation with Plotly
#---------------------------------------------------------------------------
# fig_pie = px.pie(data_frame=df, names = 'Genre', values='Japan Sales')
# fig_pie.show()

# fig_pie = px.pie(data_frame=df, names = 'Genre', values='Japan Sales')
# fig_pie.show()

# fig_bar = px.bar(data_frame=df, x = 'Genre', y='Japan Sales')
# fig_bar.show()

# fig_hist = px.histogram(data_frame=df, x = 'Year', y='Japan Sales')
# fig_hist.show()

# Data Visualisation with Plotly
#---------------------------------------------------------------------------
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Geras Grafikas'),
    html.Div('Example Div', style={'color': 'blue', 'fontSize': 14}),
    dcc.Dropdown(id='Žanro pasirinkimai',
                 options=[{'label': x, 'value': x } for x in sorted(df['Rajonas'].unique())],
                 value='Antakalnis'
                 ),
    dcc.Graph(id='my-graph1', figure ={} ),
    html.P('Example P', className='my-class', id='my-p-element'),
    html.Div('Example Div', style={'color': 'blue', 'fontSize': 14}),
    dcc.Graph(id='my-graph', figure ={} )

])


#     Output('graph', 'figure'),
#     Output('data-table', 'data'),
#     Output('data-table', 'columns'),
#     Output('container', 'style')
# ]

@app.callback([
    Output(component_id='my-graph',component_property='figure'),
    Output(component_id='my-graph1',component_property='figure')
    ],
    [Input(component_id='Žanro pasirinkimai',component_property='value')])



# @app.callback([
#     Output('graph', 'figure'),
#     Output('data-table', 'data'),
#     Output('data-table', 'columns'),
#     Output('container', 'style')
# ], [Input('data-dropdown', 'value')])

def interactive_graphing(value_genre):
    if value_genre is None:
        raise PreventUpdate
    print (value_genre)
    dff = df[df['Rajonas'] == value_genre]
    data = px.bar(data_frame=dff, x = 'Plotas', y='Buto kaina')
    data1 = px.bar(data_frame=dff, x = 'Šildymas', y='Buto kaina')
    return data, data1

# def interactive_graphing(value_genre):
#     print (value_genre)
#     dff = df[df['Rajonas'] == value_genre]
#     figure = px.bar(data_frame=dff, x = 'Plotas', y='Buto kaina')
#
#     return figure



if __name__ == '__main__':
    app.run_server(debug=True)