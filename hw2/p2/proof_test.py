
def sum(values, start = 0):
    total = start
    for value in values:
        total = total + value
    return total

def gcd(a, b):
    rem = a % b
    if 0 == rem:
        return b
    else:
        return gcd(b, rem)


class Fraction(object):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        return type(self)(self.num*other.den + other.num*self.den, self.den * other.den)

    def __eq__(self, other):
        return self.num*other.den == other.num*self.den

def summation(f, vals):
    return sum(map(f, vals), start=Fraction(0,1))

def f_i(i):
    return Fraction(i**2,  ( (2*i-1)*(2*i+1) ))

def sum_f_i(vals):
    return summation(f_i, vals)

def f_n(n):
    return Fraction(n*(n+1), (2*(2*n+1) ))


if __name__ == '__main__':
    max_val = 5000
    for val in range(1, max_val + 1):
        sum_val = sum_f_i(range(1,val+1))
        f_val = f_n(val)
        if sum_val != f_val:
            print('Conjecture does not hold for value: {}, got sum: {} and f(n): {}'.format(val, sum_val, f_val))
            break
    else:
        print('Success, worked for all values 1 to {}'.format(max_val))

