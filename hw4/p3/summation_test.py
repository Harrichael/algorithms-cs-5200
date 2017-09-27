
def n_term(n):
    return (n - 1) / (2 ** n)

def t_summation(n):
    total = 0
    for i in range(n+1):
        total += n_term(i)
    return total

if __name__ == '__main__':
    for test_n in range(0, 1150, 25):
        val = t_summation(test_n)
        print('n =', test_n, '   sum(n) =', val)

