balance = 20000

def Bank_menu():
    print("Welcome to the Bank Menu")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Exit")

    input_choice = input("Please select an option (1-3): ")

    if input_choice == '1':
        deposit()
    elif input_choice == '2':
        withdraw()
    elif input_choice == '3':
        exit()


def deposit():
    global balance
    amount = float(input("Enter the amount to deposit: "))
    balance += amount
    print(f"Deposit successful. New balance: ${balance:.2f}")
    Bank_menu()

def withdraw():
    global balance
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds. Please try again.")
    else:
        balance -= amount
        print(f"Withdrawal successful. New balance: ${balance:.2f}")
    Bank_menu()

def main():
    while True:
        Bank_menu()

if __name__ == "__main__":
    main()