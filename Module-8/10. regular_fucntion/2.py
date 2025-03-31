#  Write a Python program to match a word in a string using re.match(). 
import re

text = "cat in the hat"
pattern = r"hat"

print("match:", bool(re.match(pattern, text)))  # False (only checks beginning)
print("search:", bool(re.search(pattern, text)))  # True (checks anywhere)