def triangle(n):
    if n == 1:
        print('*')
        return
    print('*' * n)
    return triangle(n - 1)

triangle(5)