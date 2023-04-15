# 1 way hypothsesis testing 
import seaborn as sns
from scipy import stats

# Load iris dataset and extract petal widths for setosa and versicolor species
iris = sns.load_dataset("iris")
setosa_petal_width = iris.loc[iris.species=='setosa', 'petal_width']
versicolor_petal_width = iris.loc[iris.species=='versicolor', 'petal_width']

# Perform two-sample t-test assuming equal variances
t_stat, p_val = stats.ttest_ind(setosa_petal_width, versicolor_petal_width, equal_var=True)

# Print results
print("t-statistic:", t_stat)
print("p-value:", p_val)
if p_val < 0.05:
    print("Reject null hypothesis: the mean petal width of setosa and versicolor species are significantly different.")
else:
    print("Fail to reject null hypothesis: there is insufficient evidence to conclude that the mean petal width of setosa and versicolor species are significantly different.")