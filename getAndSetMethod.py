class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    
    def setName(self, name):
        self.__name = name
        return
    def setAge(self,age):
        self.__age = age
        return
    
emp1 = Employee("Jojit", 28)
print ("Name :",emp1.getName(), "Age :" , emp1.getAge())
emp1.setName("Princess")
emp1.setAge(1)
print ("Name :",emp1.getName(), "Age :" , emp1.getAge())
