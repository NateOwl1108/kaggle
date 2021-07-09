
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.cluster import KMeans


df = pd.read_csv('processed_titanic_data.csv')
df = df[["Sex", "Pclass", "Fare", "Age", "SibSp"]]

# Minmax normalization
for column in df:
  #find min and max
  max_column = df[column].max()
  min_column = df[column].min()

  for row in range(len(df[column])):
    df[column][row] = (df[column][row]-min_column)/(max_column-min_column)

# Generate the elbow plot
sse_values = []
for k in range(1, 25):
  kmeans = KMeans(n_clusters=k).fit( df)
  sse = kmeans.inertia_
  sse_values.append(sse)

k_values = [k for k in range(1, 25)]
  
plt.plot( k_values, sse_values)
  

plt.xlabel("k")
plt.ylabel("sum squared error")
plt.savefig('Titanic kelbow min max .png')