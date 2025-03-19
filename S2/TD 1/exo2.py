# Ecrire une fonction qui vérifie si un nombre entier A divise un nombre entier B .

def is_divisor(a, b):
    return b % a == 0


# Test Cases

print(is_divisor(1, 5)) # True
print(is_divisor(9, 6)) # False
print(is_divisor(4, 8)) # True
print(is_divisor(16, 3)) # False