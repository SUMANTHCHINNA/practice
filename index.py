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
# 6th program
# Queues
class Queue:
    def __init__(self) -> None:
        self.arr=[]
    def enqueue(self,item):
        return self.arr.append(item)
    def dequeue(self):
        return self.arr.pop(0)
    def peek(self):
        return self.arr[-1]
    def display(self):
        return self.arr

# 7th program...
# Sorting...

def Sorting(arr):
    z=len(arr)
    for x in range(1,z,1):
        for y in range(0,z,1):
            if(arr[y]>arr[x]):
                arr[y],arr[x]=arr[x],arr[y]

# 8th program...
# Iterative python program to reverse an array
 
# # Function to reverse A[] from start to end
# def reverseList(A, start, end):
#     while start < end:
#         A[start], A[end] = A[end], A[start]
#         start += 1
#         end -= 1
#     return A
 
# # Driver function to test above function
# A = [1, 2, 3, 4, 5, 6]
# print(A)
# reverseList(A, 0, 5)
# print("Reversed list is")
# print(A)
# # This program is contributed by Pratik Chhajer

def reverseList(A):
    start = 0
    end = len(A)-1
    while(start < end):
        A[start], A[end] = A[end], A[start]
        start = start+1
        end = end-1
    return A

arr = [1,2,3,4,5,6]
# print(reverseList(arr))

def reverseList1(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList1(A, start+1, end-1)
 
A = [1, 2, 3, 4, 5, 6]
reverseList1(A, 0, 5)
# print(A)

# 9th program...
# occurance of number in array

def countOccurrences(A,len,num):
    res=0
    for i in range(len):
        if A[i] == num:
            res += 1
    return res

arr = [1, 2, 2, 2, 2, 3, 4, 7 ,8 ,8]
len = len(arr)
num = 2
# print(countOccurrences(arr,len,num))

#10th program...
# binary search

def binarySearch(arr,target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr=[1,2,4,5,6,7,8]
print(binarySearch(arr,5))
