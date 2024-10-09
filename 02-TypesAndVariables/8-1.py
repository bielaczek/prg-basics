###
# Calculation of circle area and circumference 
#

# determine radius and PI values
# calculate area 
# calculate circumference 
# display results
import math

radius = float(input('enter radius: '))
area = round(math.pi * radius * radius, 2)
circumference = round(2 * math.pi * radius, 2)

print(f'area of circle: {area}')
print(f'circumferences of circle: {circumference}')