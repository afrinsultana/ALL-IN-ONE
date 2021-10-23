
#prime Number
def check_prime(num,i=2):
    if num==i:
        return 0
    else:
        if num%i==0:
            return 1
        else:
            return check_prime(num,i+1)
# n=30
n=int(input("Enter last Value:"))
for x in range(1,n+1):
    if check_prime(x)==0:
        print(x,end='\t')
    


