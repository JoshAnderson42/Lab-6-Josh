def encode(password):
    encoded = ''
    for num in password:
        encoded += str(int(num) + 3)[-1]
    return encoded


if __name__ == '__main__':

    while True:

        #changed again

        print('\nMenu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        selection = input('Please enter an option: ')

        if selection == '1':
            encoded = encode(input('Please enter your password to encode: '))
            print('Your password has been encoded and stored!')
        elif selection == '2':
            print(f'The encoded password is {encoded} and the original password is {''}')
        elif selection == '3':
            exit()
