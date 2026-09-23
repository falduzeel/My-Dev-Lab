print("=== Student Result Checker ===")

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
    message = "Excellent performance!"
elif marks >= 80:
    grade = "A"
    message = "Very good performance!"
elif marks >= 70:
    grade = "B"
    message = "Good performance!"
elif marks >= 60:
    grade = "C"
    message = "Keep improving!"
elif marks >= 50:
    grade = "D"
    message = "You passed, but work harder."
elif marks >= 33:
    grade = "E"
    message = "You passed."
else:
    grade = "F"
    message = "You failed. Don't give up!"

print("\n=== Result ===")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)
print("Message:", message)

if marks >= 33:
    print("Status: PASS")
else:
    print("Status: FAIL")
