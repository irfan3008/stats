import pandas as pd
import seaborn as sns
from scipy.stats import f_oneway


# Load iris.csv dataset from Github
iris = sns.load_dataset("iris")

# Split dataset by species and replace NaN values with 0
setosa = iris[iris["species"] == "setosa"]["petal_length"].fillna(0)
versicolor = iris[iris["species"] == "versicolor"]["petal_length"].fillna(0)
virginica = iris[iris["species"] == "virginica"]["petal_length"].fillna(0)

# Define null and alternative hypotheses
null_hypothesis = "The mean petal length is equal across all three species of iris (setosa, versicolor, and virginica)."
alt_hypothesis = "The mean petal length differs across at least one of the three species of iris."

# Perform one-way ANOVA test
f_stat, p_value = f_oneway(setosa, versicolor, virginica)

# Print results
print("Null hypothesis:", null_hypothesis)
print("Alternative hypothesis:", alt_hypothesis)
print("F-value:", f_stat)
print("P-value:", p_value)

# Define significance level
alpha = 0.05

# Determine whether to accept or reject null hypothesis
if p_value < alpha:
    print("We reject the null hypothesis.")
else:
    print("We accept the null hypothesis.")
    
# Visualize results using a heatmap
sns.heatmap(iris.corr(), annot=True, cmap="YlGnBu")