class Bank_Account:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def __withdraw(self,amount):
        if 0<amount<self.__balance:
            self.__balance-=amount
    def get_balance(self):
        print(self.__balance)
    def get_withdraw(self,amount):
        if 0<amount<self.__balance:
            self.__balance-=amount

obj=Bank_Account("abc",203)
obj.get_balance()
obj.deposit(203)
obj.get_balance()
obj._Bank_Account__withdraw(103)
obj.get_balance()
obj.get_withdraw(103)
obj.get_balance()

def decor(func):
    def inner(a,b):
        if b==0:
            print('zero division error')
        else:
            func(a,b)
    return inner
@decor
def f(a,b):
    print(a/b)
f(2,3)
f(2,0)