# Write a Python program to update a value in a dictionary. 
d1 ={}
num = int(input("Enter any num:"))
for i in range(num):
    key = input("Enter any word:")
    value = int(input("Enter the num: "))
    d1[key] = value

print(d1)
d1["new_key"] = "hello"
print(d1)
