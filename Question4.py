# Que 4: Use the "diamonds" dataset from seaborn to plot a histogram for the 'price' column. Use the hue
# parameter for the 'cut' column of the diamonds dataset.

# Solution --- 

import seaborn as sns

diamonds = sns.load_dataset("diamonds")

histplot = sns.histplot(data=diamonds, x="price", hue="cut")
print(histplot)

