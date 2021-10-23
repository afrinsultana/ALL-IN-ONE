class person:
    """
    A simple model of person class
    """
    def __init__(self,id,name,age) -> None:
        self.id=id
        self.name=name
        self.age=age

    def __str__(self) -> str: # arekta method ke override korbo
        return f'{self.id} {self.name} {self.age}'
    def walk(self): 
        print(self.name,'is now running')

    def show(self):
        s=f'ID={self.id}\n Name= {self.name}\n age={self.age}'
        return s
class student(person): # Child Class create korlam
    def __init__(self, id, name, age, fees) -> None:
        super().__init__(id, name, age)
        self.fees=fees


def __str__(self) -> str: # arekta method ke override korbo
        return f'{self.id} {self.name} {self.age} {self.fees}'
  
def show(self):
        s=f'ID={self.id}\n Name= {self.name}\n age={self.age}\n fees={self.fees}'
        return s

# p=person(1,'Aziz Uddin','20') # object create korbo
# # print(p.id,p.name,p.age)
# print(p)
# p.walk()
# print(p.show())



