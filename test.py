import math

def isPrime(num:int)->bool:
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num%i==0:
            return False
    return True

def printPrimes(num:int):
    if num<4 or num%2==1:
        raise Exception("Invalid Expression")
    for i in range(3,num//2+1,2):
        if isPrime(i) and isPrime(num-i):
            print(f"{i} + {num-i} = {num}")

printPrimes(8)
printPrimes(14)
printPrimes(100)
printPrimes(112)
