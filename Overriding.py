class Parent:
    def myMethod(self):
        print("Calling parent method")
        
#define child class

class Child:
    def myMethod(self):
        print("Calling child method")
        
        
#instance of child
c = Child()
# child calls overridden method
c.myMethod()

        
    