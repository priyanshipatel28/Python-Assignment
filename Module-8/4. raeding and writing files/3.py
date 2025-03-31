#  Write a Python program to read a file and print the data on the console.

f = open("two.txt",'r')
# content = f.readlines() File pointer moves to the end., means after using readlines , i don't have to use other
# content1 = f.read()
content = f.readline()#File pointer moves to the next line after each call., it will go to next line so after readline, i can use read() and readlines() both..
content1 = f.read()
print(content)
print(content1)
f.close()