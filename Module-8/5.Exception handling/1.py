# Write a Python program to handle exceptions in a simple calculator (division by zero, invalid 
# # input). 

def calcutor(num1,num2):
    try:
        return f"The diviosn is :{num1//num2}"
    except ZeroDivisionError:
        return f"The denominator can't be zero"

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
print(calcutor(num1,num2))
