# Ecrire une fonction et une procédure qui calcul de la factorielle de n

def factorielle(n):
    if n == 0:
        return 1
    return n * factorielle(n - 1)

# Test Cases

print(factorielle(5)) # 120
print(factorielle(4)) # 24  
print(factorielle(6)) # 720