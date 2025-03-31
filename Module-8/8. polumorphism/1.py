# 19) Write a Python program to show method overloading.
# ====> python is not supported in overloading.

# 20) Write a Python program to show method overriding. 
# When a child class inherits from a parent class and defines a method with the same name as the one in the parent class, the child class version overrides the parent class version.
class Car:
    def fuel_type(self):
        return "Petrol"  

class Tesla(Car):
    def fuel_type(self):  
        return "Electric"  
    
car = Car()         
tesla = Tesla()    
print(car.fuel_type())    
print(tesla.fuel_type())    
