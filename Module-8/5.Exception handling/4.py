#  Write a Python program to handle file exceptions and use the finally block for closing 
# the file. 
try:
    f=open("four.txt",'r')
except FileNotFoundError:
    print("not found")
else:
    print("open!")
finally:
    try:
        f.close()
    except NameError:
        print(" file is not close!")
