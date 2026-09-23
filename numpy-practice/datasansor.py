import numpy as np

np.random.seed(7)

# Smart City sensor dataset
temperature = np.random.randint(20, 41, 12)
humidity = np.random.randint(35, 91, 12)

data = np.column_stack((temperature, humidity))

print("Temperature & Humidity")
print(data)

# Statistics
print("\nAverage Temperature:", np.mean(temperature))
print("Highest Humidity:", np.max(humidity))

# Filter hot days
hot_days = data[data[:, 0] >= 30]
print("\nHot Days (>=30°C)")
print(hot_days)

# Reshape into weekly report
weekly = temperature.reshape(3, 4)
print("\nWeekly Temperature")
print(weekly)

# Normalize values
normalized = (temperature - temperature.min()) / (temperature.max() - temperature.min())
print("\nNormalized Temperature")
print(np.round(normalized, 2))
