##tuple assingment
somelist=['laptop','accer']
#here left side of assignment operator is a tuple. Python automaticaly assigns first item to first and 2nd 2dn
#no of variables on left nd numbers of values on right must be same
x,y=somelist
print(x)
print(y)
#or 
somelist=['laptop','accer']
(x,y)=somelist
print(x)
print(y)
#breaking a string into two variables
emailId='qmarabbas715@gmail.com'
username,domain=emailId.split('@') #split() returns a list of two elements 
print(username,domain)

##swape values 
(x,y)=(y,x) #swap values
print(x)
print(y)
