import pandas as pd

world = pd.read_csv("data\world.csv")

world = world.sort_values(by = "Country")

