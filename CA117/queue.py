import LinkedList

class Queue:
	def __init__(self):
		self.linkedlist = LinkedList.LinkedList()

	def enqueue(self, item):
		self.linkedlist.addlast(item)

	def dequeue(self):
		return self.linkedlist.remove()

	def is_empty(self):
		return self.linkedlist.is_empty()
