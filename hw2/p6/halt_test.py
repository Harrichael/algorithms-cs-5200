
def depth(n):
    if n < 2:
        return 1
    if n % 2 == 1:
        return 1 + depth(3*n + 1)
    else:
        return 1 + depth(n/2)

if __name__ == '__main__':
    low_bound = 1
    hi_bound = 100
    for val in range(low_bound, hi_bound + 1):
        depth(val)

    print('Depth function did not halt for numbers {} to {}'.format(low_bound, hi_bound))

