PRICE = 50
due = PRICE
inserted = 0

while inserted < PRICE:
    print("Amount Due: " + str(due))
    coin_value = int(input("Insert coin: "))
    due -= coin_value
    inserted += coin_value

print("Change Owned: " + str(inserted - PRICE))