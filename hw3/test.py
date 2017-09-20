
def test(g, a, b):
    if a < b:
        a, b = b, a
    if a % g == 0 and b % g == 0:
        _s = a % b
        if _s % g == 0:
            s = _s // g
            t = (g - a*s)//b
            return g == s*a + t*b
    return False

if __name__ == '__main__':
    test_vals = [
        [5, 45, 10],
        [2, 45, 10],
        [1, 45, 10],
        [1, 13, 11],
        [5, 10, 45],
        [9, 36, 27],
        [3, 36, 27],
    ]

    for vals in test_vals:
        print(vals, test(*vals))
