```python
import numpy as np

rng = np.random.default_rng(42)

print("--- 1. Advanced Array Manipulation ---")

matrix_a = np.arange(1, 7).reshape(2, 3)
matrix_b = np.arange(7, 13).reshape(2, 3)

v_stacked = np.vstack((matrix_a, matrix_b))
h_stacked = np.hstack((matrix_a, matrix_b))
d_stacked = np.dstack((matrix_a, matrix_b))

print("Vertical Stack:\n", v_stacked)
print("Horizontal Stack:\n", h_stacked)
print("Depth Stack Shape:", d_stacked.shape)

concatenated_axis0 = np.concatenate((matrix_a, matrix_b), axis=0)

print("\n--- 2. Linear Algebra Operations ---")

square_matrix = np.array([
    [4, 2],
    [1, 3]
])

dot_product = square_matrix @ matrix_a

print("Matrix Multiplication (@ operator):\n", dot_product)

det = np.linalg.det(square_matrix)
inv = np.linalg.inv(square_matrix)

print(f"Determinant: {det:.2f}")
print("Inverse Matrix:\n", inv)

eigenvalues, eigenvectors = np.linalg.eig(square_matrix)

print("Eigenvalues:", eigenvalues)

U, S, Vt = np.linalg.svd(square_matrix)

print("SVD Singular Values (S):", np.round(S, 3))

print("\n--- 3. Masked Arrays ---")

raw_data = np.array([
    10, 20, -999, 40, -999, 60
], dtype=float)

masked_data = np.ma.masked_equal(raw_data, -999)

print("Original Data:", raw_data)
print("Masked Data:", masked_data)
print("Mean ignoring masked values:", masked_data.mean())

data_with_nans = np.where(
    raw_data == -999,
    np.nan,
    raw_data
)

print("NaN-aware Mean:", np.nanmean(data_with_nans))

print("\n--- 4. Feature Normalization & Broadcasting ---")

features = rng.integers(50, 100, size=(4, 3))

print("Raw Features:\n", features)

mean = np.mean(features, axis=0)
std = np.std(features, axis=0)

z_scores = (features - mean) / std

print(
    "Normalized Features (Z-scores):\n",
    np.round(z_scores, 3)
)

min_vals = features.min(axis=0)
max_vals = features.max(axis=0)

min_max_scaled = (
    features - min_vals
) / (max_vals - min_vals)

print(
    "Min-Max Scaled Features:\n",
    np.round(min_max_scaled, 3)
)

print("\n--- 5. Einstein Summation ---")

einsum_dot = np.einsum(
    'ij,jk->ik',
    square_matrix,
    matrix_a
)

print("Matrix Product via einsum:\n", einsum_dot)

col_sums = np.einsum('ij->j', features)

print("Column Sums via einsum:", col_sums)
```
