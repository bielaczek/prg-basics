products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

counter = 0
for key, value in products.items():
    counter += value
    print(f'{key} : {value}')

print(f'sum of products: {counter}')