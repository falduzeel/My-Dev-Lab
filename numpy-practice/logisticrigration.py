import numpy as np

features = np.random.randn(100, 5)
weights = np.random.randn(5, 1)
bias = 0.5

z = np.dot(features, weights) + bias
predictions = 1 / (1 + np.exp(-z))

targets = np.random.randint(0, 2, size=(100, 1))
loss = -np.mean(targets * np.log(predictions + 1e-15) + (1 - targets) * np.log(1 - predictions + 1e-15))

learning_rate = 0.01
error = predictions - targets
dw = np.dot(features.T, error) / len(features)
db = np.mean(error)

weights -= learning_rate * dw
bias -= learning_rate * db

print("Loss:", loss)
print("Updated Weights Shape:", weights.shape)