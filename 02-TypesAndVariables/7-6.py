#Enter vehicle speed: 158
#Speed is valid: False

speed = int(input('ENter vehicle speed: '))
validSpeed = speed > 39 and speed < 141
print(f'SPeed is valid: {validSpeed}')