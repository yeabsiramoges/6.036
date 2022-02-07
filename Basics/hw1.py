def length(col_v):
	return np.ndarray.item(np.sqrt(col_v.T.dot(col_v)))

# Write a Python function using numpy operations (no loops!) that takes column vectors (d by 1) x and th (of the same dimension) and scalar th0 and returns the signed perpendicular distance (as a 1 by 1 array) from the hyperplane encoded by (th, th0) to x.
# Note that you are allowed to use the "length" function defined in previous coding qestions (including week 1 exercises).

def signed_dist(x, th, th0):
	out = th.T.dot(x) + th0
	return out/length(out)

# Write a column function that takes a column vector x, th, and a scalar th0 and returns the sign
# should be a 2D array

def positive(x, th, th0):
	out = th.T.dot(x)+th0
	val = out/length(th)
	return np.sign(val)

# A should be a 1 by 5 array of values, either +1, 0, or -1, indicating, for each point in data, whether it is on the positive side of the hyperplane defined by th, th0. 
# Use data, th, th0 as variables in your submission
A = positive(data, th, th0)