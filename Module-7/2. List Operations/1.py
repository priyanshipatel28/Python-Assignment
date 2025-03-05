#contaenation
l1= ['a','b','c']
print(l1*2)
#output: 
        # ['a','b','c','a','b','c']
#membership
l1= ['a','b','c']
print('a' in l1)

# Write a Python program to add elements to a list using insert() and append().
l1 = []
for i in range(1,6):
    num = int(input("Enter any number: "))
    l1.append(num)
print(l1)
#to insert a element in list
print("for insert")
index = int(input("Enter the index number you want to add element: "))
element = int(input("Enter any number: "))
l1.insert(index,element)
print(l1)

#to add element at the end of list , we will use append
# append is a method that will be accessed with(.) operator.
print("for append")
l1.append(45)
print(l1)