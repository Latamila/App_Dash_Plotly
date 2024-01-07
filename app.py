from dash import Dash, dcc, html,Input, Output
import pandas
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Scatter plot Interativo com Dataset de Fundos Imobiliários'),
    dcc.Graph(id="scatter-plot"),
    html.P("Filtro pelo Dividend Yeld: "),
    dcc.RangeSlider(
        id="range-slider",
        min=7, max=25, step=0.1,
        marks={0: '0', 2.5:'2.5'},
        value=[0.5, 2]
    ),
])

@app.callback(
    Output("scatter-plot","figure"),
    Input("range-slider", "value"))
def update_bar_chart(slider_range):
    df = pandas.read_csv('fundos.csv') #replace with your own dataset
    low, high = slider_range
    mask = (df['dy'] > low) & (df['dy'] < high)
    fig = px.scatter(
        df[mask], x='dy', y='ValoRemuneracao_3anos',
        color='gestao', size='preco',
        hover_data=['ticker']
    )
    return fig

app.run_server(debug=True)
