first = 0
second = 1

print(first, second, end=' ')
for i in range (29):
    sum = first + second
    print(sum, end=' ')
    first = second
    second = sum