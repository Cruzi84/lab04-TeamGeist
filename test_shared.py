def test_initial_balance(funded_account):
    assert funded_account.balance == 1000


def test_account_balance_after_multiple_operations(funded_account):
    funded_account.deposit(500)
    funded_account.withdraw(200)
    assert funded_account.balance == 1300