# EXPENSE TRACKER PROJECT
from pathlib import Path

while True:
    try:
        selection = int(
            input(
                "\nselect a number for menu option:\n"
                "1. Add Expense\n"
                "2. View Expenses\n"
                "3. Quit\n"
                "Choice: "
            )
        )
        if not (1 <= selection <= 3):
            print("kindly enter the number from provided menu")
            continue
        break
    except ValueError:
        print("kindly enter a valid number")


def add_expense():
    try:
        amount = int(input("enter the expense amount (INR): "))
    except ValueError:
        print("enter a valid amount, retry.")
        exit()
    else:
        description = input("expense made for: ")
        return amount, description


def view_expense():
    if Path("expenses.txt").exists():
        with open("expenses.txt", "r") as f:
            for line in f:
                print(line, end="")
        view_total()
    else:
        print("no data available")


def view_total():
    total = 0
    with open("expenses.txt", "r") as f:
        for line in f:
            description, amount = line.split(",")
            total += int(amount)
        print(f"Total expense is INR {total}")


if selection == 1:
    amount, description = add_expense()

    with open("expenses.txt", "a") as f:
        f.write(f"{description},{amount}\n")

    view_total()

elif selection == 2:
    view_expense()

elif selection == 3:
    print("good bye")
    exit()
else:
    print("enter a valid number")
