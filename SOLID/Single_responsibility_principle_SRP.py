"""
    OOP - every class and method must have only one reason to change.
    FP - every function must have only one reason to change
"""

from typing import Tuple

def process_customer_money(account_number: int,
                           balance:        int,
                           operation:      str,
                           amount:         int=0) -> Tuple[int, int]:
    if operation == 'deposit':
        balance += amount
        print(f'New balance: {balance} ')
    elif operation == 'withdraw':
        if amount > balance:
            raise ValueError("Unfortunately your balance is insufficient for any withdrawals right now...")
        balance -= amount
        print(f'New balance: {balance} ')
    elif operation == 'print':
        print(f'Account no:{account_number}, Balance: {balance}')
    elif operation == 'change_account_number':
        account_number = amount
        print(f'Your account number has changed to "{account_number}" ')
    return account_number, balance

