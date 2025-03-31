# Write a Python program to demonstrate handling multiple exceptions. 

try:
    f=open("one.txt",'r')
    try:
        f=open("three.txt",'x')
    except FileExistsError:
        print("already exist")
    finally:
        print("bye")

except FileNotFoundError:
    print("not found")

finally:
    print("bye!")
