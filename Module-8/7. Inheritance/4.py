#Hierarchical 
# # A base class Employee has attributes name and salary and a method show_employee_details() to display the details.
# A class Manager inherits from Employee and adds an attribute department with a method show_department().
# Another class Developer inherits from Employee and adds an attribute programming_language with a method show_language().

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def show_employee_details(self):
        return f"The name of the employee is {self.name}\nThe salary of the employee is {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department
    def show_department(self):
        return f" {self.show_employee_details()}\nThe departemnt is {self.department}"
    
class Developer(Employee):
    def __init__(self, name, salary,programming_langauge):
        super().__init__(name, salary)
        self.programming_langauge = programming_langauge
    def show_language(self):
        return f"{self.show_employee_details()}\nthe langauge is {self.programming_langauge}"
    
m= Manager("helli",25000,"IT")
print(m.show_department())

d = Developer("mahi",14500,"AI")
print(d.show_language())