# Write a Python program that manipulates and prints strings using various string methods.
#each example is of formatting string
str = "  Hello, World!  "

greeting = "Hello" + " " + "World!"  # Concatenating two strings
print(f"Concatenation: {greeting}")

repeat_str = "Hello " * 3  # Repeating a string multiple times
print(f"Repetition: {repeat_str}")

print(f"Uppercase: {str.upper()}")

print(f"Lowercase: {str.lower()}")

print(f"Title Case: {str.title()}")

print(f"Length of the string: {len(str)}")

print(f"Is 'Hello' present in the string: {'Hello' in str}") #True or False

#Finding Substring Index(it will give on first index of the word or charater.)
print(f"Index of 'World': {str.find('World')}")

print(f"Starts with '  Hello': {str.startswith('  Hello')}")
print(f"Ends with 'World!  ': {str.endswith('World!  ')}")

