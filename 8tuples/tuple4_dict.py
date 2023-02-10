##tuple and dictionaries
#items() a dictionary method returns a tuple (key,value)
eng2urd={'one':'ayeak','two':'do','three':'teein','four':'chaar','five':'panch'} 
t=list(eng2urd.items()) ##items() return dict values in key-value tuples
print(t) #list of tuples items order is unpredictable
#sorting tuple list
t.sort()
print(t)
#another example
math2urd={1:'ayeak',2:'do',4:'chaar',0:'jekganush'}
t=list(math2urd.items())  
t.sort() #list is sorted by asecending ordery by key value
print(t)

##multiple assignments with dictionaries
#for loop has two iteration variables, the dict is converted in a list of tuples 
#tuples are assigned to iteration variable key and val
for key, val in list(eng2urd.items()): 
    print(val,' --> ',key)

##sorting by dictinory values ..in previous exercise we sorted dictionary by key 
d = {'a':10, 'b':1, 'c':22}
print(d)
l=list()
for key,val in list(d.items()):
    l.append((val,key))
print(l)
l.sort(reverse=True)
print(l)
