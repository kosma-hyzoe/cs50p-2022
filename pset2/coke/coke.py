PRICE = 50
VALID_COIN_DENOMINATIONS = [25, 10, 5]

due = PRICE
inserted = 0


while inserted < PRICE:
    print("Amount Due: " + str(due))
    coin_value = int(input("Insert coin: "))
    if coin_value in VALID_COIN_DENOMINATIONS:
        due -= coin_value
        inserted += coin_value

print("Change Owed: " + str(inserted - PRICE))
