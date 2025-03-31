# Write a Python program to read the contents of a file and print them on the console. 
try:
    f= open("one.txt",'r')
    content = f.read()
    print(content)
except Exception as e:
    print("the error is :",e)
