list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6]
list2 = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

common = set([number for number in list1 if number in list2]) # set to avoid duplicates

print(common)