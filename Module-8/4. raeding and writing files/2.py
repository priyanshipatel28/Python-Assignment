# Write a Python program to write multiple strings into a file. 
w1 = ("hello,\nthis is my first program.\nthis is a writelines program,\n i am trying to do write data with tuple.\nthank you for watching!!")
f=open("two.txt",'w')
f.write(w1)
print("done!")
f.close()
