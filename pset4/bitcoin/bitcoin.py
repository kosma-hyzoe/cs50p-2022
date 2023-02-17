import sys
import requests


def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")

    try:
        amount = float(sys.argv[1])
        value = amount * check_rate_usd()
        print(f"${value:,.4f}")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)


def check_rate_usd():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        return response.json()["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print("Error: " + str(e))
        sys.exit(1)


main()
