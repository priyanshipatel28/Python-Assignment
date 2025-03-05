# Write a Python program to convert two lists into one 
# dictionary using a for loop. 

l1=[i for i in range(5)]
l2=[i for i in range(11,16)]

d1={}
for i in range(len(l1)):
    d1[i] =l2[i]

print(d1)