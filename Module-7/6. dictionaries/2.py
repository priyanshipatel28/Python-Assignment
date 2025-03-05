# Write a Python program to access values using keys from a dictionary. 

# here their are 2 ways to access , first with key name directly, seond with the get method it won't araise a key error.

d1 = {"name":"piyu","age":15,"salary":45000,"interest":1.12}

#to access the value
print(d1["name"])
print(d1["salary"])
print(d1["country"]) #it will raise an key error

# using get method
print(d1.get("name")) #or print(d1["name"]) same
print(d1.get("country")) # here it will print none , bydefault
print(d1.get("country","not in dictionary")) # here it will print the message i have written in d1.


