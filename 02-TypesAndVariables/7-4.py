#Enter tree circumference in cm: 120 
#Tree can be cut down: False
import math

circumference = int(input('enter circumference: '))
diameter = circumference / math.pi

print('diameter: ', diameter)
cutPossible = diameter >= 50

print(f'Tree can be cut down: {cutPossible}')