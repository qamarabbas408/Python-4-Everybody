def userDefineFunction():
    print("i am here")

def anotherUserDefinedFn():
    userDefineFunction()
    print('but i have my own body')

print(userDefineFunction)
userDefineFunction()

anotherUserDefinedFn()

def addTwo(a,b):
    sum = a+b
    return sum

sum=addTwo(2,3)
print(sum)