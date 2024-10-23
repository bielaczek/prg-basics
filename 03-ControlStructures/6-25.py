PIN = '0805'
tries = 0

while True:
    code = input(f'Enter PIN code: ')
    if code == PIN:
        print('Correct')
        break
    else:
        print('Incorrect...')
        tries += 1
        if tries > 2:
            print('Sorry, your payment card has been blocked')
            break