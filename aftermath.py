import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()
plt.rcParams.update({'font.size': 22})

print("\tCreating Plots")

world = pd.read_csv(r"E:\Code dump\covid\covid-trouble\data\world.csv")

# Plotting the bar plot.
india = world[world["Country"] == "India"]

india = india[india["New Cases"] > 35000]

# Bar plot
plt.figure(figsize=(30, 20))
plt.bar(x=india["Date"], height=india["New Cases"])
plt.title("India: Number of cases by Date", fontsize=24, fontweight="bold")
plt.savefig("E:\Code dump\covid\covid-trouble\Indiacases.png")


# Line plot
plt.figure(figsize=(30, 20))
plt.plot(india["Date"], india["New Cases"], linewidth = 16, label = "New Cases")
plt.plot(india["Date"], india["New Recovered"], linewidth = 16, label = "New Recoveries", linestyle = 'dashed')
plt.title("India: Number of cases by Date", fontsize=30, fontweight="bold")
plt.xlabel("Dates", fontsize = 25)
plt.ylabel("Number of cases or recoveries", fontsize = 25)
plt.legend(fontsize = 25)
plt.savefig("E:\Code dump\covid\covid-trouble\Indiacases_line.png")


usa = world[world["Country"] == "USA"]
brazil = world[world["Country"] == "Brazil"]
russia = world[world["Country"] == "Russia"]
sa = world[world["Country"] == "South Africa"]

new_cases = [usa.iloc[usa.shape[0] - 1, :]["New Cases"],
                brazil.iloc[brazil.shape[0] - 1, :]["New Cases"],
                india.iloc[india.shape[0] - 1, :]["New Cases"],
                russia.iloc[russia.shape[0] - 1, :]["New Cases"],
                sa.iloc[sa.shape[0] - 1, :]["New Cases"]]

recovered_cases = [usa.iloc[usa.shape[0] - 1, :]["New Recovered"],
                brazil.iloc[brazil.shape[0] - 1, :]["New Recovered"],
                india.iloc[india.shape[0] - 1, :]["New Recovered"],
                russia.iloc[russia.shape[0] - 1, :]["New Recovered"],
                sa.iloc[sa.shape[0] - 1, :]["New Recovered"]]

position = [1.0, 2.0, 3.0, 4.0, 5.0]
position_recovered = [1.25, 2.25, 3.25, 4.25, 5.25]
position_country = [1.125, 2.125, 3.125, 4.125, 5.125]
plt.figure(figsize=(30, 20))
plt.bar(position, new_cases, width = 0.25, label = "New Cases")
plt.bar(position_recovered, recovered_cases, width = 0.25, label = "New Recovered Cases")
plt.xticks(position_country, ["USA", "Brazil", "India", "Russia", "South Africa"])
plt.xlabel("Country", fontsize = 25)
plt.ylabel("Number of cases", fontsize = 25)
plt.title("Comparision Between the Top Five Countries", fontsize = 25)
plt.legend(fontsize = 25)
plt.savefig("E:\Code dump\covid\covid-trouble\Top_five.png")

print("\tPlots created")