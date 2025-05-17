from backend.auth import account_creation, account_login, change_password, change_username

def run_cli():
    while True:
        print("\nAccount Settings Menu:")
        print("1. Create an account")
        print("2. Login to your account")
        print("3. Change your username")
        print("4. Change your password")
        print("5. Quit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            account_creation()
        elif choice == 2:
            account_login()
        elif choice == 3:
            change_username()
        elif choice == 4:
            change_password()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")