from Tax_Discount import COUPONS


def cashier_menu():
    while True:
        print('\nCashier Menu')
        print('1. View discount policy')
        print('2. View coupons')
        print('3. Logout')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            print('\nDiscount policy:')
            print(' - Discounts come from coupons only.')
            print(' - Available coupons are shown in option 2.')
        elif choice == '2':
            print('\nAvailable coupons:')
            for code, pct in COUPONS.items():
                print(f' - {code}: {pct}%')
        elif choice == '3':
            print('Logging out from cashier.')
            break
        else:
            print('Invalid option.')


if __name__ == '__main__':
    cashier_menu()
