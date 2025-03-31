# #hybrid
# A base class University has an attribute university_name and a method show_university_name().
# A class Professor inherits from University and has an attribute subject with a method show_subject().
# A class Student also inherits from University and has an attribute course with a method show_course().
# A class ResearchAssistant inherits from both Professor and Student and has a method show_details() to display all the related information.

class university:
    def __init__(self,name):
        self.name = name
    def show_university_name(self):
        return f"NAME : {self.name}"
    
class professor(university):
    def __init__(self,name,subject):
        #super().__init__(name)
        self.subject = subject
    def show_subject(self):
        return f"SUBJECT : {self.subject}"

class student(university):
    def __init__(self,name,course):
        super().__init__(name)
        self.course = course
    def show_course(self):
        return f"COURSE : {self.course}"
    
class research_assistant(professor,student):
    def __init__(self, name, subject,course):
        professor.__init__(self,name,subject)
        student.__init__(self,name,course)

    def show_details(self):
        return f"{self.show_university_name()}\n{self.show_subject()}\n{self.show_course()}"
ra = research_assistant("piyu","python","backend")
print(ra.show_details())