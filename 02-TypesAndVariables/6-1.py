###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Jan'  
surname = 'Bielecki'
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {characters_in_name + len(surname) + 1}')