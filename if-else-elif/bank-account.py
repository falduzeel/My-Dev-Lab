class Account:
    def __init__(self, owner: str, balance: float, is_vip: bool = False):
        self.owner = owner
        self.balance = balance
        self.is_vip = is_vip

def process_withdrawal(account: Account, amount: float) -> str:
    if amount <= 0:
        return f"Error: Withdrawal amount (${amount:.2f}) must be positive."
    
    elif amount > account.balance and not account.is_vip:
        deficit = amount - account.balance
        return f"Declined: Insufficient funds. You are short by ${deficit:.2f}."
    
    elif amount > account.balance and account.is_vip:
        account.balance -= amount
        return (
            f"Approved (VIP Overdraft): Withdrew ${amount:.2f}. "
            f"New balance: ${account.balance:.2f} (Overdrawn)"
        )
    
    else:
        account.balance -= amount
        return f"Approved: Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}"


user = Account(owner="Alex", balance=150.00, is_vip=True)

print(process_withdrawal(user, -20))
print(process_withdrawal(user, 50))
print(process_withdrawal(user, 200))