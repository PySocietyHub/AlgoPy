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
        
l1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
l2 = [5, 2, 8, 6, 3, 12, 54, 99, 120]

print(merge_sort(l1)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(merge_sort(l2)) # [2, 3, 5, 6, 8, 12, 54, 99, 120]