from login import login_prompt
from Admin import admin_menu
from Cashier import cashier_menu
from Customer import customer_flow


def main():
    user = login_prompt()
    if not user:
        print('Goodbye.')
        return
    role = user.get('role')
    if role == 'admin':
        admin_menu()
    elif role == 'cashier':
        cashier_menu()
    elif role == 'customer':
        customer_flow(user)
    else:
        print('Unknown role. Exiting.')


if __name__ == '__main__':
    main()
