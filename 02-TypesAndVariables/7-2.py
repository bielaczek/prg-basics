###
# A program that checks whether the password length
# read from the keyboard is correct.
#university, peter123, (passwords ok) seven, anna333 (passwords to short)
password = input('Enter password: ')
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')