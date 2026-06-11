"""Bill Split Calculator.
Asks for total bill amount, number of people, and tip percentage.
Calculates tip amount, total bill, and amount per person.
"""


def get_positive_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = float(value)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if number <= 0:
            print("Value must be greater than 0.")
            continue

        return number


def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if number <= 0:
            print("Value must be at least 1.")
            continue

        return number


def get_tip_percentage():
    options = {
        "1": 10,
        "2": 15,
        "3": 20,
        "4": None,
    }
    prompt = (
        "Choose a tip percentage:\n"
        "  1) 10%\n"
        "  2) 15%\n"
        "  3) 20%\n"
        "  4) Custom percentage\n"
        "Enter the number of your choice: "
    )

    while True:
        choice = input(prompt).strip()
        if choice not in options:
            print("Please choose 1, 2, 3, or 4.")
            continue

        if options[choice] is not None:
            return float(options[choice])

        custom_tip = input("Enter a custom tip percentage (for example, 18 for 18%): ").strip()
        try:
            percentage = float(custom_tip)
        except ValueError:
            print("Please enter a valid number for the tip percentage.")
            continue

        if percentage < 0:
            print("Tip percentage cannot be negative.")
            continue

        return percentage


def format_currency(amount):
    return f"${amount:,.2f}"


def print_receipt(bill_amount, tip_percentage, tip_amount, total_amount, people, per_person):
    print("\n===== Bill Split Receipt =====")
    print(f"Bill amount:        {format_currency(bill_amount)}")
    print(f"Tip percentage:     {tip_percentage:.1f}%")
    print(f"Tip amount:         {format_currency(tip_amount)}")
    print(f"Total bill:         {format_currency(total_amount)}")
    print(f"Number of people:   {people}")
    print(f"Amount per person:  {format_currency(per_person)}")
    print("==============================\n")


def main():
    print("Welcome to the Bill Split Calculator!")

    bill_amount = get_positive_float("Enter the total bill amount: $")
    people = get_positive_int("Enter the number of people: ")
    tip_percentage = get_tip_percentage()

    tip_amount = bill_amount * tip_percentage / 100
    total_amount = bill_amount + tip_amount
    per_person = total_amount / people

    print_receipt(bill_amount, tip_percentage, tip_amount, total_amount, people, per_person)


if __name__ == "__main__":
    main()
