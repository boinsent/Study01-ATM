import sys
import time
correct_pin = "1234"

def transact_count():
    another_transact = input("Would you like another transact? [Y/N]")

    if another_transact == "Y":
        return main_menu()
    elif another_transact == "N":
        print("Thank you for using ATM")
        sys.exit()
    else:
        print("Invalid input")
        return transact_count()
def withdraw():
    bal = 5000
    try:
        input_withdraw = int(input("Withdraw amount: "))
        if input_withdraw > bal:
            print("Insufficient amount")
            return transact_count()
    except ValueError:
        print("Invalid input")
        return withdraw()

    updated_balance = bal - input_withdraw

    global global_available_balance
    global_available_balance = updated_balance

    print(f"Your current balance is {updated_balance}")

    return transact_count()

def view_balance():

    print(f"Your balance is: {global_available_balance}")
    return transact_count()

def main_menu():
    print("MAIN MENU")
    print("1. Withdraw")
    print("2. View Balance")
    print("3. Exit")

    select_menu = input(": ")

    if select_menu == "1":
        return withdraw()
    elif select_menu == "2":
        return view_balance()
    elif select_menu == "3":
        print("Thank you for using ATM")
        sys.exit()
    else:
        print("Invalid")
        return main_menu()

def enter_pin():
    count = 0
    while True:
        input_pin = input("Enter pin: ")
        count = count + 1

        if count == 3:
            print("Stop.. please wait")
            time.sleep(5)
            return enter_pin()

        if input_pin != correct_pin:
            print("Incorrect pin")
        else:
            return main_menu()

enter_pin()
