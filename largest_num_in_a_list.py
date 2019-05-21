numbers = [1, 2, 3, 5, 78, 34]
largest_num = numbers[0]
for count in numbers:
    if count > largest_num:
        largest_num = count
print(f"The Largest number in the list is {largest_num}")

