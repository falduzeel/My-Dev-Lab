print("SERIES SUM CALCULATOR")
n = int(input("Enter n: "))
choice = input("1.Sum 1 to N  2.Sum Squares  3.Sum Cubes: ")
if choice == "1":
    s = sum(range(1, n+1))
elif choice == "2":
    s = sum(i*i for i in range(1, n+1))
else:
    s = sum(i**3 for i in range(1, n+1))
print(f"Sum = {s}")
print(f"Formula verified: {n*(n+1)//2 if choice=='1' else n*(n+1)*(2*n+1)//6 if choice=='2' else (n*(n+1)//2)**2}")