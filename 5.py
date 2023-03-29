def count_copules(numbers):
    numbers = numbers.split(" ")
    counter = 0
    for i in range(0, len(numbers)):
        _numbers = numbers.copy()
        _numbers.remove(numbers[i])
        for j in _numbers:
            if numbers[i] == j:
                counter += 1
    return int(counter / 2)


print(count_copules("1 1 1 1 1"))
