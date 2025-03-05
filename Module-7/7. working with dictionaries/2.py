# Write a Python program to merge two lists into one dictionary using a loop. 
def merge(l1,l2):
    d1={}
    for i in range(len(l1)):
        d1[l1[i]] = l2[i]
    return d1

l1=[1,2,3,4,5]
l2=[101,102,103,104,105]
print(merge(l1,l2))