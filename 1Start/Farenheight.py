inp=input("Enter temprature in Fareneight\t")
try:
    inp=float(inp)
    Celcius=(inp-32)*5.0/9.0
    print(Celcius)
except:
    print("Enter a Valid Number")

