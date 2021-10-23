'''
Class 
A class is a blue print for the object
An object has two charecteristics
1) Attributes
2) Behaviour/Method

Syntax:
class class Name(object):
    --snip--

creating class object
objectname=classname(arguments) 
'''

class myClass(object):
    '''
    This is my First Class
    '''
    a=10

    def myFunc(self):
        print('Hello')

obj=myClass()
obj.myFunc()
print(myClass.a)
print(myClass.__doc__)
print(myClass.__name__)
print(myClass.__base__)

class Parrot:
    # Class attribute
    species='Bird'

    
    # instance Attribute
    def __init__(self,n,a):
        print("This is Parrot Class")
        self.name=n
        self.age=a
        

tiya=Parrot('Mithu',2)
print(f'{tiya.name} is {tiya.age} Years old')
print(f'{tiya.name} is a {tiya.species}')
print(tiya.__class__)
# Tota=Parrot()







