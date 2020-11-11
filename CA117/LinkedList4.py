#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

    def __str__(self):
        return str(self.item)

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self, item, next):
        self.item = item
        self.next = next

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
        
    def after(self, item):
        ptr = self.head
        while ptr != None:
            if item == str(ptr):
                return str(ptr.next)
            else:
                ptr = ptr.next
        return None

    def before(self, item):
        pilly = self.head
        if pilly == None:
            return None
        while pilly != None:
            if str(pilly.next) == item:
                return str(pilly)
            else:
                pilly = pilly.next
        return None
