def quick_sort(l):
    if len(l) <= 1: # Base Case
        return l
    
    pivot = l[-1] # choosing the pivot as the last list item (not the best practice)
    
    left = [num for num in l[:-1] if num <= pivot] # left list contains numbers that are smaller than the pivot
    right = [num for num in l[:-1] if num > pivot] # left list contains numbers that are bigger than the pivot
    
    # recursively sort the left and right side
    left = quick_sort(left) 
    right = quick_sort(right)
    
    # group things up and return the final result
    return left + [pivot] + right

# Expérimenter sur une liste quasi triée et un liste inversée : quel impact sur la complexité ?

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Liste quasi triée
l2 = [9, 8, 7, 6, 5, 4, 3, 2, 1] # Liste inversée

print(quick_sort(l1)) # O(n²)
print(quick_sort(l2)) # O(n²)
    