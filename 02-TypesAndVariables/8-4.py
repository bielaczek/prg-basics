###
# A program that reads a SWIFT code from the keyboard
# and displays the bank code and country code.
#BPKOPLPW
swift = input('enter SWIFT code: ')
print(f'Bank Code: {swift[0:4]}')
print(f'Country Code: {swift[4:6]}')