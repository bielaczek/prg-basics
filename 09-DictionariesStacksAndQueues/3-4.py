import queue

def converte_to_binary(number):
    print(f'Natural number: {number}')
    binary = queue.LifoQueue()
    while number != 0:
        binary.put(number % 2)
        number = number // 2

    binary_number = ''
    while not binary.empty():
        binary_number += str(binary.get())
    
    print(f'Binary number: {int(binary_number)}')

converte_to_binary(155)
    