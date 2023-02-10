#part1
x=6
y=2
x>=y and (x/y)>2 

#part2
x=1
y=0
x>=2 and (x/y)>2 #if first condition if false then 2nd is automaticaly considered false called short-circuiting

#part3
x=6
y=0
#comment below line when compiling
#x >=2 and (x/y)>2 #throw a runtime error because first condition is true thus evaluate 2nd which cuase runtime

#solution to part3 and part2 called guardian evaluation
x=6
y=0 
x>2 and y!=0  and  (x/y)>2 #the 3rd condition is guardian evaluation placed before the term that can cause runtime

x=1
y=0
x>=2 and y!=0 and(x/y)>2
