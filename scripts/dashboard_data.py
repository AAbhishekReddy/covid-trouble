import pandas as pd

world = pd.read_csv('E:\Code dump\covid\covid-trouble\data\world.csv')

india = world[world['Country'] == 'India']

# Saving the recoveries and new cases vs Date
india_cases_vs_recoveries = india[['Date', 'New Cases', "New Recovered"]].copy()

india_cases_vs_recoveries = india_cases_vs_recoveries[india_cases_vs_recoveries['New Cases'] > 20000]
india_cases_vs_recoveries = india_cases_vs_recoveries[india_cases_vs_recoveries['New Recovered'] > 20000]

# Saving the data into a CSV
india_cases_vs_recoveries.to_csv('E:\Code dump\covid\covid-trouble\data\india_cases_vs_recoveries.csv')
