import numpy as np

marks = np.array([45, 78, 92, 56, 88, 34, 67, 95, 73, 81])

print("Original Marks:")
print(marks)

passed = marks[marks >= 50]
print("\nPassed Students:")
print(passed)

failed = marks[marks < 50]
print("\nFailed Students:")
print(failed)

excellent = marks[marks >= 85]
print("\nExcellent Students:")
print(excellent)

updated_marks = np.where(marks < 50, marks + 5, marks)
print("\nMarks After Grace Marks:")
print(updated_marks)

status = np.where(marks >= 50, "Pass", "Fail")
print("\nStudent Status:")
print(status)

high_marks = marks[marks > marks.mean()]
print("\nMarks Above Average:")
print(high_marks)

print("\nAverage Marks:")
print(marks.mean())

print("\nHighest Marks:")
print(marks.max())

print("\nLowest Marks:")
print(marks.min())

print("\nNumber of Passed Students:")
print(np.sum(marks >= 50))

print("\nNumber of Failed Students:")
print(np.sum(marks < 50))