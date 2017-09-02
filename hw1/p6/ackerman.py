"""
Test out the ackerman function
"""

from sys import setrecursionlimit

def acker(x,y):
    if x == 0:
        return y+1
    elif y == 0:
        return acker(x-1,1)
    else:
        return acker(x-1, acker(x,y-1))

if __name__ == '__main__':
    test_input = [
        (0, 0),
        (0, 10000000000),
        (1, 0),
        (1, 1),
        (1, 5),
        (1, 9995),
        (2, 0),
        (2, 1),
        (2, 5),
        (2, 2000),
        (3, 0),
        (3, 1),
        (3, 5),
        (3, 9),
        (4, 0),
        # (4, 1) Long time but hits recursion limit
        # (5, 0), Hits recursion limit
    ]

    setrecursionlimit(10000)
    for t_input in test_input:
        print('input =', t_input, '\t', 'acker =', acker(*t_input))
