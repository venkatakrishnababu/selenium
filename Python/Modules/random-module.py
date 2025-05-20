import random
print(random.randint(2,22)) # Returns a random integer between a and b
print(random.uniform(2,22)) # Returns a random Floating number between a and b
L=[1,12,14,21,34,45,85]
print(random.choice(L)) ## Return the random number from the list
print(L)
random.shuffle(L) ## It will shuffle the list randomly
print(L)
