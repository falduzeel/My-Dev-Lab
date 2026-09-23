print("=== Shopping Discount Calculator ===")

amount = float(input("Enter your shopping amount: "))

if amount >= 5000:
    discount = 20
elif amount >= 3000:
    discount = 15
elif amount >= 1500:
    discount = 10
elif amount >= 500:
    discount = 5
else:
    discount = 0

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("\n=== Bill ===")
print("Original Amount:", amount)
print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)
