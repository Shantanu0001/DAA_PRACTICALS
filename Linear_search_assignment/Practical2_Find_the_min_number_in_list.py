numbers = [5, 2, 9, 1, 5, 6]

minimum_number = numbers[0]  

for num in numbers[1:]:
    if num < minimum_number:
        minimum_number = num 

print("The minimum number in the list is:", minimum_number)
