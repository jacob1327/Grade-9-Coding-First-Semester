
# Write a program that allows the user to have 5 attempts at guessing a password.
# You are to give a polite error message when the password is entered incorrectly.
print("Hello, you have 5 attempts to guess the password!")
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
    tries = 4 - count
    print(input(f"Enter your {count_number} password guess: "))
    print(f"Sorry the password was incorrect you have {tries} tries left")