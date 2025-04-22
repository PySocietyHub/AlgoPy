def strcpy(src: str, dest: str) -> str:
    if src == '': # when we empty the src means all its content is copied to dest so we return it
        return dest
    dest += src[0]
    return strcpy(src[1:], dest) # copying character by character from the start of src

print(strcpy("hello", ""))         # hello
print(strcpy("world", "hello "))   # hello world
print(strcpy("home", "welcome "))  # welcome home
 
 
def strcpm(ch1: str, ch2: str) -> int:
    if len(ch1) != len(ch2):
        return 1
    if ch1 == ch2:
        return 0
    
    return 1 if ch1[0] > ch2[0] or ch1[0] < ch2[0] else strcpm(ch1[1:], ch2[1:])

print(strcpm("apple", "apple"))   # 0
print(strcpm("apple", "apples"))  # 1
print(strcpm("banana", "ban"))    # 1
print(strcpm("apez", "apya"))     # 1


def anagramme(ch1: str, ch2: str) -> bool: 
    if len(ch1) != len(ch2): # if len is different is totally not anagramme
        return False
    if ch1 == '': # Base case when ch1 is empty
        return True
    if ch1[0] not in ch2:
        return False
    return anagramme(ch1[1:], ch2.replace(ch1[0], '', 1)) # We remove the first occurrence of the checked character from ch2

print(anagramme("algorithme", "logarithme")) # True
print(anagramme("chien", "nich"))            # False