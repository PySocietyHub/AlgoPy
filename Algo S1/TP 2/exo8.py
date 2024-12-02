numbers = [7, 2, 14, 0, 9, 3, 11, 6, 15, 4, 10, 1, 13, 8, 12, 5]

sorted_numbers = []

while numbers: # while numbers list is not empty
    if min(numbers) not in sorted_numbers: # if the min number of numbers list is not in the sorted list
        sorted_numbers.append(min(numbers)) # we add it to the sorted list
    numbers.remove(min(numbers)) # we remove it from the unsorted list
    
print(sorted_numbers) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]