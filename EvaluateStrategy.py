

from DataProcessing import getTestOriginalData
import matplotlib.pyplot as plt

def evaluateStrategy(y_pred):
    budget = 6250000
    avgCTR = 0.000738
    maxClick = 0
    maxClickBaseBid = 0
    baseBids = []
    clicks = []

    testOriginal = getTestOriginalData()
    testclicks = testOriginal.iloc[:, 0].values
    testpayprice = testOriginal.iloc[:, 21].values

    for baseBid in range(50, 150):
        cost = 0.0
        numClicked = 0
        numImpressions = 0

        for i in range(len(testclicks)):
            testclick = testclicks[i]
            clickProb = y_pred[i]
            testPayPrice = testpayprice[i]

            bid = (baseBid * clickProb) / avgCTR

            if (bid > testPayPrice and (cost + testPayPrice <= budget)):
                cost += testPayPrice
                numImpressions = numImpressions + 1
                numClicked = numClicked + testclick

            if (cost >= budget):
                break



        print("basebid %f" % baseBid)
        print("numImpressions %f" % numImpressions)
        print("numClicks %f" % numClicked)
        print("cost %f" % cost)
        print("########################")

        baseBids.append(baseBid)
        clicks.append(numClicked)

        if numClicked>maxClick:
            maxClick = numClicked
            maxClickBaseBid = baseBid

    print("maxClick %f" % maxClick)
    print("maxClickBaseBid %f" % maxClickBaseBid)

    #Visualize the results
    plt.plot(baseBids, clicks)
    plt.xlabel('baseBids')
    plt.ylabel('Number of clicks')
    plt.show()