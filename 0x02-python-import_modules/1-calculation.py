#!/usr/bin/python3
if __name__ == '__main__':
    import calculator_1 as calc
    a = 10
    b = 5
    c = calc.add(a, b)
    print("{} + {} = {}".format(a, b, c))
    d = calc.sub(a, b)
    print("{} - {} = {}".format(a, b, d))
    e = calc.mul(a, b)
    print("{} * {} = {}".format(a, b, e))
    f = calc.div(a, b)
    print("{} / {} = {}".format(a, b, f))
