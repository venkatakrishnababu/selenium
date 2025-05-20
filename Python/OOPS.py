### Single inher
# class A:
#     clg = 'vignan' # class or static variable
#     def __init__(self,name,age): # variables provided after self are instance variable
#         self.name=name
#         self.age=age
#     def m1(self):
#         print(self.name,self.age)
# obj=A('abc',28)
# obj.m1()
# class B(A):
#     def __init__(self,name,age,roll):
#         A.__init__(self,name,age)
#         self.roll=roll
#     def m2(self):
#         print(self.name,self.age,self.roll,B.clg)
# obj1=B('abcd',23,1234)
# obj1.m2()

#using super
'''
class A:
    clg = 'vignan' # class or static variable
    def __init__(self,name,age): # variables provided after self are instance variable
        self.name=name
        self.age=age
    def m1(self):
        print(self.name,self.age)
class B(A):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll=roll
    def m2(self):
        super().m1()
        print(self.roll,B.clg)
obj1=B('abcd',23,1234)
obj1.m2()
'''
from symtable import Class
from xml.dom.minicompat import EmptyNodeList

from pyexpat.errors import messages


##### Multiple inheritance
# class C:
#     def __init__(self,name):
#         self.name=name
#     def m1(self):
#         print(self.name)
# class D:
#     def __init__(self,age):
#         self.age=age
#     def m2(self):
#         print(self.age)
# class E(C,D):
#     def __init__(self,name,age,roll):
#         D.__init__(self,age)
#         super().__init__(name)
#         self.roll=roll
#     def m3(self):
#         super().m1()
#         print(self.age,self.roll)
# obj=E('red',23,1234)
# obj.m3()
############# Multi level inheritance

# class F:
#     def __init__(self,name):
#          self.name=name
#     def m1(self):
#         print(self.name)
# class G(F):
#     def __init__(self,age):
#          self.age=age
#     def m1(self):
#         print(self.age)
# class C:
#     def __init__(self,name):
#          self.name=name
#     def m1(self):
#         print(self.name)

### Data encapsulation ( Restricting the access to the variables and the methods)
# class emp:
#     def __init__(self,name,salary):
#         self.__name=name
#         self.__salary=salary
#     def get_name_salary(self):
#         return (self.__name,self.__salary)
# obj=emp('abcd',58000)
# print(obj.get_name_salary())


# class Bankaccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print("New balance after deposit:", self.__balance)
#
#     def __withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"withdraw amount : {amount} , Remaining balance after withdraw:", self.__balance)
#         else:
#             print("Insufficient funds")
#
#     def perform_withdraw(self, amount):
#         self.__withdraw(amount)
#
#     def __get_balance(self):
#         print("Current balance:", self.__balance)
# obj = Bankaccount("abc", 2000)
# obj.deposit(3000)
# obj._Bankaccount__get_balance()
# obj._Bankaccount__withdraw(1000)
# obj.perform_withdraw(1000)

## decorator
#Adding an extra functionality to the function or method without modifying the existing functionality

# def decor(func):
#     def inner(name):
#         if name.isupper():
#             print(name.lower())
#         else:
#             func(name)
#     return inner
# @decor
# def UL(name):
#     print(name.upper())
# UL('abc')
# UL('ABC')
#
# def dec(func):
#     def inner(x,y):
#         try:
#             return (func(x,y))
#         except ZeroDivisionError:
#             print('error:y is zero , make sure y>0')
#     return inner
# @dec
# def div(x,y):
#     print(x/y)
# div(4,2)
# div(4,0)

#polymorphism
# class A:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __mul__(self, other):
#         return self.salary*other.days
# class B:
#     def __init__(self,name,days):
#         self.name=name
#         self.days=days
#     def __mul__(self, other):
#         return self.days * other.salary
# obj=A('abc',2000)
# obj1=B('a',23)
# print(obj*obj1)
# print(obj1*obj)

# class emp:
#     def salary(self):
#         pass
# class FT(emp):
#     def salary(self):
#         print('FT')
# class CS(emp):
#     def salary(self):
#         print('CS')
# #de
# def c_salary(Emp :emp):
#     Emp.salary()
# a=FT()
# b=CS()
# c=[a,b]
# for i in C:
#     c_salary()

# class Note():
#     def message(self):
#         pass
# class email(Note):
#     def message(self):
#         print('Notified through email')
# class popup(Note):
#     def message(self):
#         print('Notified through popup')
# class text(Note):
#     def message(self):
#         print('notified through text')
# #par
# def sent_Notf(notes :Note):
#     notes.message()
# obj1=email()
# obj2=popup()
# obj3=text()
# L=[obj1,obj2,obj3]
# for i in L:
#     sent_Notf(i)

#method overriding

# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def m1(self):
#         print(self.name,self.age)
# obj1=A('abc',24)
# obj1.m1()
# class B(A):
#     def __init__(self,name,gender):
#         super().__init__(name,None)
#         self.gender=gender
#     def m1(self):
#         print(self.name,self.gender)
# obj=B('abc','M')
# obj.m1()

# class A():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def m1(self):
#         print(self.name)
#     def __m1(self):
#         print(self.age)
# obj1=A('abc',23)
# obj1._A__m1()


# DATA abstraction
# Showing the data what ever required to the enduser and Hidding the data
# which is not required to the end user

# from abc import ABC,abstractmethod
# class Bank_Account(ABC):
#     @abstractmethod
#     def deposit(self):
#         pass
#     @abstractmethod
#     def withdraw(self):
#         pass
#     @abstractmethod
#     def check_balance(self):
#         pass
# class SA(Bank_Account):
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         if self.balance>0:
#             self.balance+=amount
#     def withdraw(self,amount):
#         if self.balance>amount:
#             self.balance -=amount
#             print(f"withdraw {amount} is sucessfull")
#         else:
#             print('insufficent funds')
#     def check_balance(self):
#         print(self.balance)
# obj=SA('abc',300)
# obj.check_balance()
# obj.withdraw(100)
# obj.deposit(2000)
# obj.check_balance()

### Class method
# A class method allows us to access and modify variables with in the class
# Additionally, the first parameter of a class method is always cls
# and it is decorated with @classmethod

class IT:
    Company = 'Msys'
    def __init__(self,name,exp):
        self.name=name
        self.exp=exp
    @classmethod
    def C(cls,Company_name):
        cls.Company=Company_name
    def det(self):
        print(self.name,self.exp,self.Company)
obj=IT('ABC',3)
obj.det()
obj.C('Nutanix')
obj.det()

## static method
# Static method is decorated with @staticmethod
# It is defined inside inside the class
# The operations doesn't depend on class varaibles and instance variables

# class Operations:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def mul1(self):
#         return self.mul(self.a,self.b)
#     @staticmethod
#     def mul(a,b):
#         print(a*b)
# obj=Operations(2,3)
# obj.mul1()

