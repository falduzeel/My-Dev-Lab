import numpy as np

a = np.array([10, 20, 30, 40, 50])

print(a)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)

print(a + 10)
print(a - 5)
print(a * 2)
print(a / 10)

print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.sum(a))

b = np.array([[1, 2, 3], [4, 5, 6]])

print(b)
print(b.shape)
print(b.ndim)

print(b + 10)
print(b * 2)

print(np.sum(b))
print(np.mean(b))
print(np.max(b))
print(np.min(b))

c = np.arange(1, 21)

print(c)

d = c.reshape(4, 5)

print(d)

print(d[0])
print(d[:, 0])
print(d[1:3, 1:4])

print(np.zeros((3, 3)))
print(np.ones((2, 4)))

random_array = np.random.randint(1, 100, size=(3, 3))

print(random_array)
print(np.max(random_array))
print(np.min(random_array))
print(np.mean(random_array))
