amount = int(input('Number of products purchased: '))
price = float(input('Product price: '))

if amount > 2:
    print(f'Amount to pay: {2 * price +  (amount - 2) * price * 3 / 4}')
else:
    print(f'Amount to pay: {amount * price}')