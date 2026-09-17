import numpy as np

# 1. Advanced Indexing & Choice (Random Sampling)
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
print("Fancy Indexing:", arr[indices])

samples = np.random.choice(['A', 'B', 'C'], size=5, p=[0.6, 0.3, 0.1])
print("Random Choice:", samples)

# 2. Broadcasting (Combining 1D & 2D Arrays without Loops)
matrix = np.ones((3, 3))
vector = np.array([1, 2, 3])
broadcasted = matrix + vector
print("Broadcasted Result:\n", broadcasted)

# 3. Fast Conditional Logic with np.where
scores = np.array([45, 80, 32, 90, 60])
status = np.where(scores >= 50, 'Pass', 'Fail')
print("Status:", status)

# 4. Linear Algebra (Matrix Multiplication & Inverse)
A = np.array([[2, 1], [1, 3]])
B = np.array([[1, 2], [3, 4]])
dot_product = np.matmul(A, B)
print("Matrix Product:\n", dot_product)
