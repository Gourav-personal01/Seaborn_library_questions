# Que 3: Load the "titanic" dataset using the load_dataset function of seaborn. Plot two box plots using x =
# 'pclass', y = 'age' and y = 'fare'.


import seaborn as sns
titanic = sns.load_dataset("titanic")
print(titanic)
pclass_adn_age_data = sns.boxplot(x = titanic.pclass, y = titanic.age)
print(pclass_adn_age_data)
pclass_and_fare_data = sns.boxplot(x = titanic.pclass, y = titanic.fare)
print(pclass_and_fare_data)