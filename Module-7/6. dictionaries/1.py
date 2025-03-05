# Write a Python program to create a dictionary of 6 key-value pairs. 

#dynamic with while loop
d1={}
status = True
while status:
    key = int(input("Enter the key:"))
    value = int(input("Enter the value: "))
    d1[key] = value

    choice = input("do you like to continue: ").lower()
    if choice == 'n':
        status= False
        print(d1)

# with for loop, if the no. of iteration is fixed:
num =int(input("Enter the num: "))
d1={}
for i in range(num):
    key = int(input("Enter the key:"))
    value = int(input("Enter the value: "))
    d1[key] = value
    print(d1)

