import numpy as np

np.random.seed(42)

scores = np.array([88, 42, 95, 67, 73, 95, 51])
print("Original Scores:", scores)

sorted_scores = np.sort(scores)
print("\nSorted Scores (Copy):", sorted_scores)

matrix = np.array([[3, 9, 1], 
                   [7, 2, 8]])

print("\nSorted Matrix by Row (axis=1):\n", np.sort(matrix, axis=1))
print("Sorted Matrix by Column (axis=0):\n", np.sort(matrix, axis=0))

students = np.array(["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"])
sort_indices = np.argsort(scores)

print("\nIndices that sort scores:", sort_indices)
print("Students sorted by scores (lowest to highest):")
print(students[sort_indices])

passing_status = np.where(scores >= 70, "Pass", "Fail")
print("\nPass/Fail Status:", passing_status)

high_scorers_idx = np.where(scores > 80)[0]
print("Indices of scores > 80:", high_scorers_idx)
print("Actual high scores:", scores[high_scorers_idx])

highest_score_idx = np.argmax(scores)
lowest_score_idx = np.argmin(scores)

print(f"\nHighest score is {scores[highest_score_idx]} at index {highest_score_idx} ({students[highest_score_idx]})")
print(f"Lowest score is {scores[lowest_score_idx]} at index {lowest_score_idx} ({students[lowest_score_idx]})")

failing_count = np.count_nonzero(scores < 70)
print("\nNumber of failing scores (<70):", failing_count)

unique_vals, counts = np.unique(scores, return_counts=True)
print("Unique scores:", unique_vals)
print("Score frequencies:", counts
