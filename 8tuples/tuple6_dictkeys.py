##composite keys
#creating a composite key(tuples) in dictionary and assinging it a value
#e.g. assigning phone number to first and last name of a single person
firstName='Qamar'
lastName='Abbas'
number=588908
dictNames=dict()
dictNames[firstName,lastName]=number
for firstName,lastName in dictNames:
    print(firstName,lastName,' has ', dictNames[firstName,lastName])

##list comprehension
list_of_int_in_strings=['20','550','10','220']
list_of_int=list()
for number in list_of_int_in_strings:
    list_of_int.append(int(number)) #converts items of each list into integer
print(sum(list_of_int))
#restructuring same program using list comprehension (more compact manner)
list_of_int_in_strings=['20','550','10','220']
list_of_int=[int(number) for number in list_of_int_in_strings]
print(sum(list_of_int))
