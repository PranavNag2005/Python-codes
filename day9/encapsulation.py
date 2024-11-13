# It is a fundamental object oreiented principle
#  in python it protects your classes from 
# accidental changes or deletion and promotes 
# code reusabulity and maintainability.
#Binding of classes,function members into a single
#  unit is called as encapsulation

# class smartphone:
#     def __init__(self,brand,os) -> None:
#         self.brand=brand
#         self.os=os
# samsung=smartphone("Samsung","android")
# print(samsung.brand)


class bank:
    def __init__(self,accno,accholder,balance=0) -> None:
        self.accno=accno
        self.accholder=accholder
        self.balance=balance

    def getbalance(self):
        print("---------------")
        print(f"{self.balance}") 
        print("---------------")
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("----------------------------")
            print(f"Deposited amount: {amount}")
            print(f"remaining balance: {self.balance}")
            print("---------------------------")

        else:
            print("not a valid amount")
    def withdrawal(self,amount):
        if amount<0:
            print("amount must be positive ")
        if amount>0 and amount<=self.balance:
            self.balance-=amount
            print(" ---------------------------------")
            print(f"withdrawal amount: {amount}     ")
            print(f"Remaining amount: {self.balance}")
            print(" --------------------------------")
        else:
            print("insufficient funds ")

b=bank('ABCDEFGH1234','Pranav')
print(b.getbalance())

b.deposit(100000)
b.withdrawal(100000000000)