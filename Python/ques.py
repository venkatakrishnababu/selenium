# find largest number in the list
'''
L=[222222,333333,555555,7777777,8888888,9999999]
for i in range(0,len(L)):
    if L[0]<L[i]:
        L[0]=L[i]
print(f'The largest number in the list:{L} is ',L[0])
'''
from pickle import LONG1

'''
# add the numbers till number becomes single digit
s='123456'
for i in range(0,len(s)):
    L=sum([int(i) for i in s])
    if L<10:
        print(L)
        break
    else:
        s=str(L)
'''
'''
# print cons and non-cons numbers in the list
L=[2,4,5,7,8,9,11,13,14,15]
L1=[]
for i in range(0,len(L)):
    if L[i]-L[i-1]==1:
        L1.append(L[i])
    else:
        if len(L1)>0:
            print(L1)
        L1=[L[i]]
print(L1)
'''
'''
#flat the given list
L=[[1,2],[3],[7,8,[9]]]
L1=[j for i in L for j in i]
L2 = [int(str(i[0])) if type(i)==list else i for i in L1]
print(L2)
'''
## reverse a string and make sure should be in the same place
# S='ind@ter@@j'
# S1=''
# for i in range(0,len(S)):
#     if S[i].isalpha():
#         S1=S[i]+S1
# for i in range(0,len(S)):
#     if S[i]=='@':
#         S1=S1[:i]+'@'+S1[i:]
# print(S1)


# L=[1,4,5,8,10]
# L1=L
# print('before Append L1:',L1)
# print('before Append L:',L)
# L.append(11)
# print('After Append L1:',L1)
# print('After Append L:',L)

# L2=[1,4,5,8,10]
# L3=L2.copy()
# print('before Append L2:',L2)
# print('before Append L3:',L3)
# L2.append(11)
# print('After Append L2:',L2)
# print('After Append L3:',L3)

#
# s='appLE12'
# S1=''
# for i in s:
#     if i.isupper():
#         b=i.lower()
#         S1+=b
#     elif i.lower():
#         S1+=i.upper()
# print(S1)


# s='12345677767676767677676767676'
# b=sum(int(i) for i in s)
# while len(str(b))!=1:
#     b=sum(int(i) for i in str(b))
# print(b)

# d= {
#     11: "one",
#     21: "two",
#     32: "three",
#     14: "four",
#     51: "five",
#     6: "six",
#     7111111: "seven",
#     18: "eight",
#     911: "nine",
#     1110: "ten"
# }
# L=[]
# for i,j in d.items():
#     L.append(i)
#     L.sort()
# for i,j in d.items():
#     if L[-1] == i:
#         print(j)
# d1=(max(d.keys()))
# print(d[d1])

# print cons and non-cons numbers in the list
# L=[3,4,5,7,8,9,11,13,14,15]
# L1=[]
# for i in range(0,len(L)):
#     if L[i]-L[i-1]==1:
#         L1.append(L[i])
#     else:
#         if len(L1)>0:
#             print(L1)
#         L1=[L[i]]
# print(L1)

# d={1:'abc',2:'def'}
# b=list(d.keys())
# c=list(d.values())
# d[b[0]],d[b[1]]=c[1],c[0]
# print(d)
#
# d = {1: 'abc', 2: 'def'}
# #print(d[1])
# # d[1],d[2]=d[2],d[1]
# # print(d)
# d = {1: 'abc', 2: 'def'}
# print([*d][:2])
#


# L=['Prabhu', 'Rahul', 'Arunesh', 'Sonali', 'Rakshit']
# b=sorted(L,key=lambda x:x[-1])
# print(b)

L=[22,333333,555555,77,8888888,9999999]
for i in range(0,len(L)):
    if L[0]<L[i]:
        L[0]=L[i]
        print(L)
print(L[0])