from time import time

def linear_search(l, x):
    for num in l:
        if num == x:
            return True
    return False

def binary_search(lst, x):
    l, r = 0, len(lst) - 1
    while l <= r:
        middle = (l + r) // 2
        if lst[middle] == x:
            return True
        elif lst[middle] > x:
            r = middle - 1
        else:
            l = middle + 1
    return False
            
def testing(function, lst, x):
    start = time()
    function(lst, x)
    end = time()
    print(f'duree de {function.__name__}: {end - start:.6f} secondes')
            
l1 = [num for num in range(10 ** 3)] # list de 1000 elements
l2 = [num for num in range(10 ** 5)] # list de 100000 elements

print('list de 1000 elements')
testing(binary_search, l1, 50)
testing(linear_search, l1, 50)

print('------------------------')

print('list de 100000 elements')
testing(binary_search, l2, 50)
testing(linear_search, l2, 50)

# Result
    # list de 1000 elements
    # duree de binary_search: 0.000015 secondes
    # duree de linear_search: 0.000009 secondes
    # ------------------------
    # list de 100000 elements
    # duree de binary_search: 0.000012 secondes
    # duree de linear_search: 0.000005 secondes

# Conslusion
    # binary search is faster than linear search in sorted lists