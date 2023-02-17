def main():
    what_time = input("What time is it?")
    converted_time = convert(what_time)

    if 8 >= converted_time >= 7:
        print("Breakfast time")
    elif 13 >= converted_time >= 12:
        print("Lunch time")
    elif 19 >= converted_time >= 18:
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = round(int(minutes) / 60, 2)
    return float(hours) + minutes


if __name__ == "__main__":
    main()
