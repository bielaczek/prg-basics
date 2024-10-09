# Enter number: 125
# Binary number: 0b1111101
# Hexadecimal number: 0x7d
import math

number = int(input('enter number: '))
binary_number = bin(number)
hex_number = hex(number)

print(f'number: {number}')
print(f'number in binary: {binary_number}')
print(f'number in hex: {hex_number}')