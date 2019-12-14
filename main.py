#s15752, s16096
#sieci neuronowe:
#1: Irysy
#2: Predykcja
#3: Obrazki

import os
import pandas as pd
import matplotlib.pyplot as plt

#Set working directory and load data
iris = pd.read_csv('iris.csv')#Create numeric classes for species (0,1,2) 
iris.loc[iris['Name']=='virginica','species']=0
iris.loc[iris['Name']=='versicolor','species']=1
iris.loc[iris['Name']=='setosa','species'] = 2
iris = iris[iris['species']!=2]#Create Input and Output columns
X = iris[['PetalLength', 'PetalWidth']].values.T
Y = iris[['species']].values.T
Y = Y.astype('uint8')
#Make a scatter plot
plt.scatter(X[0, :], X[1, :], c=Y[0,:], s=40, cmap=plt.cm.Spectral);
plt.title("IRIS DATA | Blue - Versicolor, Red - Virginica ")
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()