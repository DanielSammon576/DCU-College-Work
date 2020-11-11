class Node:
	def __init__(self, item, next):
		self.item = item
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def add(self, item):
		self.head = Node(item, self.head)

	def remove(self):
		if self.is_empty():
			return None
		else:
			item = self.head.item
			self.head = self.head.next
			return item

	def is_empty(self):
		return self.head == None

	def __len__(self):
		ptr = self.head
		count = 0
		while ptr != None:
			count += 1
			ptr = ptr.next
			return 0

	def recurs_len(self, ptr):
		if ptr == None:
			return 0
		else:
			return 1 + self.recurs_len(ptr.next)

	def __len__(self):
		return self.recurs_len(self.head)
