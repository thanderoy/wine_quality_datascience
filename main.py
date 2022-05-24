# Import libraries for use in data analysis and visualization
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# Extract csv data onto a dataframe
df_red = pd.read_csv('.\\resources\\winequality-red.csv', sep=';')
df_white = pd.read_csv('.\\resources\\winequality-white.csv', sep=';')

print(df_red.head())
print(df_white.head())

data_sets = [df_red, df_white]

# Task 1
# A - Distribution of wine quality across all samples, separately for red and white

for data_set in data_sets:    
    q = data_set["quality"]
    q.plot.hist()
    plt.xlabel("Wine quality (1-10)")
    plt.show()

# B - Discretise the alcohol content variables (separately for whites and reds) into low, mid, high based on its distribution

for data_set in data_sets:
    ac = data_set["alcohol"]
    avg = np.mean(ac)
    stddev = np.std(ac)
    # print (stddev)
    # print (avg)

    def alcohol_cat_value(value):
        if value > (avg + stddev):
            return 'low'
        elif value < ((avg-stddev) and (avg + stddev)):
            return 'medium'
        elif value > (avg + stddev):
            return 'high'

    data_set["alcohol_cat"] = data_set["alcohol"].apply(alcohol_cat_value)
    data_set["alcohol_cat"] = pd.Categorical(data_set["alcohol_cat"], categories=['low', 'medium', 'high'])
    print('\nAlcohol Category')
    print(data_set["alcohol_cat"])


# C - Describe the distribution of wine quality as in (1.A), but separately for low-, mid-, and high-alcohol content

    alcohol_cat_quality_corr = data_set.groupby("alcohol_cat")[["alcohol", "quality"]].corr().unstack().iloc[:,1]
    print('\nAlcohol Category and Quality Correlation')
    print(alcohol_cat_quality_corr)
    sb.scatterplot(data=data_set, x="alcohol", y="quality")
    plt.show()

