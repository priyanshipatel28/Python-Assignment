# Write a Python program to demonstrate string slicing. 

str = "Hello, World!"

print(type(str[0:5]))

# Basic Slicing: Extracting a substring using the [start:end] format
print(f"Basic Slicing: {str[0:5]}")

# Slicing with Omitted Start or End Index
print(f"Slicing with omitted start: {str[:5]}")
print(f"Slicing with omitted end : {str[7:]}")

# Negative Indexing: Counting from the end of the string
print(f"Last character using negative index : {str[-1]}")
print(f"Last 6 characters using negative index : {str[-6:]}")

# Slicing with Step Size: [start:end:step]
print(f"Slicing with step size : {str[0:12:2]}")
print(f"Slicing with negative step : {str[::-1]}")

# Slicing with Negative Indices and Step Size
print(f"Slicing with negative step: {str[-1:-12:-2]}")

# Edge Cases for String Slicing
print(f"Edge case (start > end): '{str[5:2]}'")

# Slicing from the middle of the string
print(f"Middle slice : {str[7:12]}")

# Length of a sliced string
print(f"Length of sliced string : {len(str[0:5])}")
