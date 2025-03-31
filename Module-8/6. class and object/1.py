# Write a Python program to create a class and access the properties 
# of the class using an object. 

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        return f"Name : {self.name} and Age : {self.age}"

s1 = student("shreya",21)
print(s1.display())