number = int(input('Enter decimal number: '))
decimal = number
binary = ''

while number != 1:
    binary += str(number % 2)
    print(number)
    number = number // 2

binary += '1'

print(f'{decimal}(10) = {binary[::-1]}(2)')