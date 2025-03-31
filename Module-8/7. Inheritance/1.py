#single inheriatance
# A base class Book has an attribute title and a method show_title() to display the title of the book.

#base
class book:
    def __init__(self,name):
        self.name = name
class author(book):
    def __init__(self, name,title,page):
        book.__init__(self,name)
        self.title = title
        self.page = page
    def display(self):
        print(f"""
            The name of the book is :{self.name}
            The title of the book is :{self.title}
            Total pages are :{self.page}
              """)
try:        
    name = input("Enter the name: ")
    title = input("Enter the title: ")
    page =  int(input("Enter no. of pages: "))
    a = author(name,title,page)
    a.display()
except Exception as e:
    print("error:",e)
