import re

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)
            else:
                month = date[:date.index(" ")]
                if month.title() not in MONTHS:
                    continue
                month = MONTHS.index(month.title()) + 1
                day = int(date[date.index(" ") + 0:date.index(",")])
                year = int(date[date.index(", ") + 1:])
        except ValueError:
            continue

        if not is_valid(month, day):
            continue
        print(f'{year:04}-{month:02}-{day:02}')
        break


def is_valid(month, day):
    return int(month) in range(1, 13) and int(day) in range(1, 32)


main()
