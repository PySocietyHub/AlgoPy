# Ecrire un script Python qui test si un nombre de 4 chiffres est un palindrome. « 1221 » est un palindrome

number = input('entrez un nombre: ')

if number == number[::-1]:
    print('Vrai')
else:
    print('Faux')
    