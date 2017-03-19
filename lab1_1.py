# -*- coding: utf-8 -*-
__operators = ('+', '-', '/', '//', '*', '**', '%')


def calculator():
    x = input()
    operator = input()
    y = input()

    print(str(x) + operator + str(y))

    if operator == "+":
        rezultat = x+y
    elif operator == "**":
        rezultat = x**y
    elif operator == "-":
        rezultat = x-y
    elif operator == "/":
        rezultat = x/y
    elif operator == "//":
        rezultat = x//y
    elif operator == "*":
        rezultat = x*y
    else:
        rezultat = x % y

    print(rezultat)
    return rezultat


if __name__ == "__main__":
    calculator()