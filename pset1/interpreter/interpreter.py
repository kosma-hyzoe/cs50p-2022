import sys


expression = input("Expression: ")
x, modifier, y = expression.split(" ")

match modifier:
    case "/":
        print(float(int(x) / int(y)))
    case "*":
        print(float(int(x) * int(y)))
    case "+":
        print(float(int(x) + int(y)))
    case "-":
        print(float(int(x) - int(y)))
