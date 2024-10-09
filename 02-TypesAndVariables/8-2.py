###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# input celcius from user
celcius = float(input('enter celcius: '))

# calculate fahrenheit and kelvin
fahrenheit = celcius * 9 / 5 + 32
kelvin = celcius + 273.15

# display results
print(f'celcius: {celcius}')
print(f'fahrenheit: {fahrenheit}')
print(f'kelvin: {kelvin}')