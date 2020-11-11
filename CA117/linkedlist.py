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
        count = 0
        if ptr == None:
            return count
        else:
            if not int(ptr.item) % 2:
                count += 1
            return recurs_len_even(ptr.next)

    def count_even(self):
        return self.recurs_len_even(self.head())

import sys

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    ll = LinkedList()
    
    for num in nums:
        ll.add(num)
    
    print(even_count(ll))

if __name__ == "__main__":
    main()