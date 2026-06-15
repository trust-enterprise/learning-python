import functions


def main_menu():
    while True:
        try:
            selected_menu = int(
                input(
                    "\nselect a menu number\n"
                    "1. add expense\n"
                    "2. view expense\n"
                    "3. clear expense\n"
                    "4. quit\n"
                    "selected option: "
                )
            )
            if not (1 <= selected_menu <= 4):
                print("enter a menu number in the range 1 to 4")
                continue
        except ValueError as e:
            print("enter a valid menu number", e)
            continue

        if selected_menu == 1:
            functions.add_expense()
        elif selected_menu == 2:
            functions.view_expense()
        elif selected_menu == 3:
            functions.clear_expense()
        else:
            print("good bye")
            exit()


main_menu()
