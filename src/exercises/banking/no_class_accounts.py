from functools import singledispatch, partial
import uuid
from src.lib.functions import attempt

open_accounts = {}

def create_basic_account(name, balance=0.0):
    return {
        "id": uuid.uuid4(),
        "name": name,
        "balance": balance,
        "transaction_history": {}
    }

def log_transaction():
    pass

def transfer_money(from_account, to_account, transfer_amount):
    from_balance = from_account["balance"]
    assert from_balance >= transfer_amount
    to_account["balance"] += transfer_amount
    from_account["balance"] -= transfer_amount
    # todo: log to ledger
    return from_account, to_account

def add_account_names(accounts, new_account):
    name = new_account["name"]
    assert name not in accounts
    accounts[name] = new_account
    return accounts

def deposit(account, amount):
    account["balance"] += amount
    return account

def withdraw(account, amount):
    assert account["balance"] >= amount
    account["balance"] -= amount
    return account


def evaluate():
    add = partial(add_account_names, open_accounts)
    new_account = create_basic_account("tom")
    transfer_account = create_basic_account("jerry", 100.20)
    internal_open_accounts = add(new_account)
    internal_open_accounts = add(transfer_account)


    internal_open_accounts = attempt(lambda: transfer_money(internal_open_accounts["tom"],
                                                            transfer_account["jerry"], 20.10),
                                       internal_open_accounts)
    _, _ = transfer_money(internal_open_accounts["jerry"],
                                              internal_open_accounts["tom"], 20.10)
    print(internal_open_accounts)

evaluate()