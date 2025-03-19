numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

somme = 0
minimum = numbers[0]
maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number
    elif number < minimum:
        minimum = number
    somme += number
    
moyenne = somme / len(numbers)

print(minimum, maximum, moyenne)