#
#   qsort code and a partition function.
#
#   Modify the code so that it returns the number of compares and the number of moves.
#
def partition(lst, lo, hi):
    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        
    print(hi)
    return hi

def rec_qsort(lst, lo, hi):
    if lo < hi:
        pivot = partition(lst, lo, hi)
        print(pivot)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)

def qsort(lst):
    rec_qsort(lst, 0, len(lst) - 1)

import sys
from qsort import qsort

def main():
    # Read each test case
    line = sys.stdin.readline()
    items = line.strip().split()
  #  print(items)
    
    orig = list(items)
  #  print(orig)

    #print(items)
    result = qsort(items)
    if items != sorted(orig):
        print("The list is not sorted.")
    else:
        print(result)

if __name__ == "__main__":
    main()
