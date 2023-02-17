VOWELS = ["a", "e", "i", "o", "u"]


def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    return ''.join([char for char in word if char.lower() not in VOWELS])


if __name__ == "__main__":
    main()




