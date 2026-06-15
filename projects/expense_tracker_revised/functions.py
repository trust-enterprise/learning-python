import requests
from pathlib import Path

expense_file = Path("expense.txt")


def add_expense():
    description = input("expense made for: ")
    try:
        amount_original = float(input("expense amount in original currency: "))
        amount_INR = 0
    except ValueError as e:
        print("enter a valid amount", e)
        return

    else:
        if amount_original < 0.5:
            print("amount has to be greater than 0")
            return
        currency = input(
            "enter the currency code for transaction (if INR, press Enter): "
        ).upper()

        if currency in ("", "INR"):
            currency = "INR"
            amount_INR = amount_original
        else:
            amount_INR = get_rate_converter(currency)
            if amount_INR is None:
                print("currency could not be converted")
                return
        with open(expense_file, "a") as f:
            f.write(f"{description},{amount_original},{currency},{amount_INR}\n")

        view_total()


def get_rate_converter(currency_code):
    try:
        response = requests.get(
            f"https://api.exchangerate-api.com/v4/latest/{currency_code}", timeout=5
        )
        response.raise_for_status()
        data = response.json()

        print("status code: ", response.status_code)
        return data["rates"]["INR"]
    except requests.RequestException as e:
        print("request could not be completed", e)
        return None


def view_total():
    try:
        total = 0
        with open(expense_file, "r") as f:
            for line in f:
                description, amount_original, currency, amount_INR = line.strip().split(
                    ","
                )
                total += float(amount_INR)
        print(f"total expense: INR {round(total,2)}")
    except FileNotFoundError as e:
        print("no data available", e)
        return


def view_expense():
    try:
        with open(expense_file, "r") as f:
            for line in f:
                description, amount_original, currency, amount_INR = line.strip().split(
                    ","
                )
                print(f"{description} - {amount_original} {currency}: {amount_INR} INR")

        view_total()
    except FileNotFoundError as e:
        print("no data available", e)
        return


def clear_expense():
    try:
        Path(expense_file).unlink()
        print("expense cleared successfully")
    except FileNotFoundError as e:
        print("no expense available to clear", e)
        return
