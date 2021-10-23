'''
Polymorphism forms- Bohurup
Plymorphism is an ability to use common interface for multiple form
Ex:There are ultiple Shape option(Rectange, Circle, Triange)

'''

class Parrot:
    def fly(self):
        print('Parrot can fly')

    def swim(self):
        print("Parrot can\'t  swim")

class Penguin:
    def fly(self):
        print('Penguin can\'t fly')

    def swim(self):
        print("Penguin can  swim")

def fly_test(obj):
    obj.fly()

def swim_test1(obj):
    obj.swim()

Tiya=Parrot()
peddy=Penguin()

fly_test(Tiya)
fly_test(peddy)

