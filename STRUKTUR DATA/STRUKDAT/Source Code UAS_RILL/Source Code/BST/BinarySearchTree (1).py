# Kelompok 4:
# Guntur Wisnu Saputra_11211042
# Muhammad Insan Kamil_11211058
# Muhammad Ricky Zakaria_11211062	
# Ramadhan Djibran Sanjaya_11211070	
# Rangga Hermawan_11211071	
# Rendy Pernanda_11211074	

class Node:
    # Method yang akan dieksekusi ketika membuat objek Node
    def __init__(self, value):
        self.__left = None
        self.__right = None
        self.__value = value
    # Method untuk mengupdate nilai dari variabel private "left"
    def setLeft(self,left):
        self.__left = left
    # Method untuk mengupdate nilai dari variabel private "right"
    def setRight(self,right):
        self.__right = right
    # Method untuk mengupdate nilai dari variabel private "value"
    def setValue(self, value):
        self.__value = value
    # Method untuk mendapatkan nilai dari variabel private "left"
    def getLeft(self):
        return self.__left
    # Method untuk mendapatkan nilai dari variabel private "right"
    def getRight(self):
        return self.__right
    # Method untuk mendapatkan nilai dari variabel private "value"
    def getValue(self):
        return self.__value

# Fungsi untuk menyelipkan node dibagian tertentu sesuai dengan konsep Binary Search Tree(BST)
def insert(root, value):
    # Untuk mengecek apakah root-nya kosong atau tidak, sekaligus sebagai batas dari perulangan yang dilakukan oleh fungsi rekursif
    if root is None:
        return Node(value)
    # Jika root tidak kosong
    else:
        # Jika nilai node yang ingin diinsert sama dengan nilai dari root, maka return root, karena dalam Binary Search Tree tidak bolah ada nilai yang duplikat
        if root.getValue() == value:
            return root
        # Jika nilai node yang ingin diinsert lebih besar dari nilai root, insert node tersebut ke bagian kanan root
        elif root.getValue() < value:
            root.setRight(insert(root.getRight(), value))
        # Jika nilai node yang ingin diinsert lebih kecil dari nilai root, insert node tersebut ke bagian kiri root
        else:
            root.setLeft(insert(root.getLeft(), value))
    return root

