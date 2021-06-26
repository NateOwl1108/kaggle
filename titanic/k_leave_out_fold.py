import sys
sys.path.append('src')
from k_nearest_neighbors_classifier import KNearestNeighborsClassifier
import pandas as pd 
df = pd.read_csv('processed_titanic_data.csv')
df = df[
    "Survived",
    "Sex",
    "Pclass",
    "Fare",
    "Age",
    "SibSp"
]
accuracies = []
k_values = [1,3,5,10,15,20,30,40,50,75]
 
def all_ks_accuracies(df):

  #looping through all values of k
  for k_value in k_values:
    num_correct = 0
    #looping throught all the rows of the dataframe
    for row_num in range(len(df)):
      # Remove one row from the dataframe
      copy_df = df.copy()

      row = copy_df.iloc[row_num]
      for column in df:
        del df[column][row_num]
      
      #fit the new dataframe to KNearestNeighborsClassifier 
      knn = KNearestNeighborsClassifier(k = k_value)
      knn.fit(copy_df, dependent_variable = 'Cookie Type')

      #classify row
      knn_classify = knn.classify(row)
      if knn_classify == row['Cookie Type']:
        num_correct += 1
        print('correct', row_num)
      else:
        print('incorrect', row_num)
    accuracies.append(num_correct/len(df))
  return accuracies


import math
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator

accuracies= [0] + all_ks_accuracies(df)


plt.plot(k_values,accuracies, color = 'blue', linewidth = 1)
plt.savefig('K values accuracies.png')
#Why is the accuracy low when k is very low?
#because the data is overfit
#Why is the accuracy low when k is very high?
#Because the data is underfit.
