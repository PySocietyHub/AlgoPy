n = int(input('entre the number of rows: '))

pascal_triangle = [[1]] # base dyal triangle

for i in range(n): # ghandoro 3la 7sab ch7al mn ster 3tana l user
    triangle_row = [1] # lbidaya dyal triangle
    for j in range(len(pascal_triangle[i]) - 1): # ghandoro 3la ster li9bel bach mnno n9addo ster li3ndna
        triangle_row.append(pascal_triangle[i][j] + pascal_triangle[i][j+1]) # ghanzido kola ra9em m3a li 7dah o nzidoh f ster dyalna
    triangle_row.append(1) # ghadi nsddo ster b 1
    pascal_triangle.append(triangle_row) # ghadi nzido ster 3la triangle


for row in pascal_triangle: # kolla ster mn triangle
    for digit in row: # kolla ra9em f dak ster
        print(f'{digit} ', end='') # ghanktboh ondiro espace
    print() # mora mansaliw mn kolla ster ne9zo l lli tab3o