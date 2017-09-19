
from tabulate import tabulate

from cube_sum import rec_sum

def est_sum(n):
    return .5 * n**3 + 0.75 * n**2

if __name__ == '__main__':
    output = [['n', 'Sum', '|Sum|', 'Est', 'Error', 'a=E(n)/n^3', 'b=E(n)/n^2', 'c=E(n)/n']]
    for n in range(1, 41):
        s = rec_sum(n)
        sa = abs(s)
        est = est_sum(n)
        error = sa - est
        a = error/n**3
        b = error/n**2
        c = error/n
        output.append([n, s, sa, est, error, a, b, c])

    print(tabulate(output))

