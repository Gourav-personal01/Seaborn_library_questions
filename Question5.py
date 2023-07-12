# Que 5: Use the "iris" dataset from seaborn to plot a pair plot. Use the hue parameter for the "species" column
# of the iris dataset.

import seaborn as sns

iris = sns.load_dataset('iris')

pairplot = sns.pairplot(data = iris, hue = 'species')
print(pairplot)