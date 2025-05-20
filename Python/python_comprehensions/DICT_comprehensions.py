# L=[1, 2, 3, 4, 5]
# d={i:i**2 for i in L}
# print(d)
from contextlib import chdir

#------------------------------------------

# d={'a': 1, 'b': 2, 'c': 3}
# d1={i[1]:i[0] for i in d.items()}
# print(d1)


#---------------------------------------
# d={1: 10, 2: 15, 3: 20, 4: 25, 5: 30}
# d1={i[0]:i[1] for i in d.items() if i[1]%2==0}
# print(d1)

#---------------------------------------------

# S="dictionary"
# d={}
# for i in S:
#     b=S.count(i)
#     d[i]=b
# print(d)
# d1={i:S.count(i) for i in S}
# print(d1)

#-----------------------------------------------------------
# d={ 'A': 5, 'B': -3, 'C': 10, 'D': -8 }
# d1={i:j for i,j in d.items() if j>0}
# print(d1)

##
# L=["apple", "banana", "cherry"]
# d={i:len(i) for i in L }
# print(d)

##
# print(ord('a'))
# print(ord('z'))
# d={chr(i):i for i in range(ord('a'),ord('z')+1)}
# print(d)

##

# L=[1, 2, 3, 4, 5]
# L1=[4, 5, 6, 7, 8]
# d={i:i**2 for i in L if i in L1}
# print(d)

##
L=[1,2,3,4,5]
def fact(n):
    if n==0 or n==1:
        return n
    else:
        return n*fact(n-1)
d={i:fact(i) for i in L}
print(d)
print(d.get(3))
d.update({'122':'122'})
print(d)
# d.pop('122')
# print(d)
d.popitem()
print(d)
d.setdefault('sp','ps')
print(d)