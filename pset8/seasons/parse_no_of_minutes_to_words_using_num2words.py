from num2words import num2words


def parse_number_of_minutes_to_words(number: int):
    words = num2words(number=number)
    return words.capitalize().replace(" and ", " ") + " minutes"
