# Ré-écrire les fonctions suivantes sous forme récursive et sous forme terminal quand cʼest possible.

""" 
Fonction fun1(n: entier) : entier
Variables s, i: entier
Debut
    s ← 0
    Pour i ← 1 à n Faire
        s = s + i
    Finpour
    Retourner s
FinFonction 
""" 

    
def fun1(n):
    if n == 0:
        return 0
    return n +  fun1(n - 1)


""" 
Fonction fun2(n: entier) : entier
Variables a, b, i: entier
Debut
    a ← 0
    b ← 0
    Pour i ← 1 à n Faire
        a ← a + i
        b ← b + a
    Finpour
    Retourner b
FinFonction 
"""
def fun2(n, a=0, b=0):
    if n == 0:
        return b
    a += n
    b += a
    return fun2(n - 1, a, b)

""" 
Fonction sum(n : entier) : entier
    Si n = 0 Alors
        Retourner 0
    Sinon
        Retourner abs(n) + sum(n+1)
    FinSi
FinFonction 
"""

def sum_recursion(n):
    if n == 0:
        return 0
    if n > 0:
        return abs(n) + sum_recursion(n - 1) # n-1 to prevent infinite recursion calls
    return abs(n) + sum_recursion(n + 1) # for negative numbers

