class KMeans():
  def  __init__(self, initial_clusters, data):
    self.initial_clusters = initial_clusters
    self.data = data
    self.clusters = initial_clusters
    
  def distance(self, point_1 , point_2):
    distance = 0
    for value in range(len(point_1)):
      distance += (point_1[value] - point_2[value]) **2
    return distance ** 0.5

  def get_centers(self):
    new_centers = {k: [] for k in self.clusters}

    for cluster in self.clusters:
      #for each column in data get column index
      for column in range(len(self.data[0])):
        #create 0 sum 
        sum_data_cluster = 0
        #get record value in cluster
        for row in self.clusters[cluster]:
          #add to sum data of row and column 
          
          sum_data_cluster += self.data[row][column]

        #round mean 
        sum_data_cluster = round(sum_data_cluster/len(self.clusters[cluster]),3)

        #update centers
        new_centers[cluster].append(sum_data_cluster)
    
    self.centers = new_centers
  
  def get_new_clusters(self):
    new_clusters = {k: [] for k in self.clusters}

    #find closest datapoints
    #get row values
    for row in range(len(self.data)):
      
      smallest_distance = 1000
      chosen_cluster = None
      #compare them to different clusters centers

      for cluster in self.centers:
        distance =  self.distance(self.data[row], self.centers[cluster])
        
        if distance < smallest_distance:
          smallest_distance = distance
          chosen_cluster = cluster
      new_clusters[chosen_cluster].append(row)
    

    return new_clusters

  def run_til_complete(self, iterations):

    for i in range(iterations):
      self.get_centers()
      new_clusters = self.get_new_clusters()
      if self.clusters == new_clusters:
        break
      self.clusters = new_clusters
  
  def SSE(self):
    
    sse = 0
    for cluster in self.clusters:
      for value in self.clusters[cluster]:
        square_distance = self.distance(self.centers[cluster], self.data[value]) ** 2
        sse += square_distance

    return sse




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

# we usually don't know the classes, of the 
# data we're trying to cluster, but I'm providing
# them here so that you can actually see that the
# k-means algorithm succeeds.

classes = ['Shortbread',
            'Fortune',
            'Shortbread',
            'Sugar',
            'Fortune',
            'Shortbread',
            'Sugar',
            'Shortbread',
            'Sugar',
            'Shortbread',
            'Sugar',
            'Fortune',
            'Shortbread',
            'Fortune',
            'Sugar',
            'Shortbread',
            'Sugar',
            'Fortune',
            'Shortbread']


initial_clusters = {
    1: [0,3,6,9,12,15,18],
    2: [1,4,7,10,13,16],
    3: [2,5,8,11,14,17]
    }
kmeans = KMeans(initial_clusters, data)
kmeans.run_til_complete(100)


print(kmeans.clusters)
print(kmeans.centers)

{
    0: [0, 2, 5, 7, 9, 12, 15, 18],
    1: [3, 6, 8, 10, 14, 16],
    2: [1, 4, 11, 13, 17]
}

{
    0: [0.133, 0.171, 0.291, 0.416],
    1: [0.018, 0.1, 0.378, 0.51],
    2: [0.21, 0.08, 0.38, 0.346]
}



