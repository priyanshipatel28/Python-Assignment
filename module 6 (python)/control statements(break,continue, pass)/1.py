# Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue 
# statement. List1 = ['apple', 'banana', 'mango'] 

list1 =['apple','banana','mango']

for i in list1:
    if i == 'banana':
        continue#the continue statement only affects the iteration flow, not the list content.
    print(i,end=" ")# on this way it will print the list

print(list1)# the continue statement is for iteration it will noe effect the list itself.
# so it i want to remove banana from the list then i have to do it manually or by remove method.

