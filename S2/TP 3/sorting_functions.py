import random

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

def merge_sort(lst):
    n = len(lst)
    
    if n == 1: # Base Case
        return lst
    
    mid = n // 2
    
    # divide lst to 2 sub-arrays
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])
    l_pointer, r_pointer = 0, 0 # making for each list so we can traverse it's items
    
    sorted_l = [0] * n # a list of 0's in the same lenght of our list where we can store items after merging
    i = 0
    
    # merging process
    while l_pointer < len(l) and r_pointer < len(r):
        if l[l_pointer] < r[r_pointer]:
            sorted_l[i] = l[l_pointer]
            l_pointer += 1
        else:
            sorted_l[i] = r[r_pointer]
            r_pointer += 1
        i += 1
    # in case if L runs out of items and R still got some
    while l_pointer < len(l):
        sorted_l[i] = l[l_pointer]
        l_pointer += 1
        i += 1
        
    # in case if R runs out of items and L still got some
    while r_pointer < len(r):
        sorted_l[i] = r[r_pointer]
        r_pointer += 1
        i += 1
        
    return sorted_l

def quick_sort(l):
    if len(l) <= 1: # Base Case
        return l
    
    pivot = random.choice(l) # randome pivot choice
    
    left = [num for num in l[:-1] if num <= pivot] # left list contains numbers that are smaller than the pivot
    right = [num for num in l[:-1] if num > pivot] # left list contains numbers that are bigger than the pivot
    
    # recursively sort the left and right side
    left = quick_sort(left) 
    right = quick_sort(right)
    
    # group things up and return the final result
    return left + [pivot] + right