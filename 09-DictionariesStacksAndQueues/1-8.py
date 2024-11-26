price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

sum_before = 0
sum_after = 0

for key, value in price_list.items():
    print(f'{key} : {value}')
    sum_before += value
print(f'Sum before discount: {round(sum_before, 2)}')

for key, value in price_list.items():
    value = value * 9 / 10
    sum_after += value
    print(f'{key} : {round(value, 2)}')

print(f'Sum after discount: {round(sum_after, 2)}')