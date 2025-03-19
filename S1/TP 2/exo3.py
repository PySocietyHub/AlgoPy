# Palindrome string

s = str(input('entrez une chaine de characters: '))

i, j = 0, len(s) - 1

while i <= j:
    if s[i] != s[j]:
        print('Faux, cette chaine n est pas palindrome')
        exit()
    i += 1
    j -= 1
print('Vrai, cette chaine est palindrome')