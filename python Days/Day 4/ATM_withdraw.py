#Exercise 4 ATM withdraw system.

balance=15000

withdraw_amt=int(input("Enter withdraw amount:"))

if withdraw_amt>=0:
    if withdraw_amt<=balance:
        if withdraw_amt % 100 == 0:
            T_bal=balance-withdraw_amt
            print("Withdraw amount is:",withdraw_amt)
            print("Total balance is:",T_bal)
        else:
            print("Enter a valid amount in multiple of 100.")
    else:
        print("Insuficient Balance.")
else:
    print("Invalid input Don't use Negative numbers.")