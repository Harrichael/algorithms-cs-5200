
c = 17

def f(n):
    if n > 100:
        return n - 10
    else:
        return f(f(n + c))

if __name__ == '__main__':
    for n in range(100 - 2*c, 100 + 2*c):
        print(n, f(n))

