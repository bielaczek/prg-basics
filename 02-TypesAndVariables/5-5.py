# Enter price: 24.72
# Enter discount %: 15
# Price with discount: 21.01
# Reduction: 3.71

price = round(float(input("podaj cene: ")), 2)
discount = float(input("podaj znizke w %: "))

reduction = round(price / 100 * discount, 2)
priceWithDiscount = round(price - reduction, 2)

print("price: ", price)
print("discount: ", discount)
print("price with discount: ", priceWithDiscount)
print("reduction: ", reduction)