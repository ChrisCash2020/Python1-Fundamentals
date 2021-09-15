priceIsRight = 10

if priceIsRight < 3:
    print("Price is too low!")
elif priceIsRight >= 4 and priceIsRight <= 9:
    print("Price is almost there!")
elif priceIsRight == 10:
    print("Price is exactly that!")
else:
    print("Price is too high!")