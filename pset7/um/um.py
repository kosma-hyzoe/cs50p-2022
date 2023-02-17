import re
import sys


def main():
    print(input("Text: "))


def count(s):
    if ums := re.findall(r"(^um[,.!?])|( um[,.!?])|( um[,.!?]*$)|(^um$)", s, re.IGNORECASE):
        return len(ums)
    else:
        return 0


if __name__ == "__main__":
    main()

