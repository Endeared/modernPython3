def get_data():
    email_address = input('Enter Email: ')
    password = input('Enter Password: ')

    return email_address, password

email, password = get_data()
print(email + " ][ " + password)