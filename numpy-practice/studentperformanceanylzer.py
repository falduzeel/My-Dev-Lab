import numpy as np

students = np.array([
    [85, 78, 92, 88],
    [67, 72, 70, 75],
    [95, 91, 89, 96],
    [56, 64, 61, 59],
    [78, 85, 80, 82],
    [91, 87, 94, 90],
    [73, 69, 76, 71],
    [88, 93, 86, 89]
])

print("Student Marks:")
print(students)

subjects = ["Maths", "Physics", "Chemistry", "Computer"]

print("\nAverage Marks:")
print(np.mean(students, axis=0))

print("\nHighest Marks:")
print(np.max(students, axis=0))

print("\nLowest Marks:")
print(np.min(students, axis=0))

print("\nOverall Student Average:")
student_average = np.mean(students, axis=1)
print(student_average)

print("\nHighest Student Average:")
print(np.max(student_average))

print("\nLowest Student Average:")
print(np.min(student_average))

print("\nTop Student Position:")
print(np.argmax(student_average) + 1)

print("\nSorted Student Averages:")
print(np.sort(student_average)[::-1])

print("\nStudents Above 80 Average:")
high_performers = students[student_average >= 80]
print(high_performers)

print("\nStudents Below 70 Average:")
low_performers = students[student_average < 70]
print(low_performers)

print("\nTotal Marks Of Each Student:")
total_marks = np.sum(students, axis=1)
print(total_marks)

print("\nMaximum Total Marks:")
print(np.max(total_marks))

print("\nMinimum Total Marks:")
print(np.min(total_marks))

print("\nTotal Class Marks:")
print(np.sum(students))

print("\nClass Average:")
print(np.mean(students))

print("\nStandard Deviation:")
print(np.std(students))

print("\nMedian:")
print(np.median(students))

print("\nStudents With Maths Above 80:")
print(students[students[:, 0] > 80])

print("\nStudents With Physics Above 80:")
print(students[students[:, 1] > 80])

print("\nStudents With Chemistry Above 80:")
print(students[students[:, 2] > 80])

print("\nStudents With Computer Above 80:")
print(students[students[:, 3] > 80])

print("\nPassed Students:")
passed = np.all(students >= 40, axis=1)
print(passed)

print("\nNumber Of Passed Students:")
print(np.sum(passed))

print("\nNumber Of Students:")
print(students.shape[0])

print("\nNumber Of Subjects:")
print(students.shape[1])

print("\nMarks Greater Than 90:")
print(students[students > 90])

print("\nMarks Less Than 60:")
print(students[students < 60])

bonus_marks = np.where(students < 75, students + 5, students)

print("\nMarks After Bonus:")
print(bonus_marks)

capped_marks = np.clip(students, 60, 95)

print("\nMarks After Clipping:")
print(capped_marks)

normalized = students / 100

print("\nNormalized Marks:")
print(normalized)

rounded_average = np.round(student_average, 2)

print("\nRounded Averages:")
print(rounded_average)

rank_order = np.argsort(student_average)[::-1]

print("\nStudent Ranking:")
for rank, student_index in enumerate(rank_order, start=1):
    print(
        "Rank",
        rank,
        "- Student",
        student_index + 1,
        "- Average",
        round(student_average[student_index], 2)
    )

print("\nSubject Performance:")

for i in range(students.shape[1]):
    average = np.mean(students[:, i])
    highest = np.max(students[:, i])
    lowest = np.min(students[:, i])

    print(
        subjects[i],
        "Average:",
        round(average, 2),
        "Highest:",
        highest,
        "Lowest:",
        lowest
    )

print("\nCorrelation Matrix:")
print(np.corrcoef(students.T))

print("\nTranspose Of Marks:")
print(students.T)

print("\nFirst Three Students:")
print(students[:3])

print("\nLast Three Students:")
print(students[-3:])

print("\nFirst Two Subjects:")
print(students[:, :2])

print("\nLast Two Subjects:")
print(students[:, 2:])

print("\nSorted Marks:")
print(np.sort(students, axis=1))

print("\nStudent With Maximum Maths Marks:")
maths_index = np.argmax(students[:, 0])
print(students[maths_index])

print("\nStudent With Maximum Physics Marks:")
physics_index = np.argmax(students[:, 1])
print(students[physics_index])

print("\nStudent With Maximum Chemistry Marks:")
chemistry_index = np.argmax(students[:, 2])
print(students[chemistry_index])

print("\nStudent With Maximum Computer Marks:")
computer_index = np.argmax(students[:, 3])
print(students[computer_index])