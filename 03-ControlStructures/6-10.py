current_price = int(input('Current product price: '))
previous_price = int(input('Previous product price: '))

reduction = 100 - (current_price / previous_price * 100)

if reduction >= 10:
    print(f'Buy the product!!')
    print(f'Product price reduced by {reduction}%')