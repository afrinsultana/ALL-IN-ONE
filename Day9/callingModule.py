import module1 as m
import os

while True :
    os.system('cls')  # Clear Screen
    print('  Main Menu ')
    print('-'*20)
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. exit')
    print('Enter Your Selection : ')
    ch=input()
    if ch=='1': 
        x=int(input('Enter First Value: '))
        y=int(input('Enter Second Value: ')) 
        results=m.add(x,y)
        print(f'addition is {results}')
        break
    elif ch=='2':
         x=int(input('Enter First Value: '))
         y=int(input('Enter Second Value: ')) 
         results=m.sub(x,y)
         print(f'Subtraction is {results}')
         break
    elif ch=='3':
         x=int(input('Enter First Value: '))
         y=int(input('Enter Second Value: ')) 
         results=m.mult(x,y)
         print(f'Multiplication is {results}')
         break
    elif ch=='4':
         x=int(input('Enter First Value: '))
         y=int(input('Enter Second Value: ')) 
         results=m.div(x,y)
         print(f'Division is {results}')
         break
    elif ch=='5':
        break
    else:
        print('Sorry Invalid Selection')
        print('Press Enter to continue ........') 
        input()    




