# import statements
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def knn(N,d):
    # make an matrix N by d
    points = np.empty([N, d])
    for i in range(N):
        for j in range(d):
            # uniformly select a random number for each point in the matrix
            points[i][j] = np.random.uniform()
    # each row in the matrix is a randomly selected point in C(d) where d is the dimensions of the cube
    
    # compute the euclidean distance between each and every point
    distance_matrix = euclidean_distances(points,points)
    # since this will double count and count distances between a point and itself, we need to extract only the "triangle" of data we want
    pairwise_diff = np.zeros(int((N*(N-1))/2))
    index = 0
    for i in range(N):
        for j in range(i):
            pairwise_diff[index] = distance_matrix[i][j]
            index = index + 1
    
    # create a histogram now with the useful distances
    plt.figure()
    plt.title(str(N)+" samples in "+str(d)+" dimensions")
    plt.hist(pairwise_diff)
    plt.show() 
    
knn(100,2)
knn(100,3)
knn(100,10)
knn(100,100)
knn(100,1000)
knn(100,10000)
