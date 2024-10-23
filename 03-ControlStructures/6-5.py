# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN

time = int(input('enter how many hours car was parked: '))

if time <= 2:
    fee = time * 5
elif time <= 6:
    fee = time * 15
elif time > 6:
    fee = time * 20

print(f'the fee is {fee}')