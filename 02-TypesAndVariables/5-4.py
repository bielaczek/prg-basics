# Amount  : 15.84
# VAT 23% :  3.64

amount = round(float(input("podaj cene")), 2)
vat = round(amount * 23 / 100, 2)

print("amount :", amount)
print("VAT :", vat)