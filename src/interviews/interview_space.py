from functools import singledispatch
from venv import create
import uuid

"""
params: name, balance (o)
"""
@singledispatch
def create_basic_account(value):
    raise NotImplementedError("Unsupported param arrangement")

@create_basic_account.register
def create_basic_account(name):
    return {
        "id": uuid.uuid4(),
        "name": name,
        "balance": 0.0,
        "transaction_history": {}
    }

@create_basic_account.register
def create_basic_account(name, balance):
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


def evaluate():
    new_account = create_basic_account("tom")
    transfer_account = create_basic_account("jerry", 100.20)

    updated_from, updated_to = transfer_account(new_account, transfer_account, 20.10)
    updated_from, updated_to = transfer_account(transfer_account, new_account, 20.10)


    print("hello")

evaluate()