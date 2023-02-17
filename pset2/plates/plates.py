def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:2].isalpha() or not s.isalnum():
        return False

    has_numbers_after_letters = None
    for char in s:
        if char.isnumeric() and not has_numbers_after_letters:
            if char == "0":
                return False
            has_numbers_after_letters = True

        if has_numbers_after_letters and char.isalpha():
            return False

    return True

main()
