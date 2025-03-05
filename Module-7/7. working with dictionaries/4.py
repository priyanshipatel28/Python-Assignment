# Write a Python program to separate keys and values from a dictionary using 
# keys() and values() methods. 

d1 ={}
num = int(input("Enter any num:"))
for i in range(num):
    key = input("Enter any word:")
    value = int(input("Enter the num: "))
    d1[key] = value

print(d1)
print("The keys are: ",d1.keys())
print("The values are: ",d1.values())