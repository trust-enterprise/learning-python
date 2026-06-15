# EXPENSE TRACKER PROJECT
from expense import Expense
from pathlib import Path
from currency import get_inr_rate

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
        amount = int(input("enter the expense amount: "))
    except ValueError:
        print("enter a valid amount, retry.")
        exit()
    else:
        description = input("expense made for: ")
        currency = input("preferred currency code (press enter for INR): ").upper()
        if currency == "":
            currency = "INR"
        if not currency == "INR":
            rate = get_inr_rate(currency)
            if rate is None:
                print("enter valid currency code")
                exit()
            amount = amount * rate

        return (
            amount,
            description,
        )


def view_expense():
    if Path("expenses.txt").exists():
        with open("expenses.txt", "r") as f:
            for line in f:
                expense = Expense.from_file_line(line)
                print(expense)
        view_total()
    else:
        print("no data available")


def view_total():
    total = 0
    with open("expenses.txt", "r") as f:
        for line in f:
            description, amount = line.split(",")
            total += float(amount)
        print(f"Total expense is INR {round(total,2)}")


if selection == 1:
    amount, description = add_expense()

    expense = Expense(description, amount)

    with open("expenses.txt", "a") as f:
        f.write(expense.to_file_string() + "\n")

    view_total()

elif selection == 2:
    view_expense()

elif selection == 3:
    print("good bye")
    exit()
else:
    print("enter a valid number")
