numbers =[26, 25, 16, 9, 5, 10]

largest_number = numbers[0]

for i in numbers:
    if i > largest_number:
        largest_number = i
print(largest_number)