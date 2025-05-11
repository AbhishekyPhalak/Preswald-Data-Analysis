import pandas as pd
import plotly.express as px
from preswald import connect, get_df, table, text, plotly

connect()
df = pd.read_csv('data/seattle-weather.csv')

filtered_df = df[df['temp_max'] > 10]

text("# Data Analysis App")
table(filtered_df, title="Filtered Data")

fig = px.scatter(df, x="date", y="temp_max", color="weather")
plotly(fig)
