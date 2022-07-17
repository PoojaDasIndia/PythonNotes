import pdb
class BalanceExceptionError(Exception):
    pass

pdb.set_trace()
def bank_balance():
    Total_Money = 10000
    withdraw = 9000
    try:
        balance = Total_Money - withdraw
        if balance <= 2000:
            raise BalanceExceptionError("Insufficient Balance")
        print(balance)

    except BalanceExceptionError as be:
        print(be)


bank_balance()
