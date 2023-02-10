inputNumbers=list()
while True:
    inp=input('Enter numbers: ')
    if inp == 'stop' or inp=='close' or inp==' ':break
    inputNumbers.append(float(inp))

print(max(inputNumbers))
print(min(inputNumbers))