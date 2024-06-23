numbers = [5, 2, 9, 1, 5, 6]

maximum_number = numbers[0] 

for num in numbers[1:]:
    if num > maximum_number:
        maximum_number = num  

print("The maximum number in the list is:", maximum_number)
