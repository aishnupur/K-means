# K-means
The data set can be downloaded from the website  https://www.kaggle.com/ruslankl/mice-protein-expression.
The missing values were imputed using the mean of the dimensions. The mice were clustered into k clusters using K-means clustering algorithm. 
In the k-means clustering algorithm the clusters are formed by undergoing the following steps:
1. Randomly assign the cluster centroids in the dataset.
2. Calculate the distance of each data points from these cluster centroids using either euclidean distance or manhattan distance.
3. Assign the data points to the respective clusters depending on the shortest distance from the cluster centroids.
4. Find the mean of the cluster.
5. The mean value becomes the new cluster centroid.
6. Repeat steps 2 to 5 till the proper clusters are formed, which we come to know by checking if the mean value is changing any further.
