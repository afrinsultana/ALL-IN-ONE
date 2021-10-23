'''
Encapsulation:data Hiding

we can restrict accessto method and variable
This prevent data from direct modification which is called encapsulation
'''

class Computer:
    def __init__(self):
        self.__maxprice=900 # _prefix used for private attribute
    def sell(self):
        print(f"selling price is {self.__maxprice}")
    def setMaxPrice(self,price):
        self.__maxprice=price
    def __str__(self):
        return f'Computer er daam {self.__maxprice}'


c=Computer()
c.sell()
c.__maxprice=2000
c.sell()
c.setMaxPrice(3000)
c.sell()
print(c)