# Write a Python program to open a file in write mode, write some text, and then close it.
# write(): Writes a single string to the file.
# writelines(): Writes multiple strings from an iterable to the file.

# Writing using write()
f=open("with_write.txt",'w')
f.write("alisha \n")
f.write("jitu\n")

# Writing using writelines()
lines = ["first line\n", "second line\n", "third line\n"]
f= open("with_writelines.txt",'w')
f.writelines(lines)
