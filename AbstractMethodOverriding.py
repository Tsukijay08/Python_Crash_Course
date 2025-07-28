from abc import ABC ,abstractmethod
class DemoClass(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return
    def method2(self):
        print("concrete method")
        
        
class ConcreteClass(DemoClass):
    def method1(self):
        super().method1()
        return
obj = ConcreteClass()
obj.method1()
obj.method2()