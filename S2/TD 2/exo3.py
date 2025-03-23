# 1. Ecrire une fonction qui calcule le maximum de 2 nombres réels

def max_of_two(a, b):
    return a if a > b else b


# 2. Ecrire une fonction récursive qui calcule le maximum de 3 nombres réels en utilisant la fonction de 1.

def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))


# 3. Ecrire une fonction récursive  qui calcule le maximum de 4 nombres réels en utilisant la fonction de 1.

def max_of_four(a, b, c, d):
    return max_of_two(max_of_two(a, b), max_of_two(c, d))

# 4. La fonction est-elle récursive ? # Non