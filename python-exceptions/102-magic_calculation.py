#!/usr/bin/python3


def magic_calculation():
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except:
            result = b + a
            break
    return result
