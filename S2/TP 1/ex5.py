# 1: Déclarez une variable globale counter
counter = 0

# 2: Créez une fonction increase(n) qui utilise global counter
def increase(n):
    global counter
    counter += n
    return counter

# 3: Ajoutez une variable locale counter dans une autre fonction local_increase(n)
def local_increase(n):
    counter = 0
    counter += n
    return counter

# 4, 5: Test and analyse the 2 functions
print(increase(5)) # increase the global counter
print(local_increase(3)) # use a local counter variable