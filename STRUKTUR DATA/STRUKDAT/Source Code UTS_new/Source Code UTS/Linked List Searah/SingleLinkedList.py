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

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    # Method untuk menambahkan Node diakhir linked list
    def add_end(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.getNext() != None:
                n = n.getNext()
            n.setNext(new_node)
        self.length+=1

    # Method untuk menambahkan Node diawal linked list
    def add_begin(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            new_node.setNext(self.head)
            self.head = new_node
        self.length+=1

    # Method untuk menyisipkan node pada indeks tertentu
    def insert(self,value,index):
        if index == 0:
            self.add_begin(value)
        else:
            count=1
            n=self.head
            new_node=Node(value)
            while count<index and n!=None:
                n=n.getNext()
                count+=1
            if n == None:
                print("index yang dimasukkan melebihi panjang LinkedList")
            else:
                new_node.setNext(n.getNext())
                n.setNext(new_node)
        self.length+=1

    # Method untuk menampilkan nilai dari Node yang ada di linked list
    def printLL(self):
        n = self.head
        while n != None:
            print(n.getValue(), "-->", end=" ")
            n = n.getNext()
        print("None")

    # Method untuk mendapatkan Node pada indeks tertentu
    def getLL(self, index):
        if index == 0:
            return self.head.getValue()
        else:
            count=1
            n=self.head
            while count<index and n!=None:
                n=n.getNext()
                count+=1
            if n.getNext() == None:
                print("index yang dimaksud tidak ada")
            else:
                return n.getNext().getValue()
        
    # Method untuk menghapus Node berdasarkan indeks
    def remove(self, index):
        if index == 0:
            self.head = self.head.getNext()
        else:
            count=1
            n=self.head
            while count<index and n!=None:
                n=n.getNext()
                count+=1
            if n == None or n.getNext() == None:
                print("index yang dimasukkan harus kurang dari panjang LinkedList")
            else:
                n.setNext(n.getNext().getNext())
        self.length-=1


    # Method untuk menukar Node
    def swap(self, index1, index2):
        if index1 >= self.length or index2 >= self.length:
            print("indeks yang dimasukkan melebihi panjang linked list")
        elif index1 == index2:
            print("tidak bisa menjalankan perintah, indeks yang dimasukkan sama")
        elif self.head.getValue() == self.getLL(index1):
                temp = self.getLL(index1)
                self.add_begin(self.getLL(index2))
                self.remove(index1+1)
                self.insert(temp, index2)
                self.remove(index2+1)
        elif self.head.getValue() == self.getLL(index2):
                temp = self.getLL(index2)
                self.add_begin(self.getLL(index1))
                self.remove(index2+1)
                self.insert(temp, index1)
                self.remove(index1+1)
        else:   
            n=self.head
            while n != None:
                    if n.getValue() == self.getLL(index1):
                            temp = self.getLL(index1)
                            self.insert(self.getLL(index2),index1)
                            self.remove(index1+1)
                            self.insert(temp,index2)
                            self.remove(index2+1)
                            break
                    elif n.getValue() == self.getLL(index2):
                            temp = self.getLL(index2)
                            self.insert(self.getLL(index1),index2)
                            self.remove(index2+1)
                            self.insert(temp,index1)
                            self.remove(index1+1)
                            break
                    n = n.getNext()

myLL = SinglyLinkedList()
myLL.add_end(2)
myLL.add_end(1)
myLL.add_end(30)
myLL.remove(4)
myLL.printLL()