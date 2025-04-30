n = int(input('entrez la valeur de N: '))
for i in range(1, n + 1):
    print('*' * i)

# recursive approach
def triangle(n):
    if n == 0:
        return
    triangle(n - 1)
    print('*' * n)
    
triangle(n)
