# Given two lists of numbers, write a procedure that returns a list of the element-wise sum of the number in those two lists. 
# In the following, no imports should be used.

def add_two_lists(a, b):
    c = []
    for val1, val2 in zip(a, b):
        c.append(val1+val2)
    return c

# Given two column vectors (each represented as a list of numbers), write a procedure dot that returns the (scalar) dot product of two input vectors, each represented as a list of numbers.

def dot(v1, v2):
    sum = 0
    for a, b in zip(v1, v2):
        sum += a * b
    return sum

# Write a function add_n that takes a single numeric argument n, and returns a function. 
# The returned function should take a vector v as an argument and return a new vector with the value for n added to each element of vector v. 
# For example, add_n(10)([1, 5, 3]) should return [11, 15, 13].

def add_n(n):
    def vect(v):
        newv = []
        for elem in v:
            newv.append(n+elem)
        return newv
    return vect

# Write a function array_mult that takes two two-dimensional arrays and performs a matrix multiplication, return a new two-dimensional array. 
# Each array should be represented as a list of lists, i.e., as a list of rows, as discussed earlier.

def array_mult(A, B):
	def col(M, c): return [v[c] for v in M]
	b = []
	for i in range(len(A)):
		a = []
		for j in range(len(B[0])):
			a.append(dot(A[i], col(B, j)))
		b.append(a)
	return b
