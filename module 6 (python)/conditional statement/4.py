# Practical Example 8: Write a Python program to check if a person is eligible to donate blood 
# using a nested if. 

age = int(input("Enter your age: "))

if age>=18 and age<60:
    weight = int(input("Enter your weight: "))
    if weight>=50:
        print("You are eligible for blood donation.")
    else:
        print("You are not eligible.")
else:
    print("Your age is not appropriate for donating blood.")
