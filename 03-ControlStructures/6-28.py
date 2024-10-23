n = int(input('Enter n: '))
string = '2 '

primes = 1
number = 3

while primes < n:
    prime = True
    for i in range (2, number):
        if number % i == 0:
            prime = False
            break
    
    if prime:
        primes += 1
        string += str(number)
        string += ' '
    number += 1
    
print(string)