# Required Python Packages
import pandas as pd
import numpy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

import pdb

# File Paths
TRAIN_PATH = "we_data/train.csv"
VALIDATION_PATH = "we_data/validation.csv"

def main():

    # Load csv file
    train_dataset = pd.read_csv(TRAIN_PATH)
    validation_dataset = pd.read_csv(VALIDATION_PATH)
    train_dataset = train_dataset[['click','weekday','hour','region','city','adexchange','slotwidth','slotheight']].replace("null", numpy.NaN)
    validation_dataset = validation_dataset[['click','weekday','hour','region','city','adexchange','slotwidth','slotheight']].replace("null", numpy.NaN)
    train_dataset.dropna(inplace=True) # remove rows with NaN values
    validation_dataset.dropna(inplace=True)


    #1,2,7,8,9,14,15
	#train_x, test_x, train_y, test_y = split_dataset(train_dataset, 0.7, HEADERS[1:-1], HEADERS[-1])
    X = train_dataset.iloc[:, 1:7].values #colums weekday, hour, region etc... as above ^ #iloc[rows, coloumns], ':' by itself means 'all'
    Y = train_dataset.iloc[:, 0].values #0 is click coloumn, the coloumn we want to predict

    X_test = validation_dataset.iloc[:, 1:7].values # colums weekday, hour, region etc... as above ^
    Y_test = validation_dataset.iloc[:, 0].values #0 is click coloumn

	#n_estimators the higher the better I guess, but i get impatient at n = 10, n = 100 never finishes
    rf = RandomForestRegressor(n_estimators=10, oob_score=False, random_state=0)
    rf.fit(X,Y)
    predicted_train = rf.predict(X)
    predicted_test = rf.predict(X_test)
    
    cost = 0.0
    numClicked = 0
    numImpressions = 0
    budget = 6250000
	#was 270 then 170 then 160
    baseBid = 250
    avgCTR = 6.646376573167722E-4
    
    testOriginal = pd.read_csv("we_data/validation.csv")
    testclicks = testOriginal.iloc[:, 0].values
    testpayprice = testOriginal.iloc[:, 21].values

    for i in range(len(testclicks)):
		testclick = testclicks[i]
		clickProb = predicted_test[i] # using predicted_test throws index error
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


if __name__ == "__main__":
    main()