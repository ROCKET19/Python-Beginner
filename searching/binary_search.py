def search(list_array, number):
    count = 1
    for i in list_array:
        if i == number:
            return count
        count += 1