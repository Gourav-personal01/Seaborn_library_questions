# Que 6: Use the "flights" dataset from seaborn to plot a heatmap.

import seaborn as sns

flights = sns.load_dataset("flights")

flights_pivot = flights.pivot_table(values="passengers", index="month", columns="year")

heatmap=sns.heatmap(flights_pivot, annot=True, cmap="Blues")
print(heatmap)
