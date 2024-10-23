height = 1
str = ''
for i in range (5):
    for j in range (height):
        str += '*'
    print(str)
    str = ''
    height += 1

height = height - 2

for i in range (4):
    for j in range (height):
         str += '*'
    print(str)
    str = ''
    height -= 1