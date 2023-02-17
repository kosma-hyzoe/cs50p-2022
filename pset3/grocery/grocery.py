def main():
    groceries = {}

    while True:
        try:
            item = input()

            if item == "":
                break

            groceries[item] = groceries[item] + 1 if item in groceries else 1
        except EOFError:
            break

    print_groceries(groceries)
    return


def print_groceries(groceries: dict):
    for item, amount in sorted(groceries.items()):
        print(f"{amount} {item.upper()}")


main()
