class Student:
    def __init__(self):
        self.name = "Jojit"
        self.subs= self.Subject()
        return
    def show(self):
        print("Name :" ,self.name)
        self.subs.display()
    class Subject:
        def __init__(self):
            self.sub1 = "Python Learning"
            self.sub2 = "Java Spring Boot"
            return
        def display(self):
            print ("Subject :", self.sub1, self.sub2)
            
            
s1 = Student()
s1.show()
        