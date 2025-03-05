# Write a  Python program to create a tuple with multiple data types.

l1=[]
num = int(input("Enter num:"))
for i in range(num):
    n = input("Enetr eement for list:")
    l1.append(n)
print(l1)
t1=tuple(l1)
print("the tuple is :",t1)