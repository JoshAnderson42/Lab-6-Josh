def encode(password):
    encoded = ''
    for num in password:
        encoded += str(int(num) + 3)
    return encoded

if __name__ == '__main__':

    while True:

        #changed
        
        print('\nMenu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        selection = input('\nPlease enter an option: ')

        if selection == '1':
            password = input('Please enter your password to encode: ')
            encoded = encode(password)
            print(encoded)
        elif selection == '2':
            exit()
        elif selection == '3':
            exit()
