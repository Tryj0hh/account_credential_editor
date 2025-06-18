import sys

def show_interface_options():
    print("Welcome to the Account Management System")
    print("Select interface:")
    print("1. Command Line Interface (CLI)")
    print("2. Web Interface (Flask)")
    print("3. Exit")

def main():
    while True:
        show_interface_options()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            import src.cli as cli
            cli.run_cli()
            break
        elif choice == 2:
            print('We are still working on this!')
        elif choice == 3:
            print("Exiting. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()