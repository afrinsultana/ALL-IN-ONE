# Syntax of Function
# =================================

# def function_name(parameters):
#     '''
#     Document String (doc String)    
#     '''
#     statements

# Function without arguments
def welcome():
    '''
    this function greets to the person
    '''
    print('Hello Shiddhartha kormokar. Good Morning!')


# Calling Function
welcome()
print(welcome.__doc__)


# Function with arguments
def welcome(name):
    '''
    this function greets to the person
    '''
    print(f'Hello {name}. Good Morning!')



welcome("Mahadi Hasan")
welcome("Sayed Nashid")

def welcome(name, msg):
    '''
    this function greets to the person
    '''
    print(f'Hello {name}.{msg} !')
welcome("Afrin Sultana","Ki Ranna Hoyeche")
welcome("Sayed Nashid","Chole Ashun")



# Python Arbitrary Arguments

def welcome(*names) :
    for x in names :
        print(f'Hello {x}')

welcome('Shahin','Sid','Aziz','Nawshin','Tahmid')


def addition(*nums) :
    sum=0
    for n in nums :
        sum=sum+n
    # print(sum)
    print(f'The Sum Is {sum}')
addition(5,10,15,20)
# addition(5+3+10+15+20)


# anonymus Functions are also called Lambda Functions
# syntax:
# functionName=lambda arguments: expression

# showDouble = lembda x:x*2
# def getDouble(x):
#     # print(x*2)
#     return x*2

# # getDouble(5)
# print(getDouble(20))

showDouble = lambda x:x*2
print(f'The Double Value is : {showDouble(2)}')

def getDouble(x):
    # print(x*2)
    return x*2

# getDouble(5)
# print(getDouble(20))

myList=[1,5,4,6,8,11,3,12]
newList=list(filter(lambda x:(x%2==0),myList))
print(newList)

# Keyword Arguments
def describe_Pet(petName,animalType):
    print(f'\n I have a {animalType}. ')
    print(f'My {animalType}\'s name is {petName.title()}. ')

describe_Pet(animalType='dog',petName='Tommy')

# Default Values
# def greet(name,msg) :
def greet(name,msg='Good Morning') :
    print(f'Hello {name},{msg}')
# greet('Sid',msg='Good Morning')
# greet('Sid',msg='Good Morning')
greet('Sid')
greet('Tahmid','Good Evening')
# ========================================================
def buildProfile(first,last,**UserInfo):
    profile={}
    profile['First_Name']=first
    profile['Last_Name']=last
    for key,value in UserInfo.items():
        profile[key]=value
    return profile

up=buildProfile('Afrin','Sultana',location='Dhaka',field='IT')
print(up)







