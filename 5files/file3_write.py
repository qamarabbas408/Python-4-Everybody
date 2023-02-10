path='files/'
filename='writeFile.txt'

##write a file 
# fout=open('files/writeFile.txt','w') #this will create a file if not exists but if exists overwrites the content
# print(fout)

##writing some data into file
data="From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
data2='From qmarabbas715@gmail.com'
fout=open('%s%s'%(path,filename),'w') 
fout.write(data) #writes content in the file if invoked again data is added to the end
fout.write(data2) #writes content in the file
#close the file so that last bit of data is physicaly written to the disk.
# This step is optional because python automaticaly closses the file at the end of programs
fout.close() 

##debuging
s = '1 2\t 3\n 4' #what if we have data of such sorts 
print(s) #this will treat special characters as escape sequences 
#but in real proggrams we want to display data as it is, we use repr() function
print(repr(s))
