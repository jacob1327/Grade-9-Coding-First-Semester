# Write a program that allows the user to have 10 attempts at guessing a whole number between 0 and 20 (inclusive).
# You are to give a polite error message when the guess is incorrect,
# but also tell the user to guess “higher” or “lower”.
import random
# import random module to generate a random number
secret_number = (random.randint(0, 21))
count_number = ""
print("Hello! You have 10 attempts to guess a whole number between 0 and 20 inclusive.")
for attempt in range(0, 10):
    # define count numbers for whichever # guess the attempt has been looped for(more organized)
    if attempt == 0:
        count_number = "first"
    elif attempt == 1:
        count_number = "second"
    elif attempt == 2:
        count_number = "third"
    elif attempt == 3:
        count_number = "fourth"
    elif attempt == 4:
        count_number = "fifth"
    elif attempt == 5:
        count_number = "sixth"
    elif attempt == 6:
        count_number = "seventh"
    elif attempt == 7:
        count_number = "eighth"
    elif attempt == 8:
        count_number = "ninth"
    elif attempt == 8:
        count_number = "tenth"
    try_number = 9 - attempt
    guess = int(input(f"Enter your {count_number} guess: "))
    if guess == secret_number:
        print("You guessed the correct number!!! Congratulations ")
        break
    elif guess > secret_number:
        print(f"Sorry, your guess is GREATER than the secret number. You have {try_number} tries left\n")
        continue
    elif guess < secret_number:
        print(f"Sorry, your guess is LESS than the secret number. You have {try_number} tries left\n")
        continue


