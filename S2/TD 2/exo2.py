"""  
Le triangle de Pascal (Blaise Pascal!) est une présentation des coefficients binomiaux 
sous la forme d'un triangle .
On le définit par récurrence:
"""



def pascal_triangle(n, p):
    if n == p or p == 0:
        return 1
    return pascal_triangle(n-1, p-1) + pascal_triangle(n-1, p)



# Test Cases


print(pascal_triangle(0, 0)) # 1
print(pascal_triangle(3, 1)) # 3
print(pascal_triangle(5, 3)) # 10
print(pascal_triangle(6, 3)) # 20
