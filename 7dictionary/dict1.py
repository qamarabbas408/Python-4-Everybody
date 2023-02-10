##dictionay 
#it is same as list but its index (keys) are almost of any type unlike integer indices in lisst
#it is a mapping between keys and values
eng2urd=dict() #the function dic() creates a new empty dictionary
print(eng2urd)
#adding items to dictionary
eng2urd['one']='ayeak'
# print(eng2urd)
eng2urd={'two':'do','three':'teein','four':'chaar','five':'panch'} #new dictionary from the one created earlier
#the order of key-values pairs is  unpredictable b/c it doesn't matter--you have indexed values using keys
print(eng2urd)
print(eng2urd['three'])
print(len(eng2urd))
print('two'in eng2urd) #T
print('do' in eng2urd) #F because values are not enough for in operator to show the result
#above problems solution
val=list(eng2urd.values()) #convert dict() to list() using values()  method
print('do' in val)
print(type(eng2urd))