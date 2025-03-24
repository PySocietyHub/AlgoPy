""" 
Un mot est un palindrome si on peut le lire dans les deux sens de gauche à droite et de 
droite à gauche. Exemple KAYAK est un palindrome. Ecrire une fonction récursive permettant de 
vérifier si un mot est palindrome. 
"""

# methode 1
def is_palindrome(word, l=0, r=None): # using the two pointer approach
    if r is None:
        r = len(word) - 1
    if l >= r:
        return True
    if word[l] != word[r]:
        return False
    return is_palindrome(word, l+1, r-1)

print(is_palindrome("racecar"))  # True
print(is_palindrome("python"))   # False 


# methode 2
def est_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return est_palindrome(word[1:-1]) # recursive call after removing the first and last characters.

print(est_palindrome("level"))   # True 
print(est_palindrome("hello"))   # False
