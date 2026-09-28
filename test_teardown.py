import pytest
from bank import BankAccount


@pytest.fixture
def account():
    account = BankAccount(100)
    print("[setup]")
    yield account
    print("[teardown]")


def test_deposit(account):
    account.deposit(50)
    assert account.balance == 150


def test_withdraw(account):
    account.withdraw(30)
    assert account.balance == 70