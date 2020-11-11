#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

#
#   LinkedList class
#
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
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def recurs_len_even(self, ptr):
        #count = 0
        if ptr == None:
            return 0
        else:
            if not int(ptr.item) % 2:
                #count += 1
                return 1 + recurs_len_even(ptr.next)
            else:
                return recurs_len_even(ptr.next)

    def even_count(self):
        return self.recurs_len_even(self.head())
