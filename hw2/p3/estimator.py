
def f(n):
    term = (-1)**(n-1) * n**2
    if n <= 1:
        return term
    else:
        return term + f(n-1)

def estimate_1(n):
    return (n**2)/2

def estimate_2(n):
    return (n*(n+1))/2

def estimate_3(n):
    return (-1)**(n-1) * estimate_2(n)

if __name__ == '__main__':
    estimator = estimate_3
    for n in range(20):
        val = f(n)
        est = estimator(n)
        print('n =', n, '\tf(n) =', val, '\test(n) =', est, '\tdiff =', val - est )

