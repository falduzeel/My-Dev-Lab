import numpy as np

np.random.seed(37)

students = 8
subjects = 5

marks = np.random.randint(35, 101, (students, subjects))

bonus = np.array([5, 2, 0, 3, 1])
updated_marks = np.clip(marks + bonus, 0, 100)

total = updated_marks.sum(axis=1)
average = updated_marks.mean(axis=1)

passed = np.all(updated_marks >= 40, axis=1)
topper = np.argmax(total)

print("Original Marks:\n", marks)
print("\nUpdated Marks:\n", updated_marks)
print("\nTotal:", total)
print("Average:", np.round(average, 2))
print("Passed:", passed)
print("\nTopper Index:", topper)
print("Topper Total:", total[topper])
