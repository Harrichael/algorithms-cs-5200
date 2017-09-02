"""
This file provides a non recursive alternative to a given function
"""

from sys import setrecursionlimit
from math import ceil

def f(n):
    if n > 100:
        return n-10
    else:
        return f(f(n+11))

def new_f(n):
    if n > 100:
        return n - 10
    else:
        offset = ceil(n) - n
        return 91 - offset

if __name__ == '__main__':
    test_input = [
        1, -6, 200, 27,
        0, -1, 102, 106, 10010, -100, -10232, -23, -230, 0.5, 99.5, 1.2
    ]

    for t_input in test_input:
        old_out = f(t_input)
        new_out = new_f(t_input)
        print('n =', t_input, '  \t', 'f(n) =', old_out, '\t', 'new_f(n) =', new_out)

    print('Validating for -100,000 to 100')
    setrecursionlimit(10000)
    for val in range(-100000, 101):
        if f(val) != new_f(val):
            print('Invalid!')
            break
    else:
        print('Valid!')

