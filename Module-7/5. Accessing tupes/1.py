# ) Write a Python program to access values between index 1 and 5 in 
# a tuple. 1
#first way
# l1=[]
# num = int(input("Enter num:"))
# for i in range(num):
#     n = input("Enetr eement for list:")
#     l1.append(n)
# print(l1)
# t1=tuple(l1)
# print("the tuple is :",t1[1:6])

#another way
elements = input("Enter elements for the tuple, separated by spaces: ").split()
t1 = tuple(elements)

print("The tuple is:", t1)