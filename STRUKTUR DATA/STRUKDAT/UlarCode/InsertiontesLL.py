# Python implementation of above
# algorithm
# Node class
class Node:
	
	# Konstruktor untuk menginisialisasi
	# node object
	def __init__(self, data):
		self.data = data
		self.next = None

# Berfungsi untuk mengurutkan satu per satu
# linked list using insertion
# sort
def insertionSort(head_ref):

	# Inisialisasi daftar tertaut yang diurutkan
	sorted = None

	# Lintasi daftar tertaut yang diberikan
	# dan masukkan setiap simpul untuk diurutkan
	current = head_ref
	while (current != None):
	
		# Simpan berikutnya untuk iterasi berikutnya
		next = current.next

		# Insert current in sorted
		# linked list
		sorted = sortedInsert(sorted,
							current)
		# Update current
		current = next
	
	# Update head_ref to point to
	# sorted linked list
	head_ref = sorted
	return head_ref

# Berfungsi untuk menyisipkan new_node dalam daftar.
# Perhatikan bahwa fungsi ini mengharapkan pointer
# ke head_ref karena ini dapat memodifikasi kepala
# dari daftar tertaut input (mirip dengan Push())
def sortedInsert(head_ref, new_node):
	current = None
	
	# Kasus khusus untuk ujung kepala
	if (head_ref == None or
	(head_ref).data >= new_node.data):
		new_node.next = head_ref
		head_ref = new_node
	
	else:
	
		# Cari simpul sebelum titik
		# of insertion
		current = head_ref
		while (current.next != None and
			current.next.data < new_node.data):	
			current = current.next
		
		new_node.next = current.next
		current.next = new_node
		
	return head_ref

# Utility Functions
# Function to print linked list
def printList(head): 
	temp = head
	while(temp != None):
		print( temp.data, end = " ")
		temp = temp.next
	
# Fungsi utilitas untuk menyisipkan simpul
# di awal daftar tertaut
def push( head_ref, new_data):

	# Allocate node
	new_node = Node(0)

	# Put in the data
	new_node.data = new_data

	# Link the old list off the
	# new node
	new_node.next = (head_ref)

	# Move the head to point to
	# the new node
	(head_ref) = new_node
	return head_ref

# Driver code
j = None
j = push(j, 5)
j = push(j, 20)
j = push(j, 4)
j = push(j, 3)
j = push(j, 30)

print("Linked List before sorting ")
printList(j)

j = insertionSort(j)

print("Linked List after sorting ")
printList(j)

