# Write a Python program to iterate over a list using a for loop.

#with static
l1=[8,1,2,3,4,5]
for i in l1:
    print(i) # here it will directly interate element

for i in range(len(l1)):
    print(i) # here it will iterate index number but to access element we will use l1[i]
    print(l1[i])


#with dynamic
num = int(input("num: "))
l1=[] #create a empty dictinary
for i in range(num):
    n1 = int(input("n1: "))
    l1.append(n1)
print(l1)

for i in l1:
    print(i)

for i in range(len(l1)):
    print(l1[i])

