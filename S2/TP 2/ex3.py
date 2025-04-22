# On interdit l’usage de append , len , sort , reverse , etc.

# list lenght recursive function
def taille_liste(l):
    if not l: # check for empty list
        return 0
    if l == [l[0]]: # check if the list has just one item
        return 1
    return 1 + taille_liste(l[1:]) # keep removing one item until len = 1

print(taille_liste([1, 5, 6, 8, 9])) # 5
print(taille_liste([1, 5, 6, 8, 9, 45, 99, 5, 4])) # 9
print(taille_liste([])) # 0

# list sum recursive function
def sum_liste(l): # same first function approach
    if l == [l[0]]:
        return l[0]
    return l[0] + sum_liste(l[1:])

print(sum_liste([1, 5, 6, 8, 9])) # 29
print(sum_liste([1, 5, 6, 8, 9, 45, 99, 5, 4])) # 182
print(sum_liste([1, 2])) # 3

# display list items in reverse order
def aff_liste_inv(l):
    if l == [l[0]]:
        print(l[0])
        return None
    
    print(f'{l[-1]} -> ', end='')
    return aff_liste_inv(l[:-1])

aff_liste_inv([1, 5, 6, 8, 9]) # 9 -> 8 -> 6 -> 5 -> 1
aff_liste_inv([1, 5, 6, 8, 9, 45, 99, 5, 4]) # 4 -> 5 -> 99 -> 45 -> 9 -> 8 -> 6 -> 5 -> 1
aff_liste_inv([1, 2]) # 2 -> 1