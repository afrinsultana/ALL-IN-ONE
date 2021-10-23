"""
Syntax to open file
file_Object=open("File name","mode")
'r'- Read mode
'w'-Write mode
'a'- append mode
'r+'- read/write mode
 open+read/write+ close
"""

# open a file for write mode
file=open("pyBatch6.txt","w")

file.write("Hello World !")
file.write("This is our text file")
file.write("And this is another line")
file.write("This is write mode")

file.write("\nHello World !\n")
file.write("This is our text file\n")
file.write("And this is another line\n")
file.write("This is write mode\n")

file.close()


# open a file for read mode
file=open("pyBatch6.txt","r")
# Read entire file
# print(file.read())
# print(file.read(16)) #  Read 16 digit character
# print(file.readline())# read a single line
print(file.readlines())# read a multiple lines
file.close()

file=open("pyBatch6.txt","r")
s=file.readlines()
for line in s:
    print(line)
file.close()

file=open("pyBatch6.txt","r")
for line in file:
    print(line)
file.close()

file=open("pyBatch6.txt","a")
file.write("we meet again \n")
file.write("Python is awesome !\n")

file.close()
i=1

file=open("pyBatch6.txt","r")
for line in file:
    print(i,'.',line)
    i=i+1
file.close()

