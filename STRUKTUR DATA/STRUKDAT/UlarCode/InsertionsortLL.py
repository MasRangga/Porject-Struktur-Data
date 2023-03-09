class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__prev = None
    def setValue(self, value):
        self.__value = value
    def setNext(self, next):
        self.__next = next
    def setPrev(self, prev):
        self.__prev = prev
    def getValue(self):
        return self.__value
    def getNext(self):
        return self.__next
    def getPrev(self):
        return self.__prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_end(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            n = self.head
            while n.getNext() != None:
                n = n.getNext()
            n.setNext(new_node)
            new_node.setPrev(n)
            self.tail = new_node

    def add_begin(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.setNext(self.head)
            self.head.setPrev(new_node)
            self.head = new_node

    def printLL(self):
        n = self.head
        print("Hasil:")
        while n != None:
            if n.getNext() == None:
                print(n.getValue())
            else:
                print(n.getValue(),end=",")
            n = n.getNext()


    def InsertionSort(self, value):
        node = Node(value)
        if self.head == None or value < self.head.getValue():
            self.add_begin(value)
        elif self.tail.getValue() < value:
                self.add_end(value)
        else:
            n = self.head
            while n.getNext() != None and n.getValue() < value:
                n = n.getNext()
            previous = n.getPrev()
            previous.setNext(node)
            node.setPrev(previous)
            node.setNext(n)
            n.setPrev(node)

print(".:: Program Pengurutan ::.")
value = str(input("Masukkan beberapa angka acak(dipisahkan dengan koma) :"))
try:
    number = value.split(",")
    myLL = LinkedList()
    for x in number:
            myLL.InsertionSort(int(x))
    myLL.printLL()
except:
    print("input harus berupa angka-angka yang dipisahkan dengan koma")