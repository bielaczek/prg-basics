format24 = input('Enter time (24-hour format): ')

format12 = str(int(format24[0:2]) % 12) + format24[2:5]
print(format12)
print(f'Time in 12-hour format: {format12}pm')