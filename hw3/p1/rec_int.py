
c = 14

def f(n):
    if n > 100:
        return n - 10
    else:
        return f(f(n + c))

def simpl_f(n):
    if n > 100:
        return n - 10
    elif c <= 10:
        while True:
            pass
    else:
        period = c - 10
        diff = 100 - n
        return 90 + period - diff % period

if __name__ == '__main__':
    for n in range(100 - 2*c, 100):
        print(n, f(n), simpl_f(n))

