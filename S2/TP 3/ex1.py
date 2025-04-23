from random import shuffle
from time import time

def bubble_sort(l):
    n = len(l)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if l[j + 1] < l[j]:
                l[j + 1], l[j] = l[j], l[j + 1]
    return l
                

def insertion_sort(l):
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j -= 1
    return l


l1 = [i for i in range(100)] # list of 100 items
shuffle(l1)

l2 = [i for i in range(500)] # list of 500 items
shuffle(l2)

l3 = [i for i in range(1000)] # list of 1000 items
shuffle(l3)

def test_bubble_sort(l):
    nums = l[:] # Copy to avoid modifying original before passing it to the insertion sort function
    start = time()
    bubble_sort(nums)
    end = time()
    print(f'duree de bubble_sort: {end - start}')

def test_insertion_sort(l):
    nums = l[:] 
    start = time()
    insertion_sort(nums)
    end = time()
    print(f'duree de insertion_sort: {end - start}')

# test pour liste a taille 100
test_bubble_sort(l1)
test_insertion_sort(l1)
print('-------------------------------------')

# test pour liste a taille 500
test_bubble_sort(l1)
test_insertion_sort(l1)
print('-------------------------------------')

# test pour liste a taille 1000
test_bubble_sort(l1)
test_insertion_sort(l1)
print('-------------------------------------')

# conclusion :
    # insertion sort is faster than bubble sort