from Tax_Discount import compute_total


def customer_flow(user):
    print(f"\nWelcome, {user.get('username')}! Let's process your purchase.")
    while True:
        try:
            subtotal = float(input('Enter subtotal amount (or type 0 to logout): ').strip())
        except ValueError:
            print('Please enter a valid numeric subtotal.')
            continue
        if subtotal == 0:
            print('Logging out from customer.')
            break
        location = input('Enter location (state code e.g. NY, CA) for tax calculation: ').strip()
        coupon = input('Enter coupon code (or leave blank): ').strip()
        if coupon == '':
            coupon = None
        result = compute_total(subtotal, location, coupon)
        print('\n--- Receipt ---')
        print(f"Subtotal: ${result['subtotal']:.2f}")
        if result['coupon_valid']:
            print(f"Coupon discount: {result['coupon_discount']}% (valid)")
        elif coupon:
            print('Coupon discount: INVALID code provided')
        else:
            print('No discounts applied.')
        print(f"Total discount applied: {result['total_discount_percent']}%")
        print(f"Discounted total: ${result['discounted_total']:.2f}")
        print(f"Tax rate: {result['tax_rate_percent']}%")
        print(f"Final total: ${result['final_total']:.2f}")
        print('----------------')
        cont = input('Process another purchase? (y/n): ').strip().lower()
        if cont != 'y':
            print('Logging out from customer.')
            break


if __name__ == '__main__':
    customer_flow({'username': 'guest'})
