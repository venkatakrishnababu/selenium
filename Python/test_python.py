#functions
#if a group of statments which are repteadly required
# Then it is not good write those statements every time
# we need define the it as a function and class that function based on requirement
# Recursive function
'''
def fact(n):
    if n==1 or n==0:
        return n
    else:
        return n*fact(n-1)
print(fact(5))
'''
# lambda function
#by using this function the redablity of programm will increasee
# lambda inputargument:returnexpression
'''
L=[1,2,3,4]
b=lambda n:n%2==0
for i in L:
    if b(i)==True:
        print(i)
'''
#local variable :- defined inside the function
#global variable :- defined outside the function
#Modifying the global variable
'''
b=10
def f():
    global b
    b=13
    a=12
    print(a)
def f1():
    print(b)
f()
f1()
'''
##Bulit in functions
#Map-->Map is used to apply the function on the iteerable object
#map(function,iter1,iter2_________,itern)
'''
a=[1,2,3,4]
b=[5,6,7,8]
def c(a,b):
    return a+b
print(list(map(c,a,b)))
print(list(map(lambda a,b:a+b,a,b)))
'''
#filter-->It is used to extract the unwanted elements from the iterable object
#filter(function,iter1)
'''
L=[2,3,6,8,7,12]
def f(a):
    if a%2==0:
        return(a)
print(list(filter(f,L)))
print(list(filter(lambda n:n%2==0,L)))
'''
#Zip
#The zip() function in Python is used to combine two or more iterables (e.g., lists, tuples, etc.) element-wise,
# creating a new iterable of tuples
'''
L=[1,2,3]
L1=(1,2)
print(list(zip(L,L1)))
'''
#enumarate is used to iterate over an iterable objects
# it will keep track of index postion enumarate(iterableobject,start=0)
'''
L=['a','b','c']
print(list(enumerate(L,start=0)))
'''
# test_example.py
def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 5 - 2 == 3
