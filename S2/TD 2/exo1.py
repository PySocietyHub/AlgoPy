# Ecrire une fonction récursif permettant de calculer le nième terme de la suite (regarde le pdf):

def suite(n):
    if n < 2:
        return 1
    return 3 * suite(n - 1) + suite(n - 2)


# Test Cases


print(suite(5)) # 142
print(suite(3)) # 13
print(suite(9)) # 16897
print(suite(1)) # 1