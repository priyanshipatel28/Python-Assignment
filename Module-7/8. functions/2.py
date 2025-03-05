# Write a Python program to create a calculator using functions. 
def calculator(n):
    if n in [1,2,3,4,5,6]:
        num1 = int(input("num1:"))
        num2 = int(input("num2:"))
        if n==1: 
            return f"add : {num1+num2}"
        elif n==2:
            return f"sub : {num1-num2}"
        elif n==3:
            if num2!=0:
                return f"div : {num1//num2}"
            else:
                return "Enter valid denomenator"
        elif n==4:
            return f"mul : {num1*num2}"
        elif n==5:
            return f"mol : {num2%num1}" # the result will be remainder
        else:
            return f"pow : {num1**num2}"
    else:
        return "invalid choice"



choice = int(input("Enter your choice:\n1=add\n2=sub\n3=div\n4=mul\n5=mol\n6=power\n-->"))
print(calculator(choice))
