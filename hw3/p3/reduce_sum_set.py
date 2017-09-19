
def gcd(a, b):
    rem = a % b
    if 0 == rem:
        return b
    else:
        return gcd(b, rem)

def reduce_set(s):
    if len(s) >= 2:
        x, y = s.pop(), s.pop()
        s.add(gcd(x, y))
        reduce_set(s)

    return s

if __name__ == '__main__':
    input_data = [
        [20, 10,  30, 45,  105, 125, 10],
        [20, 10,  30, 45,  105, -25, 10],
        [72, 144, 12, -60, 120, -6,  24],
        [33126, 312, 2532274, 432040, 23212],
        [540051690381, 5404079462298, 3485942644184],
    ]

    for data in input_data:
        data_set = set(data)
        print(data, reduce_set(data_set))

