import pandas as pd
import plotly.express as px

world = pd.read_csv("data\world.csv")

world = world.sort_values(by = "Country")

df = px.data.gapminder().query("year==2007")
fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.show()

iso = pd.read_excel("data\iso_codes.xls")


iso.head()