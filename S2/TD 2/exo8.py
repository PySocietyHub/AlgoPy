""" 
Proposez une fonction récursive qui compte les occurences d'une lettre dans un mot. 
Elle prend deux paramètres, la lettre et le mot. Elle retourne le nombre de fois où cette lettre 
apparaît dans le mot 
"""


def counter(word, letter):
    if len(word) < 1:
        return 0
    return (1 if word[0] == letter else 0) + counter(word[1:], letter)


# Test Cases

print(counter('hiiiii', 'i')) # 5
print(counter('hello', 'l')) # 2
print(counter('mega man', 'e')) # 1
print(counter('try', 'z')) # 0