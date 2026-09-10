import numpy as np

print("DAY 32 - NUMPY")

arr = np.array([10, 20, 30, 40, 50])

print("\nOriginal Array:")
print(arr)

print("\nSum:")
print(np.sum(arr))

print("\nMean:")
print(np.mean(arr))

print("\nMaximum:")
print(np.max(arr))

print("\nMinimum:")
print(np.min(arr))

print("\nStandard Deviation:")
print(np.std(arr))

print("\nSorted Array:")
numbers = np.array([50, 10, 40, 20, 30])
print(np.sort(numbers))

print("\n2D Array:")
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(matrix)

print("\nSum of All Elements:")
print(np.sum(matrix))

print("\nColumn Sum:")
print(np.sum(matrix, axis=0))

print("\nRow Sum:")
print(np.sum(matrix, axis=1))

print("\nMaximum of Each Column:")
print(np.max(matrix, axis=0))

print("\nMinimum of Each Row:")
print(np.min(matrix, axis=1))

print("\nTranspose:")
print(matrix.T)

print("\nReshaped Array:")
arr2 = np.arange(1, 13)
print(arr2.reshape(3, 4))

print("\nRandom Array:")
random_array = np.random.randint(1, 100, 5)
print(random_array)

print("\nRandom Array Sum:")
print(np.sum(random_array))