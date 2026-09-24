print("=== ATM Withdrawal System ===")

balance = 25000
amount = int(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
elif amount % 100 != 0:
    print("Enter amount in multiples of 100")
elif amount > 10000:
    print("Daily withdrawal limit exceeded")
else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Withdrawn Amount: ₹", amount)
    print("Remaining Balance: ₹", balance)

if balance < 5000:
    print("Warning: Your balance is low")
elif balance < 10000:
    print("Keep monitoring your balance")
else:
    print("Your balance is healthy")