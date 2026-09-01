import numpy as np

np.random.seed(42)

employee_ids = np.arange(1001, 1101)
years_exp = np.random.randint(1, 15, size=100)
projects_completed = years_exp * 3 + np.random.randint(1, 5, size=100)
eval_scores = np.random.normal(loc=75, scale=10, size=100).clip(0, 100)

dataset = np.column_stack((employee_ids, years_exp, projects_completed, eval_scores))

mean_score = np.mean(dataset[:, 3])
std_score = np.std(dataset[:, 3])
max_score = np.max(dataset[:, 3])
top_performer_id = int(dataset[np.argmax(dataset[:, 3]), 0])

print("--- Initial Data Analysis ---")
print(f"Total Employees Analyzed: {len(dataset)}")
print(f"Average Evaluation Score: {mean_score:.2f}")
print(f"Standard Deviation      : {std_score:.2f}")
print(f"Highest Score           : {max_score:.2f} (Employee ID: {top_performer_id})")

standardized_scores = (dataset[:, 3] - mean_score) / std_score

high_performer_mask = standardized_scores > 1.0
high_performers = dataset[high_performer_mask]

print(f"\nFound {len(high_performers)} high-performing employees (Z-score > 1.0).")

output_data = np.column_stack((dataset, standardized_scores))
header = "Employee_ID,Years_Exp,Projects_Completed,Eval_Score,Z_Score"

np.savetxt("employee_performance_summary.csv", output_data, fmt="%.2f", delimiter=",", header=header, comments="")
print("\nResults successfully saved to 'employee_performance_summary.csv'.")