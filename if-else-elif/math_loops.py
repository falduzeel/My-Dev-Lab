n = int(input("Enter N: "))

sum_for = 0
for i in range(1, n+1):
    sum_for += i
print(f"Sum 1-{n}: {sum_for}")

fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print(f"Factorial {n}: {fact}")

is_prime = True
if n > 1:
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            is_prime = False
            break
print(f"{n} prime: {'Yes' if is_prime else 'No'}")

print("Table:")
r = 1
while r <= 5:
    for c in range(1, 6):
        print(f"{n}*{c}={n*c}", end=" ")
    print()
    r += 1