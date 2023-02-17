from datetime import timedelta
from seasons import *


def test_seasons():
    assert not is_valid_date("2022-16-02")
    assert is_valid_date("2022-02-16")
    print(get_age_in_minutes("2021-02-16"))
    assert parse_number_of_minutes_to_words(get_age_in_minutes("2021-02-16")) == "One million, fifty-one thousand, two hundred minutes"
    today_a_year_ago = date.today() - timedelta(days=365)
    assert get_age_in_minutes(str(today_a_year_ago)) == 525600
