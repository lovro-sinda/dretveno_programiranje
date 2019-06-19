import requests
from bs4 import BeautifulSoup    # PyPI name: beautifulsoup4
import pandas as pd
import csv
from pandas import DataFrame
from sklearn import linear_model
import statsmodels.api as sm
def extract_value_from(Value):
    out = Value.replace('€', '')
    if 'M' in out:
        out = float(out.replace('M', ''))*1000
    elif 'K' in Value:
        out = float(out.replace('K', ''))*1
    return float(out)
DATA_LOCATION = "../data/players.csv"
FIRST_ATTRIBUTE = "Club"
SECOND_ATTRIBUTE = "Overall"
teci = "Value"
datas = pd.read_csv(DATA_LOCATION)
data = datas[[FIRST_ATTRIBUTE, SECOND_ATTRIBUTE,teci]]
K = data.values
#data['Value'] = data['Value'].apply(lambda x: extract_value_from(x))
data['Value'].head()

X = datas[['Overall','Overall']] # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = datas['Overall']
 
# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)


