# exponentiation rapide
def puissance(x, n):
    if n == 1:
        return x
    elif n % 2 == 0:
        return puissance(x * x, n / 2)
    elif n > 2 and n % 2 != 0:
        return x * puissance(x * x, (n - 1) / 2)