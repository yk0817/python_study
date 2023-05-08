class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		if not self.head:
			self.head = Node(data)
			return
		current = self.head
		while current.next:
			current = current.next
		current.next = Node(data)

a_list = LinkedList()
a_list.append("Tuesday")
a_list.append("Wednesday")
print(a_list)