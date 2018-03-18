# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('train.csv') #train
testOriginal = pd.read_csv("validation.csv")


columnsToDrop = [
					'bidid',
					'userid',
					'IP',
                    'domain',
					'url',
                    'city',
                    'hour',
                    'useragent',
                    'adexchange',
					'urlid',
					'slotid',
					'slotvisibility',
					'slotformat',
					'slotprice',
					'creative',
					'bidprice',
					'payprice',
					'keypage',
					'usertag'
				]


dataset = dataset.drop(columnsToDrop, axis=1)
test = testOriginal.drop(columnsToDrop, axis=1)

#cleaning up data, replacing NaN by 0
#dataset = dataset.apply(pd.to_numeric, errors='coerce')
#dataset = dataset.replace('NaN',0)
#test = test.apply(pd.to_numeric, errors='coerce')
#test = test.replace('NaN',0)

#dataset['adexchange'] = dataset['adexchange'].replace(np.nan, 0)
#test['adexchange'] = test['adexchange'].replace(np.nan, 0)

X = dataset.iloc[:, 1:6].values # colums 1, 2, 3,.. 5 are X
y = dataset.iloc[:, 0].values #0 is index of what we want to predict...

X_test = test.iloc[:, 1:6].values # colums 1, 2, 3,.. 5 are X
y_test = test.iloc[:, 0].values #0 is index of what we want to predict...

# Encoding categorical data
# 2 is the index of the column that we want to encode
#in this case, it is the useragent: chrome, firefox, etc
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
#labelencoder = LabelEncoder()
#columnToEncodeIndex = 1
#X[:, columnToEncodeIndex] = labelencoder.fit_transform(X[:, columnToEncodeIndex])
#onehotencoder = OneHotEncoder(categorical_features = [columnToEncodeIndex])
#X = onehotencoder.fit_transform(X).toarray()

#X_test[:, columnToEncodeIndex] = labelencoder.fit_transform(X_test[:, columnToEncodeIndex])
#onehotencoder = OneHotEncoder(categorical_features = [columnToEncodeIndex])
#X_test = onehotencoder.fit_transform(X_test).toarray()



# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)

# Predicting the Test set results
y_pred = regressor.predict(X_test)


cost = 0.0
numClicked = 0
numImpressions = 0
budget = 6250000

baseBid = 270
avgCTR = 6.646376573167722E-4


testclicks = testOriginal.iloc[:, 0].values
testpayprice = testOriginal.iloc[:, 21].values


for i in range(len(testclicks)):
    testclick = testclicks[i]
    clickProb = y_pred[i]
    testPayPrice = testpayprice[i]

    bid = (baseBid * clickProb) / avgCTR

    if(bid > testPayPrice and (cost + testPayPrice <= budget)):
        cost += testPayPrice
        numImpressions = numImpressions + 1
        numClicked = numClicked + testclick

    if(cost>= budget):
        break



print("numImpressions %f" % numImpressions)
print("numClicks %f" % numClicked)
print("cost %f" % cost)


