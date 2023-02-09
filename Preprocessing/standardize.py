#standardizing is the process of removing the mean and scaling to unit std dev.
import numpy as np

def standardize(mat):
  matrix = np.array(mat,dtype="float")
  for x in range(len(matrix[0])):
    m = np.mean(matrix[:,x]) #mean
    s = np.std(matrix[:,x]) #standard deviation
    matrix[:,x]-=m
    matrix[:,x]/=s
  return matrix