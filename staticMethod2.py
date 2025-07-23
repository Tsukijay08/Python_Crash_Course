class Student:
    stdCount = 0
    def __init__(self, name , age):
        self.__name = name
        self.__age = age
        Student.stdCount += 1
        
    @staticmethod
    def showCount():
     print(Student.stdCount)
            
std1 = Student("Jojit", 28)
std2 = Student("Fritz", 29)
std3 = Student("Jeff", 30)

print ("Number of Student ")
Student.showCount()
            