#while
n=10
while n>0:
    print(n)
    n=n-1

#for
names=['ab','sdf','sfdf','sdfdsfe']
for  name in names:
    print('names are ',name)
print("application close")


# #infinite-loop
# n=10
# while True:
#     print(n,end='')
#     n=n-1
# print('Done!')

# #break statement in infinite loop
# while True:
#     line=input('>')
#     if(line=='close'):
#         break
#     print(line)
# print('Application Closed')

# #continue statement
while True:
    line=input('> ')
    if line[0]=='#':
        continue
    if line =='close':
        break
    print(line)
print("application close")