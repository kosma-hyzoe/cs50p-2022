import inflect

p = inflect.engine()
names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        break

joined_names = p.join(names)

print("Adieu, adieu, to " + joined_names)