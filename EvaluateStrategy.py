
from DataProcessing import getTestOriginalData
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def evaluateStrategy(y_pred):
    df = pd.DataFrame(columns=['bid', 'clicks', 'imps', 'spent', 'CTR', 'CPC', 'CPM'])
    lists = {'bid': [], 'clicks': [], 'imps': [], 'spent': [], 'ctr': [], 'cpc': [], 'cpm': []}

    budget = 6250000
    avgCTR = 0.000738
    maxClick = 0
    maxClickBaseBid = 0
    baseBids = []

    spent = 0
    p_budget = 6250000.0

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

            if bid > testPayPrice and (cost + testPayPrice <= budget):
                cost += testPayPrice

                numImpressions = numImpressions + 1
                numClicked = numClicked + testclick
                p_budget = p_budget - testPayPrice
                spent = spent + testPayPrice

            if cost >= budget:
                break

        spent = spent / 1000
        ctr = ((numClicked / numImpressions) * 100)
        cpm = ((spent / numImpressions) * 1000)
        cpc = (spent / numClicked)

        lists['bid'].append(baseBid)
        lists['clicks'].append(numClicked)
        lists['imps'].append(numImpressions)
        lists['spent'].append(spent)
        lists['ctr'].append(ctr)
        lists['cpc'].append(cpc)
        lists['cpm'].append(cpm)


        #print("basebid %f" % baseBid)
        #print("numImpressions %f" % numImpressions)
        #print("numClicks %f" % numClicked)
        #print("cost %f" % cost)
        #print("########################")

        if numClicked>maxClick:
            maxClick = numClicked
            maxClickBaseBid = baseBid

    df.bid = lists['bid']
    df.clicks = lists['clicks']
    df.imps = lists['imps']
    df.spent = lists['spent']
    df.CTR = lists['ctr']
    df.CPC = lists['cpc']
    df.CPM = lists['cpm']

    print(df.iloc[np.where(df.clicks == df.clicks.max())[0]])

    print("maxClick %f" % maxClick)
    print("maxClickBaseBid %f" % maxClickBaseBid)

    #Visualize the results
    plt.plot(lists['bid'], lists['clicks'])
    plt.xlabel('baseBids')
    plt.ylabel('Number of clicks')
    plt.show()


# params - predict_proba, dataset(training data), validation clicks
def visualise_auc(pCTR_train, dataset, y_valid):
    from sklearn import metrics
    pCTRtrain = pd.DataFrame(pCTR_train)

    pctrval_list = []

    bin_count = len(dataset) / 2 * np.bincount(dataset.click)
    opt_bin = bin_count[1] / bin_count[0]

    for p in pCTRtrain[1]:
        pctrval_list.append(p / (p + ((1 - p) / opt_bin)))

    pctr_val = pd.DataFrame(pctrval_list)
    f, t, th = metrics.roc_curve(y_valid, pctr_val)

    fig, axes = plt.subplots(1, figsize=(8, 5))
    auc = 'AUC=%.5f' % metrics.auc(f, t)
    axes.step(f, t, lw=2, label=auc)
    axes.legend(loc='lower right', fontsize='small')
    plt.show()