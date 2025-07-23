class Parent:
    parentAttr = 100
    def __init__(self):
        print ("Calling parent Constructor")

    def parentMethod(self):
        print("Calling parent method")
        
    def setAttr(self, attr):
        Parent.parentAttr = attr
        
    def getAttr(self):
        print("Parent Attribute :",Parent.parentAttr)
        
#defines child class
class Child(Parent):
    
    def __init__(self):
        print ("Calling Child constructor")
        
    def childMethod(self):
        print("Calling child method")
        
        
# instance of child
c = Child()  
# child calls its method        
c.childMethod() 
# calls parent's method     
c.parentMethod()  
# again call parent's method   
c.setAttr(200)  
# again call parent's method     
c.getAttr()      



        