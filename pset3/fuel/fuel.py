while True:
    try:
        fraction = input("Fraction: ")
        if "." in fraction or "," in fraction:
            continue

        denominator, divisor = fraction.split("/")
        denominator, divisor = int(denominator), int(divisor)

        fraction_in_percent = round(denominator / divisor, 2) * 100

        if fraction_in_percent > 100:
            continue
        elif fraction_in_percent >= 99:
            print("F")
        elif fraction_in_percent <= 1:
            print("E")
        else:
            print(f"{int(fraction_in_percent)}%")

        break
    except (ValueError, ZeroDivisionError):
        continue
