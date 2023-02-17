def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction: str):
    denominator, divisor = fraction.split("/")
    denominator, divisor = int(denominator), int(divisor)

    if divisor == 0:
        raise ZeroDivisionError
    elif denominator > divisor:
        raise ValueError

    return round(denominator / divisor, 2) * 100


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{int(percentage)}%"
