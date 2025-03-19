file=open('sample.txt','r')
print(file.read())
file.close()


file=open('sample.txt','r')
print("\n Reading few characters on the paragraph abot the Rivers....")
print(file.read(11))
print(file.read(16))
print(file.read(10))
file.close()