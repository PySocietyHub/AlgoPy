numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 5, 7, 9, 2]

stack = []

for number in numbers:
    if number not in stack:
        stack.append(number)

print(stack)