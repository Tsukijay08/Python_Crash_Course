# Define a custom metaclass
class  MyMetaClass(type):
   def __init__(cls, name, bases, dct):
      print('Initializing class', name)
        
      # Add a class-level attribute
      cls.version= 10
      
      super().__init__(name, bases, dct)

# Define a class using the custom metaclass
class MyClass(metaclass=MyMetaClass):
   def __init__(self, value):
      self.value = value
    
   def display(self):
      print(f"Value: {self.value}, Version: {self.__class__.version}")

# Instantiate the class and demonstrate its usage
obj = MyClass(42)
obj.display()