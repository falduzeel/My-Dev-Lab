import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])

matrix_zeros = np.zeros((3, 3))

matrix = np.arange(1, 10).reshape(3, 3)

array_sum = np.sum(arr_1d)
array_mean = np.mean(arr_1d)
matrix_squared = matrix ** 2

print("1D Array:", arr_1d)
print("\n3x3 Zeros Matrix:\n", matrix_zeros)
print("\n3x3 Matrix:\n", matrix)
print("\nSum of 1D Array:", array_sum)
print("Mean of 1D Array:", array_mean)
print("\nSquared Matrix:\n", matrix_squared)
