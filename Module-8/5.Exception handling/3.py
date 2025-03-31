# Write a Python program to handle multiple exceptions (e.g., file not found, division by zero). 
try:
    num1=int(input("Enter num1:"))
    num2=int(input("Enter num2:"))
    result = num1//num2
    print("div:",result)
    try:
        f=open("one.txt",'r')
        print("done")
        f.close()
    except FileNotFoundError:
        print("not fouond")
    # except FileExistsError:
    #     print("already exist")

except Exception as e:
    print("Error :",e)
    
finally:
    print("thank you!")