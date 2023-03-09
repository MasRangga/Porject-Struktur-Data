class Node:
    def __init__(self, key, value):
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__key = key
        self.__isRed = False
        self.__value = value
    def setRed(self, boolean):
        self.__isRed = boolean
    def setParent(self, parent):
        self.__parent = parent
    def setLeft(self,left):
        self.__left = left
    def setRight(self,right):
        self.__right = right
    def setKey(self, key):
        self.__key = key
    def setValue(self, value):
        self.__value = value
    def getRed(self):
        return self.__isRed
    def getParent(self):
        return self.__parent
    def getLeft(self):
        return self.__left
    def getRight(self):
        return self.__right
    def getKey(self):
        return self.__key
    def getValue(self):
        return self.__value
class HashMap:
    def __init__(self,sensitive):
        self.nil = Node(0,"nil")
        self.nil.setRed(False)
        self.nil.setLeft(None)
        self.nil.setRight(None)
        self.root = self.nil
        self.sensitive = sensitive

    def add(self, key, value):
        key = key if self.sensitive == True else key.lower()
        if self.sensitive == False and type(value) == str:
            value = value.lower()\
            
