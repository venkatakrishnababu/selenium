## using for and if condition
S='ind@ter@@#j'
# b=[S[i] for i in range(0,len(S)) if S[i].isalpha()][::-1]
# c=[b.insert(i,S[i]) for i in range(0,len(S)) if not S[i].isalnum()]
# print(''.join(b))

##using for and if else condition
# L=[1, 2, 3, 10, 11, 12, 20, 25, 26, 27, 40]
# L1=[]
# for i in range(0,len(L)+1):
#     if L[i]-L[i-1]==1:
#         L1.append(L[i])
#     else:
#         if len(L1)>0:
#             print(L1)
#         L1=[L[i]]
# print(L1)

# b=[(i,"even") if i%2==0 and i>1 else (i,"odd") for i in range(0,51)]
# print(b)


### using two for loops with if condition

# for i in range(2,50):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,'',end='')

## Vowels
# S='Hello World'
# L=[i for i in S if i in 'AEIOUaeiou']
# print(L)

# Given two lists ["A", "B", "C"] and [1, 2, 3], use list comprehension to generate pairs (A,1), (B,2), (C,3).
# L=["A", "B", "C"]
# L1=[1, 2, 3]
# L2=[(L[i],L1[i]) for i in range(0,len(L))]
# print(L2)


# Given a nested list [[1, 2], [3, 4], [5, 6]], use list comprehension to flatten it into [1, 2, 3, 4, 5, 6].
# L=[[1, 2], [3, 4], [5, 6]]
# L2=[j for i in L for j in i]
# print(L2)

# Given two lists [1, 2, 3, 4, 5] and [4, 5, 6, 7, 8], use list comprehension to find common elements.
# L1=[1,2,3,4,5]
# L2=[4,5,6,7,8]
# L3=[i for i in L1 if i in L2]
# print(L3)

#Given a string "Python is fun", use list comprehension to reverse each word individually.
# S="Python is fun"
# L1=[i[::-1] for i in S.split()]
# print(L1)