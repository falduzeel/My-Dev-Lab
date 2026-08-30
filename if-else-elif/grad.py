marks = int(input("Enter your marks (0 to 100): "))

if marks >= 90:
    print("Grade: A+ (Excellent)")
elif marks >= 75:
    print("Grade: A (Very Good)")
elif marks >= 60:
    print("Grade: B (Good)")
elif marks >= 35:
    print("Grade: C (Pass)")
else:
    print("Grade: F (Fail)")
