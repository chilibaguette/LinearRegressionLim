import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split

data = pd.read_csv("C:\\DATA\\wine+quality\\winequality-white.csv")

# in Step 5
x = data.iloc[:,:-1].values
y = data.iloc[:,2].values

print('The independent variable = ', x.shape)
print('The dependent variable =', y.shape)



# Step 6
#Split the dataset into  training and test_set
# x = data.drop(['quality (Y)'], axis=1).values
# y = data['quality (Y)'].values
#
# x_train,x_test,y_train,y_test=train_test_split(x, y, test_size=20, random_state=0)
#
#Get the dimension of the training set
# print('The independent variable = ', x.shape)
# print('The dependent variable =', y.shape)



# Step 5
#Define independent(x) and dependent(y) variables.
# x = data.drop(['quality (Y)'], axis=1).values
# y = data['quality (Y)'].values
#
# print('The independent variable = ', x.shape)
# print('The dependent variable =', y.shape)


# in Step 4
#Get the correlation (or the degree of association) between two quantitative values
# correlations = data.corr(method='pearson')
# print(correlations)

# Step 4
#Try this
# from pandas.plotting import scatter_matrix
# scatter_matrix(data)
#
# plt.grid()
# plt.show()

# Step 4
#Make a scatter plot between x1 and y
# import matplotlib.pyplot as plt
# import seaborn as sns
# data.plot.scatter(x='fixed acidity (X1)', y='quality (Y)')
# plt.grid()
# plt.show()

# Step 4
#Understand some basic information from the dataset
# print(data.describe())


# Step 3
# print(data.isnull().sum())
