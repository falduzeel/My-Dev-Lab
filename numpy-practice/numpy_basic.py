import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
range_arr = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

print("--- 2D Array ---")
print(arr_2d)

print("\n--- Array Attributes ---")
print("Shape (Rows, Cols):", arr_2d.shape)
print("Dimensions:", arr_2d.ndim)
print("Data Type:", arr_2d.dtype)
print("Total Elements:", arr_2d.size)

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("\n--- Basic Operations ---")
print("Addition:", a + b)
print("Element-wise Sq:", b**2)
print("Scalar Multiplication:", a * 2)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\n--- Indexing & Slicing ---")
print("Element at Row 1, Col 2:", matrix[1, 2])
print("First two rows, all columns:\n", matrix[0:2, :])
print("Specific Column (Col 1):", matrix[:, 1])

data = np.array([12, 45, 78, 23, 56])

print("\n--- Statistics ---")
print("Mean (Average):", np.mean(data))
print("Max Value:", np.max(data))
print("Index of Max Value:", np.argmax(data))
print("Sum of Elements:", np.sum(data))