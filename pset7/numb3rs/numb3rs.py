import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip) -> bool:
    if not re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        return False

    numbers = ip.split(".")

    for number in numbers:
        if int(number) not in range(256):
            return False

    return True


if __name__ == "__main__":
    main()
