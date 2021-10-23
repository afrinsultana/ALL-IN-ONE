"""
class baseclass: 
    pass

class derivedClass(baseClass):
    pass

"""

# Parent Class
class Bird:
    def __init__(self) -> None: # Constructor
        print('Bird is Ready')
    def whoIsThis(self):
        print('Bird')
    def swim(self):
        print('Swim Faster')

class penguin(Bird):
    def __init__(self) -> None:
        super().__init__()
        print('Penguin is ready')
    def whoIsThis(self):
        print('Penguine')
    def run(self):
        print('Run faster')

p=penguin()
p.whoIsThis()
p.swim()
