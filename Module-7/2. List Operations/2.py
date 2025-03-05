# Write a Python program to remove elements from a list using pop() and remove(). 
l1 = []
for i in range(1,6):
    num = int(input("Enter any number: "))
    l1.append(num)
print(l1)

#to remove a element in list
num = int(input("Enter the elemnt you want to remove: "))
l1.remove(num)
print("after remove")
print(l1)

#to pop element in list
#bydefault
l1.pop()
print("after first pop")
print(l1)
#by index
num = int(input("Enter any number: "))
l1.pop(num)
print("after second pop")
print(l1)