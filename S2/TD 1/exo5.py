""" 
Ecrire un algorithme qui, parmi n entiers naturels, calcul la somme et le 
produit des racines carrées des entiers carrés parfaits. Ensuite il vérifie si la 
somme et le produit sont des carrés parfaits.
"""
from math import isqrt

def is_perfect_square(n): 
    root = isqrt(int(n))
    return root * root == n


def solution(nums):
    somme = 0
    produit = 1
    
    for num in nums:
        # 1. Identifier les carrés parfaits
        if is_perfect_square(num): 
            # 2. Calculer la somme et le produit des racines carrées
            somme += isqrt(num)
            produit *= isqrt(num)
            
    # 3. Vérifier si la somme et le produit sont des carrés parfaits
    if is_perfect_square(somme):
        print(f'la somme {somme} est un carré parfait')
    else:
        print(f'La somme {somme} n\'est pas un carré parfait')
        
    if is_perfect_square(produit):
        print(f'le produit {produit} est un carré parfait')
    else:
        print(f'Le produit {produit} n\'est pas un carré parfait')
    
    
# Test Cases
solution([1, 4, 9, 16, 25]) 
print('--------------------------------------')
solution([5])
print('--------------------------------------')
solution([100, 400, 900, 1600])
print('--------------------------------------')
solution([0, 1, 4, 9])