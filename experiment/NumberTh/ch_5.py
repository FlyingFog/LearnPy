#整除性与最大公约数
import math

#5.2
def gcd(a,b):
    if a==0 and b==0:
        return 0
    return gcd(b , a%b)

def threeNPlusOne():

