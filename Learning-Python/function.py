
#  Prime
import math
def checkPrime(a):
    if a<2:
        return False
    if a==2:
        return True
    for i in range(2,int(math.sqrt(a))):
        if a%i==0:
            return False
    return True

for i in range(0,100):
    if checkPrime(i)==True:
        print(i)
    