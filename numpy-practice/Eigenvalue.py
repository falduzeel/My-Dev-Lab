import numpy as np

np.random.seed(57)

A = np.random.randint(1, 20, (4, 4))
S = (A + A.T) / 2

eigenvalues, eigenvectors = np.linalg.eig(S)

largest = np.argmax(eigenvalues)
principal_value = eigenvalues[largest]
principal_vector = eigenvectors[:, largest]

reconstructed = eigenvectors @ np.diag(eigenvalues) @ np.linalg.inv(eigenvectors)

print("Symmetric Matrix:\n", S)
print("\nEigenvalues:\n", np.round(eigenvalues, 3))
print("\nEigenvectors:\n", np.round(eigenvectors, 3))
print("\nPrincipal Eigenvalue:\n", round(principal_value, 3))
print("\nPrincipal Eigenvector:\n", np.round(principal_vector, 3))
print("\nReconstructed Matrix:\n", np.round(reconstructed, 3))
