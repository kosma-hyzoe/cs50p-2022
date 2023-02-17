import sys


def main():
    if len(sys.argv) != 2:
        print("Too few command line arguments")
        sys.exit(1)
    elif ".py" not in sys.argv[1]:
        print("Not a Python file")
        sys.exit(1)

    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    loc = 0
    for line in lines:
        if line.lstrip() != "" and not line.lstrip().startswith("#"):
            loc += 1

    print(loc)


if __name__ == '__main__':
    main()
