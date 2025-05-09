from abc import ABC
import unittest as test

class BankAccount:

    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return f"BankAccount(balance={self.balance})"
    
class Command(ABC):
    def __init__(self):
        self.success = False
    def invoke(self):
        pass

    def undo(self):
        pass

class BankAccountCommand(Command):

    class CommandType:
        DEPOSIT = "DEPOSIT"
        WITHDRAW = "WITHDRAW"

    def __init__(self, account: BankAccount, action: str, amount: float):
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount

    def invoke(self):
        if self.action == BankAccountCommand.CommandType.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == BankAccountCommand.CommandType.WITHDRAW:
            self.success = self.account.withdraw(self.amount)
    
    def undo(self):
        if not self.success:
            return
        if self.action == BankAccountCommand.CommandType.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == BankAccountCommand.CommandType.WITHDRAW:
            self.account.deposit(self.amount)

class CompositeBanckAccountCommand(Command, list):
    def __init__(self, items : list[Command]=[]):
        super().__init__()
        for item in items:
            self.append(item)

    def invoke(self):
        for command in self:
            command.invoke()

    def undo(self):
        for command in reversed(self):
            command.undo()    

class MoneyTransferCommand(CompositeBanckAccountCommand):
    def __init__(self, from_account: BankAccount, to_account: BankAccount, amount: float):
        super().__init__([
            BankAccountCommand(from_account, BankAccountCommand.CommandType.WITHDRAW, amount),
            BankAccountCommand(to_account, BankAccountCommand.CommandType.DEPOSIT, amount)
        ])

    def invoke(self):
        ok = True
        for command in self:
            if ok:
                command.invoke()
                ok = command.success
            else:
                command.success = False
        self.success = ok

class TestSuite(test.TestCase):
    def test_deposit(self):
        ba = BankAccount()
        cmd = BankAccountCommand(ba, BankAccountCommand.CommandType.DEPOSIT, 100)
        cmd.invoke()
        self.assertEqual(ba.balance, 100)
        cmd.undo()
        self.assertEqual(ba.balance, 0)

    def test_withdraw(self):
        ba = BankAccount(200)
        cmd = BankAccountCommand(ba, BankAccountCommand.CommandType.WITHDRAW, 50)
        cmd.invoke()
        self.assertEqual(ba.balance, 150)
        cmd.undo()
        self.assertEqual(ba.balance, 200)

    def test_overdraft(self):
        ba = BankAccount(200)
        cmd = BankAccountCommand(ba, BankAccountCommand.CommandType.WITHDRAW, 800)
        cmd.invoke()
        self.assertFalse(cmd.success)
        self.assertEqual(ba.balance, 200)

    def test_composite_deposit(self):
        ba = BankAccount()
        cmd1 = BankAccountCommand(ba, BankAccountCommand.CommandType.DEPOSIT, 100)
        cmd2 = BankAccountCommand(ba, BankAccountCommand.CommandType.DEPOSIT, 200)
        
        composite = CompositeBanckAccountCommand([cmd1, cmd2])
        composite.invoke()
        self.assertEqual(ba.balance, 300)
        composite.undo()
        self.assertEqual(ba.balance, 0)

    def test_money_tranfer(self):
        ba1 = BankAccount(200)
        ba2 = BankAccount(0)

        amount = 500

        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()

        self.assertEqual(ba1.balance, -300)
        self.assertEqual(ba2.balance, 500)
        transfer.undo()
        self.assertEqual(ba1.balance, 200)
        self.assertEqual(ba2.balance, 0)

if __name__ == "__main__":
    test.main()