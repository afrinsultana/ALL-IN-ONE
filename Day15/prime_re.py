
#prime Number
def check_prime(num,i=2):
    if num==i:
        return 0
    else:
        if num%i==0:
            return 1
        else:
            return check_prime(num,i+1)
n=12
if check_prime(n,2)==0:
    print(f'{n} is a prime Number')

else:
    print(f'{n} is not a prime Bumber')