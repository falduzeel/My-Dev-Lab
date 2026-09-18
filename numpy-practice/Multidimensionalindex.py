import numpy as np

np.random.seed(41)

samples = 100
coords = np.random.uniform(-50, 50, (samples, 3))
temp = np.random.uniform(15, 45, (samples, 1))
data = np.hstack((coords, temp))

print("Shape:", data.shape)

mask = (data[:, 3] > 35) & (data[:, 2] > 0)
filtered = data[mask]

print("Filtered Samples:", len(filtered))

top5_idx = np.argsort(data[:, 0])[-5:]
top5 = data[top5_idx]

print("\nTop 5 X Samples:")
print(top5)

over = data[:, 3] > 40
data[over, 3] = 40

print("\nCapped Readings:", np.sum(over))
print("Max Temp:", np.max(data[:, 3]))
