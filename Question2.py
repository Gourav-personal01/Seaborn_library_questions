# Que 2: Load the "fmri" dataset using the load_dataset function of seaborn. Plot a line plot using x =
# "timepoint" and y = "signal" for different events and regions.


#Solution
import seaborn as sns
fmri = sns.load_dataset('fmri')
fmri
lineplot = sns.lineplot(x = fmri.timepoint,y = fmri.signal, data = fmri)
print(lineplot)