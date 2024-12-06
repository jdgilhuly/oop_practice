# designing ATM
# ATM needs to display balance, withdraw money, deposit money, and open account
# multiple account --> checking, saving with different rate of return

from abc import ABC, abstractmethod
from collections import defaultdict

class ATM:
    def __init__(self):
        self.accounts = defaultdict(list)
        self.user_uuid = None

    def login(self, user_uuid):
        self.user_uuid = user_uuid

    def logout(self):
        self.user_uuid = None

    def open_account(self, type):
        if self.user_uuid not in self.accounts:
            self.accounts[self.user_uuid] = []
        if type == "Checkings":
            self.accounts[self.user_uuid].append(CheckingsAccount)
        elif type == "Savings":
            self.accounts[self.user_uuid].append(SavingsAccount)

    def display_accounts(self):
        return self.accounts[self.user_uuid]






class Account(ABC):
    def __init__(self):
        self.__account_balance = 0

    def get_balance(self):
        return self.__account_balance

    def deposit_money(self, money):
        self.__account_balance += money
        return self.__account_balance

    def withdraw_money(self, money):
        if self.get_balance - money < 0:
            return False
        else:
            self.__account_balance -= money
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

atm = ATM()

