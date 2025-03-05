# Write a Python program to sort a list using both sort() and sorted(). 

#with dynamic
num = int(input("num: "))
l1=[] #create a empty dictinary
for i in range(num):
    n1 = int(input("n1: "))
    l1.append(n1)
print(l1)

#sort in l1 ( sort is a method)
l1.sort(reverse=True) # decending
print(l1)
l1.sort(reverse= False) # ascending
print(l1)

#sorted is a function

l4 = sorted(l1)
print(l4)