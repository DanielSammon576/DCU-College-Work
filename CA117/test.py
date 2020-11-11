def count(self):
	return recurs_count(self.head)

def recurs_count(self, ptr):
	if ptr == None:
		return 0
	else:
		return 1 + recurs_count(ptr.next)



def present(self, x):
	return recurs_present(self.head, x)

def recurs_present(self.head, x):
	if self.head == None:
		return False
	elif self.head == x:
		return True
	else:
		return recurs_present(self.head.next, x)


def largest(self):
	ptr = self.head
	return recurs_largest(ptr)

def recurs_largest(self, ptr):
	if ptr.next == None:
		return ptr.item
	themax = max(ptr, ptr.next.item)
	return max(themax, recurs_largest(ptr.next))



def duplicates(self):
	ptr = self.head
	return recurs_duplicates(ptr)

def recurs_duplicates(self, ptr):
	if ptr != None:
		if ptr.next != None:
			return ptr == ptr.next.item or recurs_duplicates(ptr.next)
		return False




#TREES Examples

    def recursive_count(self, ptr):
        if ptr == None:  # Base Case
            return 0
        else:
            return(1 + self.recursive_count(ptr.left) + self.recursive_count(ptr.right))
                
    def count(self):
        return self.recursive_count(self.root)



    def count(self, lo, hi):
        return self.recurs_count_lo_hi(self.root, lo, hi)

    def recurs_count_lo_hi(self, ptr, lo, hi):
        if ptr == None:
            return 0
        elif (lo <= ptr.item) and (ptr.item <= hi):
            return(1 + self.recurs_count_lo_hi(ptr.left, lo, hi) + self.recurs_count_lo_hi(ptr.right, lo, hi))
        elif lo <= ptr.item:
            return(0 + self.recurs_count_lo_hi(ptr.left, lo, hi))
        else:
            return(0 + self.recurs_count_lo_hi(ptr.right, lo,hi))



    def height(self):
        return self.recursive_height(self.root)

    def recursive_height(self, ptr):
        if ptr == None:
            return 0
        else:
            return max(1 + self.recursive_height(ptr.left), 1 + self.recursive_height(ptr.right))

    def total(self):
        return self.total_recursive(self.root)

    def total_recursive(self, ptr):
        if ptr == None:
            return 0
        else:
            return (ptr.item + self.total_recursive(ptr.left) + self.total_recursive(ptr.right))

    def count_leaves(self):
        return self.recursive_count_leaves(self.root)

    def recursive_count_leaves(self, ptr):
        if ptr == None:
            return 0
        if ptr.left == None and ptr.right == None:
            return 1
        else:
            return self.recursive_count_leaves(ptr.left) + self.recursive_count_leaves(ptr.right)


#AVL Trees

def in_order(self):
    print(self.rec_in_order(self.root, lst=[]))

def rec_in_order(self, ptr, lst):
    if ptr:
        self.rec_in_order(ptr.left, lst)
        lst.append(str(ptr.item))
        self.rec_in_order(ptr.right, lst)
    return(' '.join(lst) + ' ')


def pre_order(self):
    print(self.rec_pre_order(self.root, lst=[]))

def rec_pre_order(self, ptr, lst):
    if ptr:
        lst.append(str(ptr.item))
        self.rec_pre_order(ptr.left, lst)
        self.rec_pre_order(ptr.right, lst)
    return(' '.join(lst) + ' ')

def post_order(self):
    print(self.rec_post_order(self.root, lst=[]))

def rec_post_order(self, ptr, lst):
    if ptr:
        self.rec_post_order(ptr.left, lst)
        self.rec_post_order(ptr.right, lst)
        lst.append(str(ptr.item))
    return(' '.join(lst) + ' ')


def is_avl(bst):
    if bst.height()  < 3:
        return True
    ptr = bst.root
    if ptr.left != None and ptr.right != None:
        return True
    return False



#HASHING 


