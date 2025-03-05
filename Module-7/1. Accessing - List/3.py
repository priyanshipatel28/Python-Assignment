# Write a Python program to find the length of a list using the len() function.

l1 = [45,1.5,"hello",True]
print(len(l1))

#length of list without len function
count = 0
for i in l1:
    count += 1
print(f"The length of list is : {count}")