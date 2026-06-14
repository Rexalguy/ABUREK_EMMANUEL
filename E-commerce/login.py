import time
from getpass import getpass

USERS = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'customer': {'password': 'customer123', 'role': 'customer'},
    'cashier': {'password': 'cashier123', 'role': 'cashier'},
}


def login_prompt():
    print('Welcome to the E-commerce platform. Type "exit" to quit.')
    while True:

        #Maximum of 3 login attempts before lockout
        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            username = input('Username: ').strip()
            if username.lower() == 'exit':
                return None
            password = getpass('Password: ')
            user = USERS.get(username)
            if user and password == user['password']:
                print(f'Login successful. Role: {user["role"]}')
                return {'username': username, 'role': user['role']}
            else:
                attempts += 1
                remaining = max_attempts - attempts
                print(f'Invalid credentials. Attempts remaining: {remaining}')
        # after 3 failed attempts
        print('Too many failed attempts. Login portal locked for 60 seconds.')
        time.sleep(60)
        print('You may try logging in again.')


if __name__ == '__main__':
    login_prompt()
