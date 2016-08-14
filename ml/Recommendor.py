import numpy as np
import random
from sklearn import neighbors, cross_validation


def JsonToArr(sample, hasClass = False):
    array = []
    for names in sample:
        y = []
        y.append(str(names))
        y.append(sample[str(names)]['distance'])
        y.append(sample[str(names)]['rating'])
        y.append(sample[str(names)]['price_range'])
        y = y + sample[str(names)]['cuisinesML']
        if hasClass:
            y.append(sample[str(names)]['userPreference'])
        array.append(y)
    return array

def recommend(userJsonList, predefinedList):
    predict_array = JsonToArr(userJsonList)
    #predict_array = userJsonList
    train_array = JsonToArr(predefinedList, True)
    #print len(predict_array), len(train_array[0])
    
    clf = neighbors.KNeighborsClassifier(n_neighbours = 5)
    temp = []
    temp2 = []
    temp3 = []
    random.shuffle(train_array)
    for arr in train_array:
        temp.append(arr[1:-1])
        temp2.append(arr[-1])
        temp3.append(arr[0])
    X = temp
    y = temp2
    #print y
    #print len(X[0])
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.1) 
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    confidence = []
    if not isinstance(predict_array[0], list):
        for i in range(0,1):
            predictVector = predict_array[1:]
            confidence.append((clf.predict_proba(predictVector),  predict_array[0]))
    else:
        for i in range(0,len(predict_array)):
            predictVector = predict_array[i][1:]
            confidence.append((clf.predict_proba(predictVector),  predict_array[i][0]))
            
    return sorted(confidence)[0][1]
    #return index #return that JSON object's index