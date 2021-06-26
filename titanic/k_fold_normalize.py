import sys
sys.path.append('src')
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import math
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator

import time
start_time = time.time()

import pandas as pd 

def all_ks_accuracies(df):
  accuracies = []
  matrix = np.array(df)

  independent_mat = matrix[:, 1:]
  dependent_mat = matrix[:,0]

  #looping through all values of k
  for k_value in k_values:
    num_correct = 0
    #looping throught all the rows of the dataframe
    for row_num in range(len(df)):
      # get independent and dependent row
      independent_row = independent_mat[row_num,:]
      dependent_row = dependent_mat[row_num]


      indices = np.arange(len(independent_mat))
      independent_mat_copy = independent_mat[indices != row_num, :]
      dependent_mat_copy = dependent_mat[indices != row_num]

    
      #fit the new dataframe to KNearestNeighborsClassifier 
      knn = KNeighborsClassifier(n_neighbors= k_value)

      knn.fit(independent_mat_copy, dependent_mat_copy)

      #classify row
      knn_classify = knn.predict([independent_row])
      if knn_classify[0] == dependent_row:
        num_correct += 1


    accuracies.append(num_correct/len(df))
  return accuracies

k_values = [k*2 + 1 for k in range(50)]
#set up df 
original_df = pd.read_csv('processed_titanic_data.csv')

original_df = original_df[["Survived","Sex","Pclass","Fare","Age","SibSp"]][:100]

accuracies=all_ks_accuracies(df)


plt.plot(k_values,accuracies)
df = original_df.copy()
#normalize scale
for column in df:

  max_column = df[column].max()
  for row in range(len(df[column])):
    df[column][row] = df[column][row]/max_column


accuracies= all_ks_accuracies(df)


plt.plot(k_values,accuracies)
df = original_df.copy()

#normalize max min
for column in df:
  #find min and max
  max_column = df[column].max()
  min_column = df[column].min()

  for row in range(len(df[column])):
    df[column][row] = (df[column][row]-min_column)/(max_column-min_column)


accuracies=all_ks_accuracies(df)


plt.plot(k_values,accuracies)
df = original_df.copy()

#normalize z
for column in df:

  average = df[column].mean()
  standard_deviation = np.std(df[column])
  for row in range(len(df[column])):
    df[column][row] = (df[column][row]-average )/(standard_deviation)

accuracies= all_ks_accuracies(df)

plt.plot(k_values,accuracies)


plt.savefig('K values accuracies.png')

end_time = time.time()
print('time taken:', end_time - start_time)
