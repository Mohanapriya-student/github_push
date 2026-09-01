#open()
file=open("hello.txt",'r')
content=(file.read())
print(content)

#close()
file=open("hello.txt")
content=(file.close())
print(content)

#write
file=open("hello.txt",'w')
file.write("hello, this is file handling")
file.close()

#append
file=open("hello.txt",'a')
file.write("end=/n","this line is added")
file.close()
