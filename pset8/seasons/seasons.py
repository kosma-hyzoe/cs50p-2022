import sys
import inflect
from datetime import date, datetime

VALID_DATE_FORMAT = "%Y-%m-%d"


def main():
    date_of_birth = input("Date of Birth: ")
    age_in_minutes = get_age_in_minutes(date_of_birth)
    print(parse_number_of_minutes_to_words(age_in_minutes))


def parse_number_of_minutes_to_words(number: int):
    p = inflect.engine()
    words = p.number_to_words(number, andword="")
    return words.capitalize() + " minutes"


def get_age_in_minutes(date_of_birth):
    if not is_valid_date(date_of_birth):
        print("Invalid date")
        sys.exit(1)

    birth_datetime = datetime.strptime(date_of_birth, VALID_DATE_FORMAT)
    today_datetime = datetime.strptime(str(date.today()), VALID_DATE_FORMAT)
    return int((today_datetime - birth_datetime).total_seconds() / 60)


def is_valid_date(date: str):
    try:
        datetime.strptime(date, VALID_DATE_FORMAT)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
