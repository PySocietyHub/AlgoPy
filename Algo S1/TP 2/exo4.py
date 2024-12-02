# based on the first question of project euler
somme = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        somme += i
    
print(somme) # 234168