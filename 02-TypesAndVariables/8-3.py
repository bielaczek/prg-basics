###
# A program that displays your height both in cm and in feet and inches.
#
cm = 170
feet = round(cm / 30.48, 2)
inches = round(cm / 2.54, 2)
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')