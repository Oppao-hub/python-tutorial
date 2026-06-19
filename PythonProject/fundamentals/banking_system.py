def show_balance(balance):
    print(f"Current Balance: ₱{balance:.2f}")

def deposit(balance):
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("Invalid amount.")
        return 0
    else:
        return amount

def withdraw(current_balance):
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount < 0:
        print("Invalid amount.")
        return 0
    elif amount > current_balance or amount == 0:
        print("Insufficient funds.")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter you choice (1-4): ")

        match(choice):
            case '1':
                show_balance(balance)
            case '2': 
                balance += deposit(balance)
            case '3':
                balance -= withdraw(balance)
            case '4':
                is_running = False
                print("Thank you. Goodbye!")
            case _:
                print("Invalid choice. Please try again!")

        print()

if __name__ == '__main__':
    main()