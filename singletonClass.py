class Singleton:
    __instance = None
    
    
    def __new__(cls):
        if cls.__instance is None:
            print("Creating object")
            cls.instance = super(Singleton,cls).__new__(cls)
        return cls.__instance
obj1 = Singleton()
obj2 = Singleton()
        