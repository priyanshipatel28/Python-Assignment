#  23) Write a Python program to search for a word in a string using 
# re.search().

# regular expresiions: A regular expression (regex) is a pattern-matching string used to search, match, and manipulate text efficiently
import re

if re.search("python","WElcome to python programming!"):
  print("Result match !!!")
else:
  print("Result Not Found !!")