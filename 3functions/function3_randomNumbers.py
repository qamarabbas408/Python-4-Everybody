from math import ceil
import random
for i in range(10):
    x=random.random() #returns numbers between 0.0 and 1.0 including 0.0 but not 1.0
    print(x)
    print(round(x))
    print(ceil(x))
print(dir(x))
print(x)
print(random.randint(5,10)) #returns a single random number between low and high returns in b.w low and high includeing them 

numbers=[2,5,6]
print(random.choice(numbers)) #returns a random number belonging to numbers varaible