# class A:
#     def __init__(self,name):
#         self.name=name
#     def m1(self):
#         print(self.name)
# class B:
#     def __init__(self,page):
#         #super().__init__(name)
#         self.age=age
#     def m2(self):
#         #print(self.name)
#         #super().m1()
#         print(self.age)
#
# class C(A,B):
#     def __init__(self,name,age,marks):
#         super().__init__(name)
#         self.age=age
#         self.marks=marks
#     def m3(self):
#         super().m1()
#         print(self.age)
#         print(self.marks)
#
# obj1=C('apple',20,50)
# obj1.m3()

## Data encapsulation means restricting the access to the variables and the methods in side the class
# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#         print(f"You have sucessfully deposited {amount}")
#     def __withdraw(self,amount):
#         if self.__balance>amount:
#             self.__balance-=amount
#             print(f"you withdraw amount was{amount}")
#     def get_balance(self):
#         print(f"your total balance amount is {self.__balance}")
#     def withdraw_amount(self,amount):
#         self.__withdraw(amount)
# obj=BankAccount('abc',2000)
# obj.get_balance()
# obj.deposit(1000)
# obj.get_balance()
# obj.withdraw_amount(1000)
# obj.get_balance()

## Decorator

# def decor(func):
#     def inner(a,b):
#         if b==0:
#             print(f"please enter some other value for B  Apart from {b}")
#         else:
#             func(a,b)
#     return inner
# @decor
# def f1(a,b):
#     print(a/b)
# f1(4,2)
# f1(4,0)



# def decor(func):
#     def inner(S):
#         if S.isupper():
#             print(S.lower())
#         else:
#             func(S)
#     return inner
# @decor
# def f1(S):
#     print(S.upper())
# f1('apple')
# f1('APPLE')

# S='1-4,4-4,8-13'
# L=[]
# b=S.split(",")
# for i in b:
#     c=i.split('-')
#     for j in range(int(c[0]),int(c[1])+1):
#         if j not in L:
#             L.append(j)
# print(L) ## [1, 2, 3, 4, 8, 9, 10, 11, 12, 13]
#

'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def check_balance(self):
        pass

class BankAccount(A):
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print(f"You have sucessfully deposited {amount}")
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=amount
            print(f"you withdraw amount was{amount}")
    def check_balance(self):
        print(f"your total balance amount is {self.__balance}")
obj=BankAccount('abc',2000)
obj.deposit(1000)
obj.withdraw(100)
obj.check_balance()
'''
from encodings.punycode import selective_find

from selenium.webdriver.common.devtools.v134.debugger import resume

'''
s='1234567891'
b=sum(int(i) for i in s)
print(b)
while b>9:
    b=sum(int(j) for j in str(b))
print(b)
'''
###Itterator :-

'''
class FibonacciGenerator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b  # Move to the next number
        return result

# Usage example
fib = FibonacciGenerator()
for _ in range(10):  # Generating the first 10 Fibonacci numbers
    print(next(fib))

'''

## Generator :- we can write generator like a normal function but here we use yield keyword instead of return
## it's main advantages is using  less memory as yield keyword hold only one value
## when we need to handle the large set of data we will go for generator
## if we want to get the values we use next()
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
#  a=fib()
#  for i in range(10):
#      print(next(a))
# import sys
# L=[i for i in range(100000)]
# gen=(i for i in range(100000))
# print(type(L))
# print(type(gen))
# print(sys.getsizeof(L))
# print(sys.getsizeof(gen))


#It helps access elements one at a time from an iterable object using next().
# class A:
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         a=self.a
#         self.a,self.b=self.b,self.a+self.b
#         return a
# obj=A()
# for i in range(10):
#     print(next(obj))
#
# class B():
#     def __init__(self):
#         self.a=2
#     def __iter__(self):
#         return self
#     def __next__(self):
#         result=self.a
#         self.a+=2
#         return result
# obj=B()
# for i in range(10):
#     print(next(obj))

S='1234567899999'
b=sum([int(i) for i in S])
print(b)
while b>9:
    b = sum([int(j) for j in str(b)])
print(b)

