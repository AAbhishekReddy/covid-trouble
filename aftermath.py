import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

world = pd.read_csv(r"data\world.csv")
# world["Date"] = pd.to_datetime(world["Date"])

world = world.sort_values(by="Country")

# df = px.data.gapminder().query("year==2007")
# fig = px.choropleth(df, locations="iso_alpha",
#                     color="lifeExp", # lifeExp is a column of gapminder
#                     hover_name="country", # column to add to hover information
#                     color_continuous_scale=px.colors.sequential.Plasma)
# fig.show()

# iso = pd.read_excel("data\iso_codes.xls")


# iso.head()


# Plotting the bar plot.
india = world[world["Country"] == "India"]

india = india[india["New Cases"] > 30000]

plt.figure(figsize=(30, 20))
plt.bar(x=india["Date"], height=india["New Cases"])
plt.title("India: Number of cases by Date", fontsize=24, fontweight="bold")
plt.savefig("Indiacases.png")

plt.figure(figsize=(30, 20))
plt.plot(india["Date"], india["New Cases"], linewidth = 16)
plt.title("India: Number of cases by Date", fontsize=30, fontweight="bold")
plt.savefig("Indiacases_line.png")


usa_new = world[world["Country"] == "USA"]