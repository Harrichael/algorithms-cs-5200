
def f(n):
    term = (-1)**(n-1) * n**2
    if n <= 1:
        return term
    else:
        return term + f(n-1)

def estimate_1(n):
    return (n**2)/2

if __name__ == '__main__':
    estimator = estimate_1
    for n in range(20):
        val = f(n)
        est = estimator(n)
        print('n =', n, '\tf(n) =', val, '\test(n) =', est, '\tdiff =', val - est )

