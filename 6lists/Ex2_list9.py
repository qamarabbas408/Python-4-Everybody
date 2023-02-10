#use a as a refrence to l thus no need to retrun any thing
def chop(l):
    del l[0]
    last=len(l)-1
    del l[last]
    return None #this is by default no need to write it explicitly

a=[1,2,3,4,5,6,7]
chop(a)
print(a)

#explicity returned new list from the function
def middle(l):
    del l[0]
    last=len(l)-1
    del l[last]
    return l
b=middle(a)
print(b)
