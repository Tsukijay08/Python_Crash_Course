class Student:
    def __init__(self, name = "Jojit", marks = 92):
        self.name = name
        self.marks = marks
        return
    
s1  = Student()
s2 = Student("Princess", 88)
    
print(" Name : {} marks : {}".format(s1.name,s1.marks))
print(" Name : {} marks : {}".format(s2.name,s2.marks))    
        