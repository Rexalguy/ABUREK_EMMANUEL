from Tax_Discount import TAX_RATES, COUPONS


def admin_menu():
    while True:
        print('\nAdmin Menu')
        print('1. View tax rates')
        print('2. View coupons')
        print('3. View discount policy')
        print('4. Logout')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            print('\nTax rates by location:')
            for k, v in TAX_RATES.items():
                print(f' - {k}: {v}%')
        elif choice == '2':
            print('\nAvailable coupon codes:')
            for code, pct in COUPONS.items():
                print(f' - {code}: {pct}%')
        elif choice == '3':
            print('\nDiscount policy:')
            print(' - No tier/subtotal discounts apply. Discounts come from coupons only.')
            print(' - Available coupons are shown in option 2.')
        elif choice == '4':
            print('Logging out from admin.')
            break
        else:
            print('Invalid option.')


if __name__ == '__main__':
    admin_menu()
