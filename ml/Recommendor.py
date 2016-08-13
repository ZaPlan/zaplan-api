import numpy as np
import random
from sklearn import neighbors, cross_validation


def recommend(userJsonList, predefinedList):
    predict_array = JsonToArr(userJsonList)
    train_array = JsonToArr(predefinedList)
    clf = neighbors.KNeighborsClassifier(n_neighbours = 3)
    temp = []
    temp2 = []
    temp3 = []
    random.shuffle(train_array)
    for arr in train_array:
        temp.append(arr[1:-1])
        temp2.append(arr[-1])
        temp3.append(arr[0])
    X = temp
    t = temp2
    X_Train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2) 
    clf.fit(X_train, y_train)

    confidence = []
    for i in len(predict_array):
        confidence.append((clf.predict_proba(predict_array[i]), i))
    index = sorted(confidence)[0][1]
    array_needed = temp3[index]
    
    for x in userJsonList['user']['restaurants']:
        if array_needed == x:
            return x #return that JSON object whose name is this
