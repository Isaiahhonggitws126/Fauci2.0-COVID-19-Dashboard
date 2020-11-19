#from data import *
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('C:/Users/David/Documents/GitHub/Fauci2.0-COVID-19-Dashboard/data/us-states.csv')

import plotly.graph_objects as go


fig = go.Figure()
fig.add_trace(go.Bar(x=df['state'],
                y=df['cases'],
                name='Cases by State',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=df['state'],
                y=df['deaths'],
                name='Deaths by State',
                marker_color='rgb(26, 118, 255)'
                ))

fig.update_layout(
    title='Cases and Death Count Per State'
    ,xaxis_tickfont_size=14,
    yaxis=dict(
        title='State',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(

        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


app.layout = html.Div(children=[
    html.H1(children='Covid19 dashboard'),

    html.Div(children='''
        State By State Cases
    '''),
    html.Label('State Dropdown'),
    dcc.Dropdown(
    	id='dropdown-1',
        options=[
       		{'label': 'Alabama','value': 'Alabama'},
			{'label': 'Alaska','value': 'Alaska'},
			{'label': 'Arizona','value': 'Arizona'},
			{'label': 'Arkansas','value': 'Arkansas'},
			{'label': 'California','value': 'California'},
			{'label': 'Colorado','value': 'Colorado'},
			{'label': 'Connecticut','value': 'Connecticut'},
			{'label': 'Delaware','value': 'Delaware'},
			{'label': 'District of Columbia','value': 'District of Columbia'},
			{'label': 'Florida','value': 'Florida'},
			{'label': 'Georgia','value': 'Georgia'},
			{'label': 'Guam','value': 'Guam'},
			{'label': 'Hawaii','value': 'Hawaii'},
			{'label': 'Idaho','value': 'Idaho'},
			{'label': 'Illinois','value': 'Illinois'},
			{'label': 'Indiana','value': 'Indiana'},
			{'label': 'Iowa','value': 'Iowa'},
			{'label': 'Kansas','value': 'Kansas'},
			{'label': 'Kentucky','value': 'Kentucky'},
			{'label': 'Louisiana','value': 'Louisiana'},
			{'label': 'Maine','value': 'Maine'},
			{'label': 'Maryland','value': 'Maryland'},
			{'label': 'Massachusetts','value': 'Massachusetts'},
			{'label': 'Michigan','value': 'Michigan'},
			{'label': 'Minnesota','value': 'Minnesota'},
			{'label': 'Mississippi','value': 'Mississippi'},
			{'label': 'Missouri','value': 'Missouri'},
			{'label': 'Montana','value': 'Montana'},
			{'label': 'Nebraska','value': 'Nebraska'},
			{'label': 'Nevada','value': 'Nevada'},
			{'label': 'New Hampshire','value': 'New Hampshire'},
			{'label': 'New Jersey','value': 'New Jersey'},
			{'label': 'New Mexico','value': 'New Mexico'},
			{'label': 'New York','value': 'New York'},
			{'label': 'North Carolina','value': 'North Carolina'},
			{'label': 'North Dakota','value': 'North Dakota'},
			{'label': 'Northern Mariana Islands','value': 'Northern Mariana Islands'},
			{'label': 'Ohio','value': 'Ohio'},
			{'label': 'Oklahoma','value': 'Oklahoma'},
			{'label': 'Oregon','value': 'Oregon'},
			{'label': 'Pennsylvania','value': 'Pennsylvania'},
			{'label': 'Puerto Rico','value': 'Puerto Rico'},
			{'label': 'Rhode Island','value': 'Rhode Island'},
			{'label': 'South Carolina','value': 'South Carolina'},
			{'label': 'South Dakota','value': 'South Dakota'},
			{'label': 'Tennessee','value': 'Tennessee'},
			{'label': 'Texas','value': 'Texas'},
			{'label': 'Utah','value': 'Utah'},
			{'label': 'Vermont','value': 'Vermont'},
			{'label': 'Virginia','value': 'Virginia'},
			{'label': 'Virgin Islands','value': 'Virgin Islands'},
			{'label': 'Washington','value': 'Washington'},
			{'label': 'West Virginia','value': 'West Virginia'},
			{'label': 'Wisconsin','value': 'Wisconsin'},
			{'label': 'Wyoming','value': 'Wyoming'}


        ],
        value=['New York'],
        multi=True
    ),
    dcc.Graph(
        id='state-cases-bar-graph',
        figure=fig
    )
])

#callbacks

@app.callback(
    Output('state-cases-bar-graph', 'figure'),
    [Input('dropdown-1', 'value')])
def update_figure(selected_states):
	#print((selected_states))
	new_df = pd.DataFrame()
	for state in selected_states:
		to_append = pd.DataFrame(df[df.state == state])
		new_df = new_df.append(to_append)

	fig = go.Figure()
	fig.add_trace(go.Bar(x=new_df['state'],
                y=new_df['cases'],
                name='Cases by State',
                marker_color='rgb(55, 83, 109)'
                ))
	fig.add_trace(go.Bar(x=new_df['state'],
                y=new_df['deaths'],
                name='Deaths by State',
                marker_color='rgb(26, 118, 255)'
                ))

	fig.update_layout(
    title='Cases and Death Count Per State'
    ,xaxis_tickfont_size=14,
    yaxis=dict(
        title='State',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(

        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
	)


	#fig = px.bar(new_df, x="state", y="cases", color="state")
	fig.update_layout(transition_duration=500)
	return fig



if __name__ == '__main__':
    app.run_server(debug=True)
