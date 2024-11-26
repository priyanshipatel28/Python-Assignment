#  Practical Example 1: How does the Python code structure work? 
name = "steven"  # Name variable

a = 20           # First number
b = 10           # Second number

add = a + b      # Addition
print(add)       # Print result

# Loop 
for i in range(1, 10):  
    if i % 2 == 0:       # Check even
        print("Even")    
    else:
        print("Odd ")  


# loop( start,stop,step)
for i in range(10,0,-1):
    print(i,end=" ")


# Division input(conditional)
numerator = int(input("Enter the numerator num: "))  
denominator = int(input("Enter the denominator num: ")) 

if numerator >= 0 and denominator != 0:  
    print("Division possible")          
else:
    print("Division is not possible")    


# Add two numbers(typecasting)
fnum = input("Enter the value of fname: ")     # First input
fnum2 = input("Enter the value of fnum2: ")    # Second input
result = int(fnum) + int(fnum2)  # Convert and add
print(result)  # Print result
