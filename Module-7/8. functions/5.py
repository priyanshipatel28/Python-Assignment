# Write 
# a Python program to create a lambda function with two expressions.
x=lambda y,z : y+z
print(x(5,10))

#just for knowledge
x=lambda y,z : y*z
print(x(5,10))

#even and odd if second paramter is even
x=lambda y,z : y+z if z%2==0 else y
print(x(5,10))