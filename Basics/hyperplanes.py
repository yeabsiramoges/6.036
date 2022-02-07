import numpy as np

# Provide an expression that sets A to be a 2x3 numpy array, containing any values you wish.
A = np.array([[1, 2, 3], [4, 5, 6]])

# Write a procedure that takes an array and returns the transpose of the array.
# You can use "np.transpose" or the ".T" but you may not use a loop.

def tp(A):
	return A.T

# Write a procedure that takes a list of numbers and returns a 2D numpy array representing a row vector containing those numbers.

def rv(value_list):
	return np.array([value_list])

# Write a procedure that takes a list of numbers and returns a 2D numpy array representing a column vector containing those numbers.
# You can use the rv procedure

def cv(value_list):
	return rv(value_list).T

# Write a procedure that takes a column vector and returns the vector's Euclidean length (or equivalently, its magnitude) as a scalar.
# You may not use np.linalg.norm, and you may not use a loop.

def length(col_v):
	return np.ndarray.item(np.sqrt(col_v.T.dot(col_v)))

# Write a procedure that takes a column vector and returns a unit vector in the same directon. 
# You may not use a for loop.
# Use your length procedure from above.

def normalize(col_v):
	return col_v/length(col_v)

# Write a procedure that tales a 2D array and returns the final column as a two dimensional array.
# You may not use a for loop.

def index_final_col(A):
	return A[:,-1,:]

# Add two columns of a matrix together and return a column vector as a numpy array

def transform(data):
	return data[:,0:1] + data[:,1:]