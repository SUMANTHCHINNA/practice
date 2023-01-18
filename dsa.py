class Queue:
    def __init__(self):
        self.arr=[]
    def enqueue(self,item):
        return self.arr.append(item)
    def dequeue(self):
        return self.arr.pop(0)
    def display(self):
        return self.arr
    def peek(self):
        return self.arr[-1]
#driver code....
x=Queue()
print(x.enqueue(1))
print(x.enqueue(2))
print(x.enqueue(3))
print(x.enqueue(4))
print(x.enqueue(5))
print(x.display())
print(x.dequeue())
print(x.dequeue())
print(x.display())
print(x.peek())

