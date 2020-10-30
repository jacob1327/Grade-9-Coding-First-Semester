list_of_names = []
count_number = ""
for count in range(0,5):
    if count == 0:
        count_number = "first"
    elif count == 1:
        count_number = "second"
    elif count == 2:
        count_number = "third"
    elif count == 3:
        count_number = "fourth"
    elif count == 4:
        count_number = "fifth"
    list_of_names.append(input(f"Enter the {count_number} name: "))

print("Your names are: ")
for names in list_of_names:
    print(names)
