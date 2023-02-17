import csv
import sys


def main():
    check_argv()
    students_before = read_csv()

    students_after = []
    for student in students_before:
        last, first = student["name"].split(', ')
        students_after.append({"first": first, "last": last,
                               "house": student["house"]})
    write_csv(students_after)


def check_argv():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
    else:
        return
    sys.exit(1)


def write_csv(rows: list[dict]):

    with open(sys.argv[2], "w") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        [writer.writerow(row) for row in rows]


def read_csv() -> list[dict]:
    try:
        with open(sys.argv[1]) as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print("File does not exists")
        sys.exit(2)


if __name__ == '__main__':
    main()
