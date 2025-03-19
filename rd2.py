file=open('sample.txt','r')
print(file.read())
file.close()

filew=open('sample.txt','w')
filew.write("\n i am using operations on a file....")
print("\n")
filew.close()

filea=open('sample.txt','a')
filea.write("\n i am working on the new module called as file handling....")
print("\n")
filea.close()


file=open('sample.txt','r')
print(file.readlines())
file.close()

