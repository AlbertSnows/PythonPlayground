import uuid

from src.lib.functions import attempt


def transfer_money(from_account, to_account, transfer_amount):
    from_balance = from_account.balance
    assert from_balance >= transfer_amount
    to_account.balance += transfer_amount
    from_account.balance -= transfer_amount
    # todo: log to ledger
    return from_account, to_account

class BasicAccount:
    def __init__(self, name: str, balance: float =0.0):
        self.id = uuid.uuid4()
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        assert amount <= self.balance
        self.balance -= amount
        return self

def evaluate():
    new_account = BasicAccount("tom")
    transfer_account = BasicAccount("jerry", 100.20)


    ifrom, ito = attempt(lambda: transfer_money(new_account, transfer_account, 20.10),
                         (new_account, transfer_account))
    ifrom, ito = transfer_money(transfer_account, new_account, 20.10)
    print([ifrom, ito])

evaluate()