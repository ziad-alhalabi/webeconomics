
import pandas as pd
import numpy as np

def getTrainTestData():
    # Importing the dataset

    usecols = ['click', 'city', 'region', 'slotwidth', 'slotheight', 'useragent', 'slotprice', 'usertag', 'weekday', 'advertiser', 'slotvisibility']
    dataset = pd.read_csv('train.csv', usecols=usecols)
    test = pd.read_csv("validation.csv", usecols=usecols)

    dataset['os'] = 'os_'+dataset['useragent'].str.split('_').str[0]
    dataset['browser'] = 'browser_'+dataset['useragent'].str.split('_').str[1]
    dataset = dataset.drop('useragent', axis=1)

    test['os'] = 'os_'+test['useragent'].str.split('_').str[0]
    test['browser'] = 'browser_'+test['useragent'].str.split('_').str[1]
    test = test.drop('useragent', axis=1)



    #Encode advertiser
 #   browserSeries = pd.Series(dataset['advertiser'])
 #   browser_encoded_domains = pd.get_dummies(browserSeries, 'advertiser')
 #   dataset = dataset.drop('advertiser', axis=1)
 #   dataset = dataset.join(browser_encoded_domains)

 #   browserSeries2 = pd.Series(test['advertiser'])
#    browser_encoded_domains2 = pd.get_dummies(browserSeries2, 'advertiser')
#    test = test.drop('advertiser', axis=1)
#    test = test.join(browser_encoded_domains2)

#    print("advertiser")
#    print(list(set(browser_encoded_domains) - set(browser_encoded_domains2)))


    #Encode slotvisibility
    s = pd.Series(dataset['slotvisibility'])
    encoded_domains = pd.get_dummies(s, 'slotvisibility')
    dataset = dataset.drop('slotvisibility', axis=1)
    dataset = dataset.join(encoded_domains)
   # dataset = dataset.drop('slotvisibility_Na', axis=1)

    s2 = pd.Series(test['slotvisibility'])
    encoded_domains2 = pd.get_dummies(s2, 'slotvisibility')
    test = test.drop('slotvisibility', axis=1)
    test = test.join(encoded_domains2)
   # test = test.drop('slotvisibility_Na', axis=1)

    #Encode usertag
    newDatasetColumns = dataset['usertag'].str.get_dummies(sep=',')
    dataset = dataset.drop('usertag', axis =1)
    dataset = dataset.join(newDatasetColumns)

    newTestColumns = test['usertag'].str.get_dummies(sep=',')
    test = test.drop('usertag', axis=1)
    test = test.join(newTestColumns)


    #Encode creative
  #  s = pd.Series(dataset['creative'])
 #   encoded_domains = pd.get_dummies(s, 'creative')
 #   dataset = dataset.drop('creative', axis=1)
 #   dataset = dataset.join(encoded_domains)
 #   dataset = dataset.drop('creative_7332', axis=1)
 #   dataset = dataset.drop('creative_7324', axis=1)


  #  s2 = pd.Series(test['creative'])
  #  encoded_domains2 = pd.get_dummies(s2, 'creative')
  #  test = test.drop('creative', axis=1)
  #  test = test.join(encoded_domains2)

    #Encode Slotformat
  #  s = pd.Series(dataset['slotformat'])
  #  encoded_domains = pd.get_dummies(s, 'slotformat')
  #  dataset = dataset.drop('slotformat', axis=1)
  #  dataset = dataset.join(encoded_domains)
  #  dataset = dataset.drop('slotformat_Na', axis=1)

  #  s2 = pd.Series(test['slotformat'])
  #  encoded_domains2 = pd.get_dummies(s2, 'slotformat')
  #  test = test.drop('slotformat', axis=1)
  #  test = test.join(encoded_domains2)
  #  test = test.drop('slotformat_Na', axis=1)

    #Encode Browser
    browserSeries = pd.Series(dataset['browser'])
    browser_encoded_domains = pd.get_dummies(browserSeries)
    dataset = dataset.drop('browser', axis=1)
    dataset = dataset.join(browser_encoded_domains)

    browserSeries2 = pd.Series(test['browser'])
    browser_encoded_domains2 = pd.get_dummies(browserSeries2)
    test = test.drop('browser', axis=1)
    test = test.join(browser_encoded_domains2)

    #Encode OS
    osSeries = pd.Series(dataset['os'])
    os_encoded_domains = pd.get_dummies(osSeries)
    dataset = dataset.drop('os', axis=1)
    dataset = dataset.join(os_encoded_domains)

    osSeries2 = pd.Series(test['os'])
    os_encoded_domains2 = pd.get_dummies(osSeries2)
    test = test.drop('os', axis=1)
    test = test.join(os_encoded_domains2)

    print()


    #cleaning up data, replacing NaN by 0
    #dataset = dataset.apply(pd.to_numeric, errors='coerce')
    #dataset = dataset.replace('NaN',0)
    #test = test.apply(pd.to_numeric, errors='coerce')
    #test = test.replace('NaN',0)



  #  print(len(dataset.columns))
    X_train = dataset.iloc[:, 1:len(dataset.columns)].values # colums 1, 2, 3,.. 6 are X
    y_train = dataset.iloc[:, 0].values #0 is index of what we want to predict...

    X_test = test.iloc[:, 1:len(test.columns)].values # colums 1, 2, 3,.. 6 are X
    y_test = test.iloc[:, 0].values #0 is index of what we want to predict...

    features = list(test.drop('click', axis=1))
    print("features=======")
    print(len(features))

    features2 = list(dataset)
    print("features2=======")
    print(len(features2))

    return X_train, y_train, X_test, y_test, features, dataset, test

#getTrainTestData()

def getTestOriginalData():
    testOriginal = pd.read_csv("validation.csv")
    return testOriginal

def getTestBididColumn():
    usecols = ['bidid']
    dataset = pd.read_csv('test.csv', usecols=usecols)
    dataset = dataset.iloc[:, 0].values  # 0 is index of what we want to predict...
    return dataset
