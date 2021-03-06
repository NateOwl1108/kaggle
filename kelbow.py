
import matplotlib.pyplot as plt 
from k_clusters import KMeans


columns = ['Portion Eggs',
            'Portion Butter',
            'Portion Sugar',
            'Portion Flour']

data = [[0.14, 0.14, 0.28, 0.44],
        [0.22, 0.1, 0.45, 0.33],
        [0.1, 0.19, 0.25, 0.4],
        [0.02, 0.08, 0.43, 0.45],
        [0.16, 0.08, 0.35, 0.3],
        [0.14, 0.17, 0.31, 0.38],
        [0.05, 0.14, 0.35, 0.5],
        [0.1, 0.21, 0.28, 0.44],
        [0.04, 0.08, 0.35, 0.47],
        [0.11, 0.13, 0.28, 0.45],
        [0.0, 0.07, 0.34, 0.65],
        [0.2, 0.05, 0.4, 0.37],
        [0.12, 0.15, 0.33, 0.45],
        [0.25, 0.1, 0.3, 0.35],
        [0.0, 0.1, 0.4, 0.5],
        [0.15, 0.2, 0.3, 0.37],
        [0.0, 0.13, 0.4, 0.49],
        [0.22, 0.07, 0.4, 0.38],
        [0.2, 0.18, 0.3, 0.4]]


sse_values = []

for k in range(1, 6):
  initial_clusters = {}
  for cluster in range(1, k+1):
    initial_clusters[cluster] = []
  for row_index in range(len(data)):
    initial_clusters[(row_index%k)+1].append(row_index)
  kmeans = KMeans(initial_clusters, data)
  kmeans.run_til_complete(50)
  sse = kmeans.SSE()
  sse_values.append(sse)

k_values = [k for k in range(1, 6)]
  
plt.plot( k_values, sse_values)
  

plt.xlabel("k")
plt.ylabel("sum squared error")
plt.savefig('kelbow.png')