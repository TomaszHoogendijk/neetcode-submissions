def add_two_numbers() -> int:
    numbers = input()
    numbers_split = numbers.split(",")
    total = 0
    for number in numbers_split:
        total += int(number)
    return total
        




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
