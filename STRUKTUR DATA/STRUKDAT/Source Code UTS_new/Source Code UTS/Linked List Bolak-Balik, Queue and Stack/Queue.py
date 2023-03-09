class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
    def setValue(self, value):
        self.__value = value
    def setNext(self, next):
        self.__next = next
    def getValue(self):
        return self.__value
    def getNext(self):
        return self.__next

class Queue:
    def __init__(self):
        self.first =  None
    def hasPop(self):
        return self.first != None
    def push(self, value):
        new_node = Node(value)
        if self.first == None:
            self.first = new_node
        else:
            n = self.first
            while n.getNext() != None:
                n = n.getNext()
            n.setNext(new_node)
    def pop(self):
        if self.hasPop():
            self.first = self.first.getNext()
    def printQ(self):
        n = self.first
        while n != None:
            print(n.getValue(), "-->", end=" ")
            n = n.getNext()
        print("None")

print("Queue")
myQueue = Queue() 
myQueue.push('K')
myQueue.printQ()
myQueue.push('A')
myQueue.printQ()
myQueue.push('M')
myQueue.printQ()
myQueue.push('I')
myQueue.printQ()
myQueue.push('L')
myQueue.printQ()
print()
print("Pop Queue")
while myQueue.hasPop():
    myQueue.pop() 
    myQueue.printQ()

