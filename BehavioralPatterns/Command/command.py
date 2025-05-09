from abc import ABC, abstractmethod

class BankAccount:

    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")
            return True
        else:
            print("Insufficient funds")
            return False

    def __str__(self):
        return f"BankAccount(balance={self.balance})"
    
class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass

class BankAccountCommand(Command):

    class CommandType:
        DEPOSIT = "DEPOSIT"
        WITHDRAW = "WITHDRAW"

    def __init__(self, account: BankAccount, action: str, amount: float):
        self.account = account
        self.action = action
        self.amount = amount
        self.success = None

    def invoke(self):
        if self.action == BankAccountCommand.CommandType.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == BankAccountCommand.CommandType.WITHDRAW:
            self.success = self.account.withdraw(self.amount)
    
    def undo(self):
        if not self.success:
            print("Cannot undo an unsuccessful command.")
            return
        if self.action == BankAccountCommand.CommandType.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == BankAccountCommand.CommandType.WITHDRAW:
            self.account.deposit(self.amount)


if __name__ == "__main__":
    ba = BankAccount() # 0 
    cmd = BankAccountCommand(ba, BankAccountCommand.CommandType.DEPOSIT, 100)
    cmd.invoke() # Deposited: 100, New Balance: 100
    cmd = BankAccountCommand(ba, BankAccountCommand.CommandType.WITHDRAW, 50)
    cmd.invoke() # Withdrawn: 50, New Balance: 50    
    cmd.undo() # Deposited: 50, New Balance: 100

    illegal_cmd = BankAccountCommand(ba, BankAccountCommand.CommandType.WITHDRAW, 1000)
    illegal_cmd.invoke() # Insufficient funds
    illegal_cmd.undo() # Insufficient funds
