string = '1 '
for i in range(2, 31):
    if i % 3 == 0 and i % 5 == 0:
        string += 'BINGO '
    elif i % 3 == 0:
        string += 'THREE '
    elif i % 5 == 0:
        string += 'FIVE '
    else:
        string += str(i) + ' '

print(string)