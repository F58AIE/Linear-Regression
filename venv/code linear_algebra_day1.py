import numpy as np


 # vector
h = 2  # height
w = 3  # width
vector = np.array([h, w]) # np to call numpy / .array to create a numpy array
print("Vector:", vector) 


# dot product
a = np.array([1, 2]) 
b = np.array([3, 4])
# 1 * 3 = 3
# 2 * 4 = 8
# 3 + 8 = 11
dot = np.dot(a,b)  # np.dot to calculate the dot product
print("Dot product:", dot)  # 11

# matrix multiplication
A = np.array ([[1,2], [3,4]])
B = np.array ([[5,6],[7,8]])

dot0 = np.dot(A,B)
print("Dot product of matrices A and B:\n", dot0)