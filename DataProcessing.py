
import pandas as pd
import numpy as np

def getTrainTestData():
    # Importing the dataset
    usecols=['click', 'weekday', 'region', 'slotwidth', 'slotheight', 'advertiser', 'useragent', 'city', 'slotprice', 'slotformat']
    dataset = pd.read_csv('train.csv', usecols=usecols) #train
    test = pd.read_csv("validation.csv", usecols=usecols)

    dataset['os'] = 'os_'+dataset['useragent'].str.split('_').str[0]
    dataset['browser'] = 'browser_'+dataset['useragent'].str.split('_').str[1]
    dataset = dataset.drop('useragent', axis=1)

    test['os'] = 'os_'+test['useragent'].str.split('_').str[0]
    test['browser'] = 'browser_'+test['useragent'].str.split('_').str[1]
    test = test.drop('useragent', axis=1)

    # android_maxthon, android_ie, other_firefox
   # dataset['useragent'] = np.where(dataset['useragent'] == 'android_maxthon', 'other_other', dataset['useragent'])
   # dataset['useragent'] = np.where(dataset['useragent'] == 'android_ie', 'other_other', dataset['useragent'])
   # dataset['useragent'] = np.where(dataset['useragent'] == 'other_firefox', 'other_other', dataset['useragent'])
   # dataset['useragent'] = np.where(dataset['useragent'] == 'mac_maxthon', 'other_other', dataset['useragent'])
   # dataset['useragent'] = np.where(dataset['useragent'] == 'mac_sogou', 'other_other', dataset['useragent'])
   # dataset['useragent'] = np.where(dataset['useragent'] == 'linux_ie', 'other_other', dataset['useragent'])

   # test['useragent'] = np.where(test['useragent'] == 'android_maxthon', 'other_other', test['useragent'])
   # test['useragent'] = np.where(test['useragent'] == 'android_ie', 'other_other', test['useragent'])
   # test['useragent'] = np.where(test['useragent'] == 'other_firefox', 'other_other', test['useragent'])
   # test['useragent'] = np.where(test['useragent'] == 'mac_maxthon', 'other_other', test['useragent'])
   # test['useragent'] = np.where(test['useragent'] == 'mac_sogou', 'other_other', test['useragent'])
   # test['useragent'] = np.where(test['useragent'] == 'linux_ie', 'other_other', test['useragent'])

    dataset['slotformat'] = dataset['slotformat'].replace('Na', -1)
    test['slotformat'] = test['slotformat'].replace('Na', -1)

    #Encode Slotformat
    s = pd.Series(dataset['slotformat'])
    encoded_domains = pd.get_dummies(s)
    dataset = dataset.drop('slotformat', axis=1)
    dataset = dataset.join(encoded_domains)

    s2 = pd.Series(test['slotformat'])
    encoded_domains2 = pd.get_dummies(s2)
    test = test.drop('slotformat', axis=1)
    test = test.join(encoded_domains2)

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

#    dataset['domain'] = dataset['domain'].replace(np.nan, 'other')
#    test['domain'] = test['domain'].replace(np.nan, 'other')

    X_train = dataset.iloc[:, 1:27].values # colums 1, 2, 3,.. 6 are X
    y_train = dataset.iloc[:, 0].values #0 is index of what we want to predict...

    X_test = test.iloc[:, 1:27].values # colums 1, 2, 3,.. 6 are X
    y_test = test.iloc[:, 0].values #0 is index of what we want to predict...


    # Encoding categorical data
    # 1 is the index of the column that we want to encode
    #in this case, it is the useragent: chrome, firefox, etc
   # from sklearn.preprocessing import LabelEncoder, OneHotEncoder
   # labelencoder = LabelEncoder()
   # columnToEncodeIndex = 1
   # X_train[:, columnToEncodeIndex] = labelencoder.fit_transform(X_train[:, columnToEncodeIndex])
   # onehotencoder = OneHotEncoder(categorical_features = [columnToEncodeIndex])
  #  X_train = onehotencoder.fit_transform(X_train).toarray()

  #  X_test[:, columnToEncodeIndex] = labelencoder.fit_transform(X_test[:, columnToEncodeIndex])
    #onehotencoder = OneHotEncoder(categorical_features = [columnToEncodeIndex])
  #  X_test = onehotencoder.fit_transform(X_test).toarray()
    return X_train, y_train, X_test, y_test

#getTrainTestData()

def getTestOriginalData():
    testOriginal = pd.read_csv("validation.csv")
    return testOriginal

def getTestBididColumn():
    usecols = ['bidid']
    dataset = pd.read_csv('test.csv', usecols=usecols)
    dataset = dataset.iloc[:, 0].values  # 0 is index of what we want to predict...
    return dataset
