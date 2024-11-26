""" 
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1 
"""
n = int(input('entre the number of rows: '))

pascal_triangle = [[1]]

for i in range(n):
    triangle_row = [1]
    for j in range(len(pascal_triangle[i]) - 1):
        triangle_row.append(pascal_triangle[i][j] + pascal_triangle[i][j+1])
    triangle_row.append(1)
    pascal_triangle.append(triangle_row)


for row in pascal_triangle:
    for digit in row:
        print(f'{digit} ', end='')
    print()