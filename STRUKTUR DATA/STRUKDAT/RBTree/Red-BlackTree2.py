class Node:
    def __init__(self, key, value):
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__key = key
        self.__isRed = False
        self.__value = value
    # Method untuk mengupdate nilai dari variabel private "IsRed"
    def setIsRed(self, boolean):
        self.__isRed = boolean
    # Method untuk mengupdate nilai dari variabel private "Parent"
    def setParent(self, parent):
        self.__parent = parent
    # Method untuk mengupdate nilai dari variabel private "left"
    def setLeft(self,left):
        self.__left = left
    # Method untuk mengupdate nilai dari variabel private "Right"
    def setRight(self,right):
        self.__right = right
    # Method untuk mengupdate nilai dari variabel private "Key"
    def setKey(self, key):
        self.__key = key
    # Method untuk mengupdate nilai dari variabel private "Value"
    def setValue(self, value):
        self.__value = value
    # Method untuk mendapatkan nilai dari variabel private "IsRed"
    def getIsRed(self):
        return self.__isRed
    # Method untuk mendapatkan nilai dari variabel private "Parent"
    def getParent(self):
        return self.__parent
    # Method untuk mendapatkan nilai dari variabel private "Left"
    def getLeft(self):
        return self.__left
    # Method untuk mendapatkan nilai dari variabel private "Right"
    def getRight(self):
        return self.__right
    # Method untuk mendapatkan nilai dari variabel private "Key"
    def getKey(self):
        return self.__key
    # Method untuk mendapatkan nilai dari variabel private "Value"
    def getValue(self):
        return self.__value
    # def getLeft(self) :
    #     return self.__left

class RBTree:
    def __init__(self):
        self.nil = Node(0,"nil")
        self.nil.setIsRed(False)
        self.nil.setLeft(None) 
        self.nil.setRight(None)
        self.root = self.nil

    def insert(self, key, value):
        # Ordinary Binary Search Insertion
        new_node = Node(key, value)
        new_node.setParent(None)
        new_node.setLeft(self.nil)
        new_node.setRight(self.nil)
        new_node.setIsRed(True)

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.getKey() < current.getKey():
                current = current.getLeft()
            elif new_node.getKey() > current.getKey():
                current = current.getRight()
            else:
                return

        # Set the parent and insert the new node
        new_node.setParent(parent)
        if parent == None:
            self.root = new_node
        elif new_node.getKey() < parent.getKey():
            parent.setLeft(new_node)
        else:
            parent.setRight(new_node)

        # Fix the tree
        self.fix_insert(new_node)

    # rotate left at node x
    def rotate_left(self, x):
        y = x.getRight()
        x.setRight(y.getLeft())
        if y.getLeft() != self.nil:
            y.getLeft().setParent(x)

        y.setParent(x.getParent())
        if x.getParent() == None:
            self.root = y
        elif x == x.getParent().getLeft():
            x.getParent().setLeft(y)
        else:
            x.getParent().setRight(y)
        y.setLeft(x)
        x.setParent(y)


    # rotate right at node x
    def rotate_right(self, x):
        y = x.getLeft()
        x.setLeft(y.getRight()) 
        if y.getRight() != self.nil:
            y.getRight().setParent(x)

        y.setParent(x.getParent())
        if x.getParent() == None:
            self.root = y
        elif x == x.getParent().getRight():
            x.getParent().setRight(y)
        else:
            x.getParent().setLeft(y)
        y.setRight(x)
        x.setParent(y)

    def fix_insert(self, new_node):
        while self.root != new_node and True == new_node.getParent().getIsRed():
            if new_node.getParent() == new_node.getParent().getParent().getLeft():
                if new_node.getParent().getParent().getRight().getIsRed():
                    new_node.getParent().getParent().getRight().setIsRed(False)
                    new_node.getParent().getParent().setIsRed(True)
                    new_node.getParent().setIsRed(False)
                    new_node = new_node.getParent().getParent()
                else:
                    if new_node == new_node.getParent().getRight():
                        self.rotate_left( new_node.getParent() )
                    new_node.getParent().setIsRed(False)
                    new_node.getParent().getParent().setIsRed(True)
                    self.rotate_right( new_node.getParent().getParent() )
            else:
                if new_node.getParent().getParent().getLeft().getIsRed():
                    new_node.getParent().getParent().getLeft().setIsRed(False)
                    new_node.getParent().getParent().setIsRed(True)
                    new_node.getParent().setIsRed(False)
                    new_node = new_node.getParent().getParent()
                else:
                    if new_node == new_node.getParent().getLeft():
                        self.rotate_right( new_node.getParent() )
                    new_node.getParent().setIsRed(False)
                    new_node.getParent().getParent().setIsRed(True)
                    self.rotate_left( new_node.getParent().getParent() )
        self.root.setIsRed(False)
    
    def exist(self, key):
        if type(search(self.root,key)) == Node:
            print("Ada")
            return True
        else:
            print("Tidak Ada")
            return False

    def edit(self, key, value):
        if self.exist(key):
            temp = search(self.root,key).getValue()
            search(self.root,key).setValue(value)
            print(f"Red Black Tree dengan key:{key}, valuenya telah diubah dari {temp} menjadi {search(self.root,key).getValue()}")
        else:
            print("Key tidak ditemukan, tidak bisa mengupdate value")

    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

def search(root, key):
        if key < root.getKey():
            if root.getLeft() is None:
                return str(key)+" Not Found" 
            return search(root.getLeft(),key)
        elif key > root.getKey():
            if root.getRight() is None:
                return str(key)+" Not Found" 
            return search(root.getRight(),key)
        else:
            return root

def PrintTree(root):
    def height(root):
        return 1 + max(height(root.getLeft()), height(root.getRight())) if root else -1  
    nlevels = height(root)
    width =  pow(2,nlevels+1)

    q=[(root,0,width,'c')]
    levels=[]

    while(q):
        node,level,x,align= q.pop(0)
        if node:            
            if len(levels)<=level:
                levels.append([])
        
            levels[level].append([node,level,x,align])
            seg= width//(pow(2,level+1))
            q.append((node.getLeft(),level+1,x-seg,'l'))
            q.append((node.getRight(),level+1,x+seg,'r'))

    for i,l in enumerate(levels):
        pre=0
        preline=0
        linestr=''
        pstr=''
        seg= width//(pow(2,i+1))
        for n in l:
            valstr= str(n[0].getKey())
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
                linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
                preline = n[2] + seg + seg//2   
            valstrC = "\033[0;31m"+ valstr +"\033[0m" if n[0].getIsRed() == True else valstr 
            pstr+=' '*(n[2]-pre-len(valstr))+ valstrC
            pre = n[2]
        print(linestr)
        print(pstr)

r = RBTree() 
r.insert(1, "Satu")
print("insert(1):")
PrintTree(r.root)  
r.insert(2, "Dua")
print("insert(2):")
PrintTree(r.root)  
r.insert(3, "Tiga")
print("insert(3):")
PrintTree(r.root)  
r.insert(4, "Empat")
print("insert(4):")
PrintTree(r.root)  
r.insert(5, "Lima")
print("insert(5):")
PrintTree(r.root)  
r.insert(6, "Enam")
print("insert(6):")
PrintTree(r.root)  
r.insert(7, "Tujuh")
print("insert(7):")
PrintTree(r.root)  
r.insert(8, "Delapan")
print("insert(8):")
PrintTree(r.root)
r.exist(10)
r.edit(7,"TUJUHHHH")
r.deleteNode(Node(5, "Lima"))

