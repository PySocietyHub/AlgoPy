""" 
En utilisant le passage par adresse, ecrire une fonction ou une procédure 
qui calcul le quotient et le reste de la division entière de deux nombres 
entiers a et b. 
"""

# on utilise une liste pour faire passage par adresse

def solution(nombres):
    reste = nombres[0] % nombres[1]
    quotient = nombres[0] // nombres[1]
    
    return reste, quotient

# Test Cases

print(solution([5, 7])) # (5, 0)
print(solution([8, 4])) # (0, 2)
print(solution([9, 3])) # (0, 3)
print(solution([16, 4])) # (0, 4)