# Write a Python program to create a list with elements of multiple data types (integers, 
# strings, floats, etc.). 

l1 = [45,1.5,"hello",True]
print(l1)

l2 = []
for i  in range(4):
    num = input("Enter your elements: ")
    l2.append(num)

print(l2)