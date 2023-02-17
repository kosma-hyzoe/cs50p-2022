import random
import sys


def main():
    level = get_level()
    score = 0

    for _ in range(1, 11):
        x = generate_integer(level)
        y = generate_integer(level)
        equation = f"{x} + {y} = "
        solution = x + y
        error_count = 0

        while True:
            try:
                user_solution = int(input(equation))
                if int(user_solution) == solution:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                error_count += 1
                print("EEE")
                if error_count == 3:
                    print(f"{equation}{solution}")
                    break

    print(f"Score: {score}")
    sys.exit(0)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 10)
    elif level == 2:
        return random.randint(10, 100)
    elif level == 3:
        return random.randint(100, 1000)


if __name__ == "__main__":
    main()
