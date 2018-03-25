# Importing the libraries
from sklearn.linear_model import LinearRegression
from DataProcessing import getTrainTestData
from EvaluateStrategy import evaluateStrategy


# Get the training and testing data
X, y, X_test, y_test = getTrainTestData()

# Initialize regressor
regressor = LinearRegression()
regressor.fit(X, y)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Evaluate the results
evaluateStrategy(y_pred)





