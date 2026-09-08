import numpy as np

arr = np.array([10, 20, 30, 40])
result_scalar = arr + 5
print("1. Scalar Addition (arr + 5):")
print(result_scalar)
print("-" * 40)

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row_vector = np.array([10, 20, 30])

result_2d = matrix + row_vector
print("2. 2D Matrix + 1D Row Vector:")
print(result_2d)
print("-" * 40)

col_vector = np.array([
    [100],
    [200],
    [300]
])

result_col = matrix + col_vector
print("3. 2D Matrix + Column Vector (Shape 3x1):")
print(result_col)
print("-" * 40)

data = np.array([
    [150, 60],
    [170, 70],
    [180, 80]
])

col_means = np.mean(data, axis=0)
centered_data = data - col_means

print("4. Mean-Centered Data (Broadcasting Column Means):")
print(centered_data)
