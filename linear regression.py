#imports
import numpy
from numpy import arange
from matplotlib import pyplot
import seaborn as sns
import pandas as pd
from pandas import read_csv
from pandas import set_option
from pandas.tools.plotting import scatter_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import mean_squared_error


filename = "housing.csv"
names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']

df = read_csv(filename,delim_whitespace = True, names = names)
# Explore the data
print(df.dtypes)


print(df.head(100))

set_option('precision', 1)
print(df.describe())

set_option('precision',2)
print(df.corr())


print(df.hist(bins = 10, figsize=(9,7), grid = True))


prices= df['MEDV']

print("\nPrices: " ,prices[:506])

crime = df['CRIM']
df2 = df.drop['MDEV']
df3 = df.drop['CRIM']
corr1 = df2.corr()
corr2 = df3.corr()
import matplotlib.pyplot as plt
plt.figure(figsize =(10,10))
sns.heatmapp(corr, vmax = 8, square = True)
plt.title('correlationbetween features')
