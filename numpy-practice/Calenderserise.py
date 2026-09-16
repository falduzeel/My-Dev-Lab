import numpy as np
import pandas as pd

np_data = np.random.randint(10, 100, size=(5, 3))
df = pd.DataFrame(np_data, columns=['Metric_A', 'Metric_B', 'Metric_C'])

back_to_numpy = df.to_numpy()

print("=== DataFrame to NumPy ===")
print(back_to_numpy)
print("Type:", type(back_to_numpy))

df['Metric_A_Log'] = np.log(df['Metric_A'])
df_normalized = np.exp(df[['Metric_A', 'Metric_B']])

print("\n=== Direct ufunc Application on Pandas ===")
print(df[['Metric_A', 'Metric_A_Log']].head(3))

df['Score'] = np.random.randint(50, 100, size=len(df))

conditions = [
    (df['Score'] >= 90),
    (df['Score'] >= 75) & (df['Score'] < 90),
    (df['Score'] < 75)
]
choices = ['High', 'Medium', 'Low']

df['Category'] = np.select(conditions, choices, default='Unknown')

print("\n=== Conditional Categorization via np.select ===")
print(df[['Score', 'Category']])

raw_series = pd.Series([10.0, np.nan, 30.0, np.nan, 50.0])

mean_val = np.nanmean(raw_series)
std_val = np.nanstd(raw_series)

cleaned_series = np.where(np.isnan(raw_series), mean_val, raw_series)

print("\n=== Handling NaNs with NumPy ===")
print("Original Series:\n", raw_series.values)
print("NaN-aware Mean:", mean_val)
print("Cleaned Array:", cleaned_series)

weights = np.array([0.4, 0.35, 0.25])
portfolio_returns = np.dot(df[['Metric_A', 'Metric_B', 'Metric_C']].to_numpy(), weights)

df['Portfolio_Return'] = portfolio_returns

print("\n=== Matrix Dot Product Integration ===")
print(df[['Metric_A', 'Metric_B', 'Metric_C', 'Portfolio_Return']])
