# ) Write a Python program to count how many times each 
# character appears in a string.
def character(s1):
    d1={}
    for i in s1:
        d1[i] = s1.count(i)
    return d1

s1=input("Enter the string: ")
print(character(s1))