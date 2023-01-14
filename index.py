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

# 3rd program
def factRecurssion(num):
    if(num == 1):
        return 1
    else:
        return factRecurssion(num-1)*num

# 4th program
def Fact(num):
    count=1
    for i in range(1,num+1):
        count = count*i
    return count

def SumOfNatural(num):
    a = num*(num+1)
    return a/2

# 5th program
# stacks
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def display(self):
        return self.items
