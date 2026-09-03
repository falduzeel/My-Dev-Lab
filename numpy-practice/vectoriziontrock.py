import numpy as np

print("=== 1. Custom Outer Operations with Broadcasting ===")
x = np.array([1, 2, 3])
y = np.array([10, 20, 30, 40])

grid_add = x[:, np.newaxis] + y
grid_sub = x[:, np.newaxis] - y

print("Addition Grid:\n", grid_add)
print("Subtraction Grid:\n", grid_sub)

print("\n=== 2. Pairwise Distance Matrix (Euclidean Distance) ===")
points = np.array([[0, 0], [3, 0], [0, 4]])

diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
dist_matrix = np.sqrt(np.sum(diff**2, axis=-1))

print("Points:\n", points)
print("Distance Matrix:\n", dist_matrix)

print("\n=== 3. Speed Up Operations with np.vectorize ===")


def complex_math(a, b):
    return a**2 + b if a > b else b**2 - a


vec_func = np.vectorize(complex_math)

arr_a = np.array([1, 5, 2])
arr_b = np.array([3, 2, 4])

result = vec_func(arr_a, arr_b)
print("Vectorized Result:", result)

print("\n=== 4. Normalizing Features Across Batches ===")
X = np.array(
    [[10.0, 200.0, 0.5], [20.0, 100.0, 0.8], [15.0, 150.0, 0.2], [25.0, 300.0, 0.9]]
)

mean = X.mean(axis=0)
std = X.std(axis=0)

X_scaled = (X - mean) / std

print("Original Mean:", mean)
print("Scaled Data:\n", np.round(X_scaled, 2))