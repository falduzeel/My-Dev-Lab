import numpy as np

data = np.arange(12)
matrix_a = data.reshape(3, 4)

print("Matrix A (3x4):")
print(matrix_a)

scaled_matrix = matrix_a * 2.5
matrix_a_transposed = matrix_a.T

print("\nMatrix A Transposed (4x3):")
print(matrix_a_transposed)

dot_product = np.dot(matrix_a, matrix_a_transposed)

print("\nDot Product A @ A.T (3x3):")
print(dot_product)

print("\nStatistics for Matrix A:")
print(f"Global Mean: {np.mean(matrix_a):.2f}")
print(f"Column Sums (axis 0): {np.sum(matrix_a, axis=0)}")
print(f"Row Means (axis 1):   {np.mean(matrix_a, axis=1)}")

rng = np.random.default_rng(seed=42)
rand_matrix = rng.normal(loc=0, scale=1, size=(3, 3))

inv_matrix = np.linalg.inv(rand_matrix)
det_value = np.linalg.det(rand_matrix)

print("\nRandom 3x3 Matrix:")
print(rand_matrix)
print(f"Determinant: {det_value:.4f}")
print("\nInverse Matrix:")
print(inv_matrix)