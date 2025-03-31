#multilevel
# A derived class WashingMachine inherits from Appliance and adds an attribute capacity with a method show_capacity() to display the washing machine's capacity.

class appliance():
    def __init__(self,capacity):
        self.capacity = capacity
    def show_capacitty(self):
        return f"the capacity is: {self.capacity}"
    
class model(appliance):
    def __init__(self, capacity,name):
        super().__init__(capacity)
        self.name = name

class washingmachine(model):
    def __init__(self, capacity, name):
        super().__init__(capacity, name)
    def display(self):
        print(self.show_capacitty())
        print("The name of the model is -",self.name)

w=washingmachine(7,"sumsung")
w.display()
