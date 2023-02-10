# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence

# filename='data.txt'
sum=0
count=0
filename=input('Enter a file Name: ')
try:
    fhand=open('dataFiles/%s'%filename)
    for line in fhand:
        line=line.rstrip()
        if line.startswith('X-DSPAM-C'):
            startIndex=line.find('0')
            startIndex=float(line[startIndex:])
            sum=startIndex+sum
            count=count+1
    print('Total Spam Confidence: ',sum)
    print('No of Spam Confidence Alerts:',count)
    print('Average Spam Confidence: ',sum/count)
except:
    print("File Not Found")
