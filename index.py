def isPrime(num):
    if(num == 2):
        return True
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True


def printPrime(num):
    import array as arr
    arr = []
    for i in range(2,num+1):
        if(isPrime(i)):
            arr.append(i)
    return arr

print(printPrime(100))