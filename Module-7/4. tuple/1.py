# Write a Python program to convert a list into a tuple.
#for static:
l1=["hello",45,12.56,True]
t1= tuple(l1)
print(t1)

#for dynamic:
l1=[]
num = int(input("Enter num:"))
for i in range(num):
    n = int(input("Enetr eement for list:"))
    l1.append(n)
print(l1)
t1=tuple(l1)
print(t1)