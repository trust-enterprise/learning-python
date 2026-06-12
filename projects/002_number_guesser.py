# GUESS A RANDOM NUMBER
from random import randint

random_num = randint(1, 10)

for chance in range(3):
    try:
        print(f"Chance {(chance+1)}/3")
        guessed_num = int(input("guess a number between 1 and 10 (endpoints included): "))
        if not (1<= guessed_num <=10):
            print("enter a valid number in range 1 to 10")
            continue

    except ValueError:
        print("enter a valid number")
        continue
    if guessed_num < random_num:
        print("guessed number is lower")
    elif guessed_num > random_num:
        print("guessed number is higher")
    else:
        print(f"you are correct, the random number is {random_num}")
        exit()

else:
    print(f"chances exhausted; the random number is {random_num}")

