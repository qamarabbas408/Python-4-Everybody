def calculation():
    while True:
        inputNumbers=input("Enter Number: ")
        if inputNumbers =='stop' or inputNumbers== '': break
        value=float(inputNumbers)
        numList.append(value)
    return numList
        
def average(numList):
    try:
        average=float(sum(numList)/len(numList))
        print("Average of Numbers is: ",average)
    except:
        print("Application Closed")
        
numList=list()
numList=calculation()
average(numList)
    