# Fungsi untuk menampilkan Binary Search Tree(BST) secara visual
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
            valstr= str(n[0].getValue())
            if n[3]=='r':
                linestr+=' '*(n[2]-preline-1-seg-seg//2)+ '¯'*(seg +seg//2)+'\\'
                preline = n[2] 
            if n[3]=='l':
                linestr+=' '*(n[2]-preline-1)+'/' + '¯'*(seg+seg//2)  
                preline = n[2] + seg + seg//2
            pstr+=' '*(n[2]-pre-len(valstr))+valstr 
            pre = n[2]
        print(linestr)
        print(pstr)   

# Fungsi untuk menampilkan nilai-nilai dari Node pada Binary Search Tree dari yang terkecil sampai yang terbesar
def inorder(root):
    if root:
        inorder(root.getLeft())
        print(root.getValue(), end=" ")
        inorder(root.getRight())

# Fungsi untuk mencari Node berdasarkan value 
def findNode(root, val):
    # Jika value yang dimasukkan pada parameter kurang dari nilai root, maka akan dicek bagian kiri dari root
    if val < root.getValue():
        # Jika dibagian kiri sampai bagian yang terdalam tidak ditemukan node yang nilai-nya sama dengan nilai yang dimasukkan pada parameter, maka kembalikan pesan bahwa "Nilai tersebut tidak ditemukan"
        if root.getLeft().getValue() is None:
            return str(val)+" Not Found"
        # mengembalikan node dibagian kiri root yang nilainya sama dengan nilai yang dimasukkan pada parameter 
        return findNode(root.getLeft(),val)
    # Jika value yang dimasukkan pada parameter lebih dari nilai root, maka akan dicek bagian kanan dari root
    elif val > root.getValue():
        # Jika dibagian kanan sampai bagian yang terdalam tidak ditemukan node yang nilai-nya sama dengan nilai yang dimasukkan pada parameter, maka kembalikan pesan bahwa "Nilai tersebut tidak ditemukan"
        if root.getRight().getValue() is None:
            return str(val)+" Not Found"
        # mengembalikan node dibagian kanan root yang nilainya sama dengan nilai yang dimasukkan pada parameter 
        return findNode(root.getRight(),val)
    # Jika value yang dimasukkan pada parameter sama dengan nilai root, maka return root
    else:
        return root

# Fungsi untuk mencari node dengan nilai terkecil
def minValueNode(node):
    current = node

    # Perulangan untuk mencari node dengan nilai terkecil
    while(current.getLeft() is not None):
        current = current.getLeft()

    return current

# Fungsi untuk menghapus Node berdasarkan value
def deleteNode(root, value):
  
    # Untuk mengecek apakah root-nya kosong atau tidak, sekaligus sebagai batas dari perulangan yang dilakukan oleh fungsi rekursif
    if root is None:
        return root
  
    # Jika nilai node yang ingin dihapus kurang dari nilai root, maka bagian kiri root akan diatur untuk menghapus node tersebut
    if value < root.getValue():
        root.setLeft(deleteNode(root.getLeft(), value))
  
    # Jika nilai node yang ingin dihapus lebih dari nilai root, maka bagian kanan root akan diatur untuk menghapus node tersebut
    elif(value > root.getValue()):
        root.setRight(deleteNode(root.getRight(), value))
    
    # Jika nilai node yang ingin dihapus sama dengan nilai root, maka root akan dihapus, lalu bagian kanan root atau bagian kiri root akan diatur untuk menggantikan root
    else:
        # Kondisi jika root hanya memiliki satu daun(leaf) atau tidak memiliki daun(leaf)
        # Jika root tidak memiliki daun, maka akan di return nilai None
        # Jika bagian kiri root kosong(tidak memiliki daun dibagian kiri), maka bagian kanan root yang akan menggantikan root yang telah dihapus
        if root.getLeft() is None:
            temp = root.getRight()
            root = None
            return temp
        # Jika bagian kanan root kosong(tidak memiliki daun dibagian kanan), maka bagian kiri root yang akan menggantikan root yang telah dihapus
        elif root.getRight() is None:
            temp = root.getLeft()
            root = None
            return temp


        # Kondisi jika root memiliki dua daun(leaf)
        # maka dicari node dengan nilai terkecil dibagian kanan root, kemudian node tersebutlah yang akan menggantikan root yang telah dihapus
        temp = minValueNode(root.getRight())
        root.setValue(temp.getValue())
        root.setRight(deleteNode(root.getRight(), temp.getValue())) 
  
    return root

# Fungsi untuk mengupdate value dari node
def updateVal(root,oldValue,newValue):
    # Menghapus node dengan nilai "odlValue"(nilai lama)
    deleteNode(root,oldValue)
    # Meng-insert node dengan nilai "newValue"(nilai baru)
    insert(root,newValue)


r = Node(5)
print()
print("\033[0;31m"+"Binary Search Tree"+"\033[0m")
r = insert(r, 3)
r = insert(r, 2)
r = insert(r, 4)
r = insert(r, 7)
r = insert(r, 6)
r = insert(r, 8)
PrintTree(r)
print("\033[0;31m"+"Call findNode(r,3):"+"\033[0m")
PrintTree(findNode(r,3))
print()
print("\033[0;31m"+"Call updateVal(r,7,10):"+"\033[0m")
print("Before:")
PrintTree(r)
print("Inorder")
inorder(r)
print("\n")
print("After:")
updateVal(r,7,10)
PrintTree(r)
print("Inorder")
inorder(r)
print("\n")
print("\033[0;31m"+"Call deleteNode(r,5):"+"\033[0m")
print("Before:")
PrintTree(r)
print("After:")
deleteNode(r,5)
PrintTree(r)