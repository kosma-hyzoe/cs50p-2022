import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if from_to := re.match(r"^(\d{1,2}(?::\d{1,2})* [AP]M) to (\d{1,2}(?::\d{1,2})* [AP]M)$", s):
        formatted_from_and_to = []
        for time in from_to.groups():
            hour, minutes, meridiem = re.search(r"(\d{1,2}):*(\d{1,2})* ([AP])M", time).groups()

            post_meridiem = True if meridiem == "P" else False
            if int(hour) not in range(1, 13):
                raise ValueError
            else:
                hour = convert_hour(hour, post_meridiem)

            if not minutes:
                formatted_from_and_to.append(f"{hour:02}:00")
            elif not is_minutes_valid(minutes):
                raise ValueError
            else:
                formatted_from_and_to.append(f"{hour:02}:{minutes:02}")
        return " to ".join(formatted_from_and_to)
    else:
        raise ValueError


def convert_hour(hour: str, post_meridiem: bool):
    hour = int(hour)
    if not post_meridiem and hour == 12:
        return 0
    elif post_meridiem and hour == 12:
        return hour
    elif post_meridiem:
        return hour + 12
    else:
        return hour


def is_minutes_valid(minutes: str) -> bool:
    if int(minutes) not in range(0, 60):
        return False
    if int(minutes) in range(0, 10) and "0" not in minutes:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
