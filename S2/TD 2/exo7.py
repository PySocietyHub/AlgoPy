""" 
Proposez une fonction récursive somme qui calcule la somme des éléments d'une liste d'entiers 
passée en paramètre. On supposera que la somme d'une liste vide est 0. 
"""

def recursive_sum(nums, n=None):
    if n is None:
        n = len(nums) - 1
    if n < 0:
        return 0
    return nums[n] + recursive_sum(nums, n - 1)