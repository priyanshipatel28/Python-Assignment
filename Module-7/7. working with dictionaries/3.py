# Write a Python program to update a value at a particular key in a 
# dictionary. 

#by dynamic
d1 ={}
num = int(input("Enter any num:"))
for i in range(num):
    key = input("Enter any word:")
    value = int(input("Enter the num: "))
    d1[key] = value

print(d1)
key_to_update = input("\nEnter the key you want to update: ")
if key_to_update in d1:
    new_value = input("Enter the new value: ")
    d1[key_to_update] = new_value  # Update the value at the specified key
    print("\nUpdated dictionary:", d1)
else:
    print("\nThe key does not exist in the dictionary.")
