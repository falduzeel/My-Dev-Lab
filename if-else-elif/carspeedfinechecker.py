print("=== Car Speed Fine Checker ===")

speed = int(input("Enter your car speed (km/h): "))

if speed <= 60:
    status = "Safe Speed"
    fine = 0
elif speed <= 80:
    status = "Warning"
    fine = 500
elif speed <= 100:
    status = "Overspeed"
    fine = 1000
elif speed <= 120:
    status = "High Overspeed"
    fine = 2000
else:
    status = "Dangerous Speed"
    fine = 5000

print("\n=== Result ===")
print("Speed:", speed, "km/h")
print("Status:", status)
print("Fine: ₹", fine)

if fine == 0:
    print("Drive safely!")
else:
    print("Please follow speed limits.")
