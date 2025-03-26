# Écrire une fonction récursive triangle qui prend un paramètre entier n et affichent un triangle :

def triangle(n):
    if n > 0:
        print('*' * n)
        return triangle(n - 1)
