list_of_numbers = []


def adding_to_list():
    number_of_numbers = 5
    order = 0
    suffix = ""
    while number_of_numbers > 0:
        number_of_numbers = number_of_numbers - 1
        order = order + 1
        if order == 1:
            suffix = "st"
        elif order == 2:
            suffix = "nd"
        elif order == 3:
            suffix = "rd"
        elif order == 4 or 5:
            suffix = "th"
        list_of_numbers.append(int(input(f"Enter the {order}{suffix} number of the list: ")))


adding_to_list()
print(list_of_numbers)

sum_of_numbers = 0
for numbers in list_of_numbers:
    numbers = numbers ** 2
    sum_of_numbers = sum_of_numbers + numbers

print(f"The sum of the squares of the numbers in the list is {sum_of_numbers}!")
