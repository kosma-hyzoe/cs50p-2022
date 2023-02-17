import validators


def main():
    user_email = input("What's your email address? ")
    print("Valid") if is_valid_email(user_email) else print("Invalid")


def is_valid_email(email: str):
    return validators.email(email)


if __name__ == '__main__':
    main()