# he distance to the horizon depends on the height of the observer above the ground. The higher you are, the farther away the horizon is. For most situations, you can use the following formula:

# d = 3.57 × √h

# Where:

# d is the distance to the horizon in kilometers
# h is the height of the observer in meters
# Write a program that calculates the distance to the horizon from a height given in meters from the keyboard. Then, using the program, calculate the distance to the horizon in km when:

# You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m). You have probably been to the seaside many times. Can you believe that the horizon is only a few kilometers away?
#You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.

import math
PerHeight = input('Enter your height in m: ')
LocHeight = input('Enter localization height in m: ')
LocHeight = float(LocHeight)
PerHeight = float(PerHeight)
d1 = 3.57 * (math.sqrt(PerHeight))
d2 = 3.57 * (math.sqrt(LocHeight + PerHeight))
print(str(d1) + ' km on beach')
print(str(d2) + ' km in hotel')
