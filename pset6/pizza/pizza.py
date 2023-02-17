import sys
import csv

from tabulate import tabulate


def main():
    check_argv()
    menu = read_menu()
    print(tabulate(menu[1:], tablefmt="grid", headers=menu[0]))


def read_menu() -> list[str]:
    try:
        with open(sys.argv[1]) as f:
            reader = csv.reader(f)
            return list(reader)
    except FileNotFoundError:
        print("File does not exists")
        sys.exit(2)


def check_argv():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
    else:
        return
    sys.exit(1)


if __name__ == '__main__':
    main()
