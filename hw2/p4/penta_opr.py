
from sys import setrecursionlimit

def opr(verts, index):
    verts = list(verts)
    verts[index] = -verts[index]
    verts[index-1] = verts[index-1] - verts[index]
    right_index = (index + 1) % len(verts)
    verts[right_index] = verts[right_index] - verts[index]
    return tuple(verts)

def count_opr(*verts):
    return max([1 + count_opr(*opr(verts, i)) for i, v in enumerate(verts) if v < 0], default=0)

if __name__ == '__main__':
    test_input = [
        (10,    -9,     8,     -9,     8),
        (-100,  -10,   -1000,  -1,     10000),
        (100,   -10,   -10,    12,     -1),
        (8,     100,   -12,    -26,    -2),
        (-1,    -1,    -1,     -1,     5),
    ]

    recursion_limit = 10000
    setrecursionlimit(recursion_limit)
    max_input_len = max(map(len, map(str, test_input)))
    try:
        for test in test_input:
            num_spaces = max_input_len - len(str(test))
            print('test =', test, ' '*num_spaces, 'max opr :', count_opr(*test))
    except RecursionError:
        print('You reached recursion limit of {}!'.format(recursion_limit))

