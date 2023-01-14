# 1st program
import array as arr

def isPrime(num):
    if(num == 2):
        return True
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True


def printPrime(num):
    arr = []
    for i in range(2,num+1):
        if(isPrime(i)):
            arr.append(i)
    return arr

# print(printPrime(100))

# 2nd program

def isEven(num):
    if(num % 2 == 0):
        return True
    else:
        return False

def printEven(num):
    arr = []
    for i in range(1,num+1):
        if(isEven(i)):
            arr.append(i)
    return arr

def factRecurssion(num):
    if(num == 1):
        return 1
    else:
        return factRecurssion(num-1)*num

def Fact(num):
    count=1
    for i in range(1,num+1):
        count = count*i
    return count


