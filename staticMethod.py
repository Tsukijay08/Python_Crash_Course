class Employee:
    empCount = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Employee.empCount += 1
        
    #creating ststic method
    def showCount():
     print(Employee.empCount)
     return
    counter = staticmethod(showCount)
    
emp1 = Employee("Jojit", 28)
emp2 = Employee("Fritz", 29)
emp3 = Employee("Jeff", 27)
            
emp1.counter()
Employee.counter()