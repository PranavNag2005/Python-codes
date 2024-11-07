balance=int(input("enter your balance "))
amount=int(input("enter the amount to withdrawal "))

if amount>balance:
    print("Insufficient funds ")
if amount<=0:
    print("enter the valid amount")

else:
    balance-=amount
    print(balance)