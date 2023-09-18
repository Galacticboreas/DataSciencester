"""
    OOP - every class and method must have only one reason to change.
    FP - every function must have only one reason to change
"""

# 1) Violation of the principle.

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

# In this example, the principle of sole responsibility is not observed, 
# since the process_customer_money function deals with several operations: 
# crediting to an account, withdrawing, withdrawing balances, etc.

# 2) Compliance with the principle

from typing import Tuple

def deposit_money(account_number: int, balance: float, amount: int) -> Tuple[int, int]:
    return account_number, balance + amount

def withdraw_money(account_number: int, balance: float, amount: int) -> Tuple[int, int]:
    if amount > balance:
        raise ValueError('Unfortunately your balance is insufficient for any withdrawals right now...')
    return account_number, balance - amount

def print_balance(account_number: int, balance: float) -> str:
    return f'Account no: {account_number}, New balance: {balance}'

def change_account_number(current_account_number: int, new_account_number: int) -> str:
    return f'Your account number has changed to "{new_account_number}" '

my_account_details = print_balance(account_number=12345678, balance=540.00)
print(my_account_details)

# 3) An example of a codebase extension.

def transfer_money(account_no1:   int,
                   balance1:      float,
                   account_no2:   int,
                   balance2:      float,
                   amount:        float) -> Tuple[Tuple[int, float], Tuple[int, float]]:
    account_no1, balance1 = withdraw_money(account_no1, balance1, amount)
    account_no2, balance2 = deposit_money(account_no2, balance2, amount)

    return (account_no1, balance1), (account_no2, balance2)

# setting accounts
account_1 = (12345678, 850.00)
account_2 = (87654321, 400.00)

# transferring 100 from account_1 to account_2
account_1, account_2 = transfer_money(account_1[0], account_1[1],
                                      account_2[0], account_2[1],
                                      100.00
                                      )

# displaying information about the transfer
print(print_balance(account_1[0], account_1[1]))
print(print_balance(account_2[0], account_2[1]))

# As a result , it turns out:
# Account no: 12345678, New balance: 750.0
# Account no: 87654321, New balance: 500.0
