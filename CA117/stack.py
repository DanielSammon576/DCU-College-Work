import LinkedList

class Stack:

	def __init__(self):
		self.linkedlist = LinkedList.LinkedList()

	def push(self, item):
		self.linkedlist.add(item)

	def pop(self):
		return self.linkedlist.remove()

	def is_empty(self):
		return self.linkedlist.is_empty()
