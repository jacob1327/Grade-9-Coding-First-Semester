# Write a program that allows the user to type in 5 numerical grades that they have achieved and calculates the average.
# Use a loop to assist with this tas

mark_number = ""
sum_of_numbers = 0
mark = int

for count in range(0, 5):
    if count == 0:
        mark_number = "first"
    elif count == 1:
        mark_number = "second"
    elif count == 2:
        mark_number = "third"
    elif count == 3:
        mark_number = "fourth"
    elif count == 4:
        mark_number = "fifth"

    mark = int(input(f"Enter your {mark_number} mark: "))
    sum_of_numbers = sum_of_numbers + mark
average = str(sum_of_numbers/5)
print(f"Your average mark is {average}")

