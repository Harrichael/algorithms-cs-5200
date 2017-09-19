
def rec_sum(n):
    if n <= 1:
        return 1
    else:
        sign = (-1)**(n-1)
        return sign * n**3 + rec_sum(n-1)

def n_term(n):
    if n % 2 == 0:
        sign = -1
    else:
        sign = 1

    return sign * n ** 3

def cube_sum(n):
    return sum(map(n_term, range(1, n+1)))

