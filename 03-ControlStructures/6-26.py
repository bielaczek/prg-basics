number = 7
while number >= 0:
    print(number, end=' ')
    number += 1
    while number % 3 != 1:
        print(number, end=' ')
        number += 1
    print('\n')
    number = number - 6
