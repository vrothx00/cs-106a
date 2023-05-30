def add_many_numbers(numbers):
    s = 0
    for i in range(len(numbers)):
        s += numbers[i]
    return s

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = add_many_numbers(numbers)
print(sum_of_numbers)