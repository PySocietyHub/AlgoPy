# ax² + bx + c

a = int(input('entrez la valeur de a: '))
b = int(input('entrez la valeur de b: '))
c = int(input('entrez la valeur de c: '))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b - delta ** 0.5) / 2 * a
    x2 = (-b + delta ** 0.5) / 2 * a
    print(f'cette fonction admet 2 solutions: {x1} et {x2}')
elif delta == 0:
    x = - b / 2 * a
    print(f'cette fonction admet une seule solution: {x}')
else:
    print('Cette fonction n admet aucun solution')