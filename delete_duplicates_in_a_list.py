# Pgm to delete duplicates in a list

numbers = [1, 2, 5, 5, 7]
for counts in numbers:
    dup = numbers.count(counts)
    if dup > 1:
        numbers.remove(counts)
print(numbers)