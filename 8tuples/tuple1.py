##tuple
#they are immutable. indices are of integers and values of any data type can be stored
t1='a','b','c'
#or
t2=('a','b','c')
print(type(t1))
print(t1)
#
t3=('zzz') #without comma python treats this expression as a string 
print(type(t3)) 
#tuple()
t4=tuple() #creates an empty tuple
print(t4)
t5=tuple('computerscience') #single string/list/tuple is changed into tuples
print(t5)
print(t5[0])
print(t5[0:4])
# t5[0]='A' throw error because tuples are immutable 

##tuples elements cant be modified but can be replaced
t6=('a','b','c')
t6=('A',)+t6[1:] #here small a is replaced with capital A tuple () indicates its a tuple
print(t6)

##comparisons
##comparison starts with first element of each sequence, if they are equal comparision moves to next element 
# and so on and until it finds elements that differ subsequent numbers are ignored no matter how large they are
t1=(1,2,3)
t2=(1,200,3)
t3=(0,0,1)
print(t1<t2)  #True
print(t1<t3)   #False
