list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6]
list2 = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

common = [number for number in list1 if number in list2] # tous les nombres qui se trouve dans la list1 et 2

if common: # si la liste est plein (au minimum un character)
    print('Vrai')
    exit()
print('False') # si la liste est vide 
