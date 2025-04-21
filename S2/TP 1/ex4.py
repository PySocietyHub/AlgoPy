# 1: wrtie functions
def append_item(lst, item):
    lst.append(item)
    
def increment(n):
    n += 1
    return n

# 2: define list a and int b
a = [1, 2]
b = 5

print(f'a: {a} \nb: {b}') # 3: print a, b before and after functions call

append_item(a, 3)
increment(b)

print(f'a: {a} \nb: {b}')

# 4: Expliquez pourquoi a est modifié tandis que b reste inchangé.
# because a (list) is passed by address but b (int) is passed by value, so the global b stays the same

# 5: Proposez une version de append_item qui ne modifie pas la liste d’origine mais en renvoie une nouvelle.
def new_append_item(lst, item):
    new_list = lst
    new_list.append(item)