EAN13 = input('Enter EAN-13 article number: ')
if len(EAN13) == 13:
    print(f'Article number is correct')
    print(int(EAN13[0:3]))
    if int(EAN13[0:3]) == 590:
        print(f'Article manufactured in Poland')