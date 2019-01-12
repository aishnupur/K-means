#importing libraries
import numpy as np
import pandas as pd

#fetching data from excel
data_file=pd.ExcelFile('mice_protein.xlsx')
df1 =data_file.parse('Data_Cortex_Nuclear')

#replacing the null values with the mean 
v1_null=df1.iloc[:, 1:78]
mean= v1_null.mean(axis=0)
v1_null.isnull().sum()
modified_v1 = []   
modified_v1 = v1_null.apply(lambda v1 : v1.fillna(v1.mean()),axis=0)

#converting data frame into numpy array
data = modified_v1.values

for k in range(2,10):
    previous_centroids = []
    samples, attributes = data.shape

#Randomly selecting the centroids for the first time
    z1 = data[np.random.randint(0, samples-1, k)]
    previous_centroids.append(z1)
    z2 = np.zeros(z1.shape)
    clusters = np.zeros((samples, 1))
    z4=np.linalg.norm(z1-z2)
    itr =0
    ep=0
#updating the centroids
    while z4 > ep:
        itr += 1
#finding the euclidean distance between the centroids and the data points
        z4=np.linalg.norm(z1-z2) 
        z2 = z1
        for updated_sample, sample in enumerate(data):
                distance = np.zeros((k, 1))
                for updated_z1, z0 in enumerate(z1):
                    distance[updated_z1] = np.linalg.norm(z0-sample)
                clusters[updated_sample, 0] = np.argmin(distance)
        z5 = np.zeros((k, attributes))
           
        for index in range(len(z1)):
               closest_data_points = [i for i in range(len(clusters)) if clusters[i] == index]
               z0 = np.mean(data[closest_data_points], axis=0)
               z5[index, :] = z0
        z1 = z5
        previous_centroids.append(z5)
