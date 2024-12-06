# designing ATM
# ATM needs to display balance, withdraw money, deposit money, and open account
# multiple account --> checking, saving with different rate of return

from abc import ABC, abstractmethod

class ATM:
    def __init__(self):
        self.accounts = {}

    def open_account(self):



class Account(ABC):
    def __init__(self):
        self.account_balance = 0

    def get_balance(self):
        return self.account_balance

    def deposit_money(self, money):
        self.account_balance += money
        return self.account_balance

    def withdraw_money(self, money):
        if self.get_balance - money < 0:
            return False
        else:
            self.account_balance -= money
            return True

    @abstractmethod
    def savings_rate(self):
        pass

class CheckingsAccount(Account):
    def __init__(self):
        super().__init__()

    def savings_rate(self):
        return 0.01

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()

    def savings_rate(self):
        return 0.05


class User():
    pass

