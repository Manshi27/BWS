import numpy as np
import cv2
import pandas as pd
from matplotlib import pyplot as plt
from xlwt import Workbook
xtest = np.empty((9, 784), dtype=np.int32)
print(type(xtest))
for j in range(0, 9):
    data = []
    img = cv2.imread("renamed\\" + str(j + 1) + ".jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28, 28))

    for i1 in range(0, 28):
        for j1 in range(0, 28):
            data.append(img[i1][j1])

    for i in range(0, len(data)):
        xtest[j][i] = data[i]

ytest = ['abhinav 20may', 'aman 4august', 'ankita 10october', 'kajol 13september', 'manish 1december', 'manshi 27october','mansi 3november', 'sanidhya 26may', 'tanya 25june']
# output array
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score,average_precision_score,recall_score,classification_report
from sklearn.neighbors import classification
model = DecisionTreeClassifier()
model.fit(xtest, ytest)
print(model.score(xtest, ytest))
# X_train,X_test,Y_Train,Y_Test=train_test_split(xtest,ytest,test_size=0.20)
# scaler=StandardScaler()
# scaler.fit(X_train)
# X_train=scaler.transform(X_train)
# X_test=scaler.transform(X_test)
# classifier=KNeighborsClassifier(n_neighbors=2)
# classifier.fit(X_test,Y_Train)
# Y_pred=classifier.predict(X_test)
classifier=KNeighborsClassifier(n_neighbors=1)
classifier.fit(xtest,ytest)
# avg_prec=average_precision_score(X_train,X_test)
print(classifier.score(xtest,ytest))
# print(avg_prec)
