class Point :
    """
    This is my point class
    """
    def __init__(self,x,y) -> None:
       self.x,self.y=x,y

    # def __repr__(self) -> str:
    #     return f'Point(x={self.x},y={self.y})'
   
    def __str__(self) -> str:
        return f'Point(x={self.x},y={self.y})'

    def __len__(self) :
        return self.x+self.y

    def get_Total(self):
        return sum([self.x,self.y])



    
p=Point(5,7)
print(p)
print(len(p))
print(p.get_Total())

# Recursion=Function call itself
# 3!=3*2*1

num=1
def factorial(N):
    if N ==0:
        return 1
    else:
        return N*factorial(N-1)

print(factorial(num))

#prime Number
def check_prime(num,i):
    if num==i:
        return 0
    else:
        if num%i==0:
            return 1
        else:
            return check_prime(i+1,num)
n=11
print(check_prime(n,2)==0)












