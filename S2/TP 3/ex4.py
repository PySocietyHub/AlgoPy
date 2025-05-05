from  sorting_functions import bubble_sort, insertion_sort, merge_sort, quick_sort
from random import shuffle
from time import time


l1 = [i for i in range(1000)]
shuffle(l1)
l2 = [i for i in range(10000)]
shuffle(l2)


def test_functions(*args, **kwargs):
    lst = kwargs.get('lst')
    for function in args:
        lst_copie = lst[:]
        start = time()
        function(lst_copie)
        end = time()
        print(f'duree de {function.__name__}: {end - start:.6f} secondes')
        
print('list of 1000 elements:')
test_functions(bubble_sort, insertion_sort, merge_sort, quick_sort, lst=l1)
print('----------------------------')
print('list of 10000 elements:')
test_functions(bubble_sort, insertion_sort, merge_sort, quick_sort, lst=l2)

# Resultat:
    # list of 1000 elements:
    # duree de bubble_sort: 0.064861 secondes
    # duree de insertion_sort: 0.041996 secondes
    # duree de merge_sort: 0.002025 secondes
    # duree de quick_sort: 0.001679 secondes
    # ----------------------------
    # list of 10000 elements:
    # duree de bubble_sort: 7.229071 secondes
    # duree de insertion_sort: 4.626906 secondes
    # duree de merge_sort: 0.029328 secondes
    # duree de quick_sort: 0.020607 secondes