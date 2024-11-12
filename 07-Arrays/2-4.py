###
# Prints some array elements
# #

# last value
# last but one value (do not use negative index values)
# sum of the first and last value
# middle value
# all array values separated by a single space (use a loop statement)

import math
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('First + Last value', arr[0] + arr[-1])
print(arr[math.floor(len(arr)/2)])

for number in arr:
    print(number,end=" ")