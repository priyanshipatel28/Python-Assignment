#  Write a Python program to demonstrate the use of local and 
# global variables in a class.

l1=[1,2,3,4]
class demon:
    global l1
    l1.append(100)

    def display_for_list(self):
        print(l1)
    
    #local
    num = 10
    def diaplay_for_local(self):
        print("The previous number :",self.num)
    def change_number(self):
        self.num1 = self.num + 10
    def diaplay_for_local_number(self):
        print("The after number :",self.num1)
    
d1 = demon()
d1.display_for_list()
d1.diaplay_for_local()
d1.change_number()
d1.diaplay_for_local_number()