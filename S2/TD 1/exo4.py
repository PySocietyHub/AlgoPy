""" 
Ecrire une fonction vérifiant si un nombre entier naturel est un carré parfait, 
en utilisant seulement les opérateurs de base, et renvoie sa racine dans le cas favorable.
Indication :  
   n est un carré parfait sʼil existe un entier i tel que n =i×i
"""

def is_perfect_square(n):
    if n < 0: # squares can't be negative
        return False
    
    root = n ** 0.5 
    return root * root == n

print(is_perfect_square(25)) # True
print(is_perfect_square(3))  # False
print(is_perfect_square(19)) # False
print(is_perfect_square(16)) # True