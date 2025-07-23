class Desktop:
    def  __init__(self):
        self._max_price = 25000
        
    def sell(self):
        return f"Selling price: {self._max_price}"
    
    def set_max_price(self, price):
        if price > self._max_price:
            self._max_price = price
            
        
#object

desktopObj = Desktop()
print(desktopObj.sell())

# Update the max price
desktopObj.set_max_price(35000)
print(desktopObj.sell())