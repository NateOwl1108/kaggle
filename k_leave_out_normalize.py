import sys
import numpy as np
from k_neighbors_classifier import KNearestNeighborsClassifier
sys.path.append('src')

import pandas as pd 
df = pd.read_csv('book.csv')

accuracies = []
k_values = [k*2 + 1 for k in range(50)]

#normalize scale
for column in df:

  max_column = df[column].max()
  for row in range(len(df[column])):
    df[column][row] = df[column][row]/max_column

#normalize max min
for column in df:

  max_column = df[column].max()
  min_column = df[column].min()
  for row in range(len(df[column])):
    df[column][row] = (df[column][row]-min_column)/(max_column-min_column)

#normalize z
for column in df:

  average = df[column].mean()
  standard_deviation = np.std(df[column])
  for row in range(len(df[column])):
    df[column][row] = (df[column][row]-average )/(standard_deviation)


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
